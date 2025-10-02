"""Dataset management for DerivaML.

This module provides functionality for managing datasets in DerivaML. A dataset represents a collection
of related data that can be versioned, downloaded, and tracked. The module includes:

- Dataset class: Core class for dataset operations
- Version management: Track and update dataset versions
- History tracking: Record dataset changes over time
- Download capabilities: Export datasets as BDBags
- Relationship management: Handle dataset dependencies and hierarchies

The Dataset class serves as a base class in DerivaML, making its methods accessible through
DerivaML class instances.

Typical usage example:
    >>> ml = DerivaML('deriva.example.org', 'my_catalog')
    >>> dataset_rid = ml.create_dataset('experiment', 'Experimental data')
    >>> ml.add_dataset_members(dataset_rid=dataset_rid, members=['1-abc123', '1-def456'])
    >>> ml.increment_dataset_version(datset_rid=dataset_rid, component=VersionPart.minor,
    ...     description='Added new samples')
"""

from __future__ import annotations

# Standard library imports
import json
import logging
from collections import defaultdict
from graphlib import TopologicalSorter
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any, Callable, Iterable, Iterator

import deriva.core.utils.hash_utils as hash_utils
import requests

# Third-party imports
from bdbag import bdbag_api as bdb
from bdbag.fetch.fetcher import fetch_single_file

# Deriva imports
from deriva.core.ermrest_model import Table
from deriva.core.utils.core_utils import format_exception
from deriva.core.utils.core_utils import tag as deriva_tags
from deriva.transfer.download.deriva_download import (
    DerivaDownloadAuthenticationError,
    DerivaDownloadAuthorizationError,
    DerivaDownloadConfigurationError,
    DerivaDownloadError,
    DerivaDownloadTimeoutError,
)
from deriva.transfer.download.deriva_export import DerivaExport
from pydantic import ConfigDict, validate_call

# Local imports
try:
    from icecream import ic

    ic.configureOutput(includeContext=True)
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from deriva_ml.core.constants import RID
from deriva_ml.core.definitions import (
    DRY_RUN_RID,
    ML_SCHEMA,
    MLVocab,
    Status,
)
from deriva_ml.core.exceptions import DerivaMLException, DerivaMLTableTypeError
from deriva_ml.dataset.aux_classes import (
    DatasetHistory,
    DatasetMinid,
    DatasetSpec,
    DatasetVersion,
    VersionPart,
)
from deriva_ml.dataset.dataset_bag import DatasetBag
from deriva_ml.model.catalog import DerivaModel
from deriva_ml.model.database import DatabaseModel

from .history import iso_to_snap

# Stop pycharm from complaining about undefined reference in docstring....
ml: DerivaML

if TYPE_CHECKING:
    from deriva_ml.core.base import DerivaML


class Dataset:
    """Manages dataset operations in a Deriva catalog.

    The Dataset class provides functionality for creating, modifying, and tracking datasets
    in a Deriva catalog. It handles versioning, relationships between datasets, and data export.

    Attributes:
        dataset_table (Table): ERMrest table storing dataset information.
        _model (DerivaModel): Catalog model instance.
        _ml_schema (str): Schema name for ML-specific tables.
        _cache_dir (Path): Directory for caching downloaded datasets.
        _working_dir (Path): Directory for working data.
        _use_minid (bool): Whether to use MINID service for dataset identification.

    Note:
        This class is typically used as a base class, with its methods accessed through
        DerivaML class instances rather than directly.
    """

    _Logger = logging.getLogger("deriva_ml")

    def __init__(
        self,
        model: DerivaModel,
        cache_dir: Path,
        working_dir: Path,
        use_minid: bool = True,
    ):
        """Initializes a Dataset instance.

        Args:
            model: DerivaModel instance representing the catalog.
            cache_dir: Directory path for caching downloaded datasets.
            working_dir: Directory path for working data.
            use_minid: Whether to use MINID service for dataset identification.
        """
        self._model = model
        self._ml_schema = ML_SCHEMA
        self._cache_dir = cache_dir
        self._working_dir = working_dir
        self._logger = logging.getLogger("deriva_ml")
        self._use_minid = use_minid

    @property
    def _dataset_table(self):
        return self._model.schemas[self._ml_schema].tables["Dataset"]

    def _is_dataset_rid(self, dataset_rid: RID, deleted: bool = False) -> bool:
        try:
            rid_info = self._model.catalog.resolve_rid(dataset_rid, self._model.model)
        except KeyError as _e:
            raise DerivaMLException(f"Invalid RID {dataset_rid}")
        if rid_info.table != self._dataset_table:
            return False
        elif deleted:
            # Got a dataset rid. Now check to see if its deleted or not.
            return True
        else:
            return not list(rid_info.datapath.entities().fetch())[0]["Deleted"]

    def _insert_dataset_versions(
        self,
        dataset_list: list[DatasetSpec],
        description: str | None = "",
        execution_rid: RID | None = None,
    ) -> None:
        schema_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema]
        # determine snapshot after changes were made

        # Construct version records for insert
        version_records = schema_path.tables["Dataset_Version"].insert(
            [
                {
                    "Dataset": dataset.rid,
                    "Version": str(dataset.version),
                    "Description": description,
                    "Execution": execution_rid,
                }
                for dataset in dataset_list
            ]
        )
        version_records = list(version_records)
        snap = self._model.catalog.get("/").json()["snaptime"]
        schema_path.tables["Dataset_Version"].update(
            [{"RID": v["RID"], "Dataset": v["Dataset"], "Snapshot": snap} for v in version_records]
        )

        # And update the dataset records.
        schema_path.tables["Dataset"].update([{"Version": v["RID"], "RID": v["Dataset"]} for v in version_records])

    def _bootstrap_versions(self):
        datasets = [ds["RID"] for ds in self.find_datasets()]
        ds_version = [
            {
                "Dataset": d,
                "Version": "0.1.0",
                "Description": "Dataset at the time of conversion to versioned datasets",
            }
            for d in datasets
        ]
        schema_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema]
        version_path = schema_path.tables["Dataset_Version"]
        dataset_path = schema_path.tables["Dataset"]
        history = list(version_path.insert(ds_version))
        dataset_versions = [{"RID": h["Dataset"], "Version": h["Version"]} for h in history]
        dataset_path.update(dataset_versions)

    def _synchronize_dataset_versions(self):
        datasets = [ds["RID"] for ds in self.find_datasets()]
        for ds in datasets:
            self.dataset_version(ds)
        schema_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema]
        dataset_version_path = schema_path.tables["Dataset_Version"]
        # Get the maximum version number for each dataset.
        versions = {}
        for v in dataset_version_path.entities().fetch():
            if v["Version"] > versions.get("Dataset", DatasetVersion(0, 0, 0)):
                versions[v["Dataset"]] = v
        dataset_path = schema_path.tables["Dataset"]

        dataset_path.update([{"RID": dataset, "Version": version["RID"]} for dataset, version in versions.items()])

    def _set_version_snapshot(self):
        """Update the Snapshot column of the Dataset_Version table to the correct time."""
        dataset_version_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables["Dataset_Version"]
        versions = dataset_version_path.entities().fetch()
        dataset_version_path.update(
            [{"RID": h["RID"], "Snapshot": iso_to_snap(h["RCT"])} for h in versions if not h["Snapshot"]]
        )

    def dataset_history(self, dataset_rid: RID) -> list[DatasetHistory]:
        """Retrieves the version history of a dataset.

        Returns a chronological list of dataset versions, including their version numbers,
        creation times, and associated metadata.

        Args:
            dataset_rid: Resource Identifier of the dataset.

        Returns:
            list[DatasetHistory]: List of history entries, each containing:
                - dataset_version: Version number (major.minor.patch)
                - minid: Minimal Viable Identifier
                - snapshot: Catalog snapshot time
                - dataset_rid: Dataset Resource Identifier
                - version_rid: Version Resource Identifier
                - description: Version description
                - execution_rid: Associated execution RID

        Raises:
            DerivaMLException: If dataset_rid is not a valid dataset RID.

        Example:
            >>> history = ml.dataset_history("1-abc123")
            >>> for entry in history:
            ...     print(f"Version {entry.dataset_version}: {entry.description}")
        """

        if not self._is_dataset_rid(dataset_rid):
            raise DerivaMLException(f"RID is not for a data set: {dataset_rid}")
        version_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables["Dataset_Version"]
        return [
            DatasetHistory(
                dataset_version=DatasetVersion.parse(v["Version"]),
                minid=v["Minid"],
                snapshot=v["Snapshot"],
                dataset_rid=dataset_rid,
                version_rid=v["RID"],
                description=v["Description"],
                execution_rid=v["Execution"],
            )
            for v in version_path.filter(version_path.Dataset == dataset_rid).entities().fetch()
        ]

    @validate_call
    def dataset_version(self, dataset_rid: RID) -> DatasetVersion:
        """Retrieve the current version of the specified dataset_table.

        Given a rid, return the most recent version of the dataset. It is important to remember that this version
        captures the state of the catalog at the time the version was created, not the current state of the catalog.
        This means that its possible that the values associated with an object in the catalog may be different
        from the values of that object in the dataset.

        Args:
            dataset_rid: The RID of the dataset to retrieve the version for.

        Returns:
            A tuple with the semantic version of the dataset_table.
        """
        history = self.dataset_history(dataset_rid)
        if not history:
            return DatasetVersion(0, 1, 0)
        else:
            # Ensure we return a DatasetVersion, not a string
            versions = [h.dataset_version for h in history]
            return max(versions) if versions else DatasetVersion(0, 1, 0)

    def _build_dataset_graph(self, dataset_rid: RID) -> Iterable[RID]:
        ts: TopologicalSorter = TopologicalSorter()
        self._build_dataset_graph_1(dataset_rid, ts, set())
        return ts.static_order()

    def _build_dataset_graph_1(self, dataset_rid: RID, ts: TopologicalSorter, visited) -> None:
        """Use topological sort to return bottom up list of nested datasets"""
        ts.add(dataset_rid)
        if dataset_rid not in visited:
            visited.add(dataset_rid)
            children = self.list_dataset_children(dataset_rid=dataset_rid)
            parents = self.list_dataset_parents(dataset_rid=dataset_rid)
            for parent in parents:
                # Convert string to RID type
                self._build_dataset_graph_1(RID(parent), ts, visited)
            for child in children:
                self._build_dataset_graph_1(child, ts, visited)

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def increment_dataset_version(
        self,
        dataset_rid: RID,
        component: VersionPart,
        description: str | None = "",
        execution_rid: RID | None = None,
    ) -> DatasetVersion:
        """Increments a dataset's version number.

        Creates a new version of the dataset by incrementing the specified version component
        (major, minor, or patch). The new version is recorded with an optional description
        and execution reference.

        Args:
            dataset_rid: Resource Identifier of the dataset to version.
            component: Which version component to increment ('major', 'minor', or 'patch').
            description: Optional description of the changes in this version.
            execution_rid: Optional execution RID to associate with this version.

        Returns:
            DatasetVersion: The new version number.

        Raises:
            DerivaMLException: If dataset_rid is invalid or version increment fails.

        Example:
            >>> new_version = ml.increment_dataset_version(
            ...     dataset_rid="1-abc123",
            ...     component="minor",
            ...     description="Added new samples"
            ... )
            >>> print(f"New version: {new_version}")  # e.g., "1.2.0"
        """

        # Find all the datasets that are reachable from this dataset and determine their new version numbers.
        related_datasets = list(self._build_dataset_graph(dataset_rid=dataset_rid))
        version_update_list = [
            DatasetSpec(
                rid=ds_rid,
                version=self.dataset_version(ds_rid).increment_version(component),
            )
            for ds_rid in related_datasets
        ]
        self._insert_dataset_versions(version_update_list, description=description, execution_rid=execution_rid)
        return next((d.version for d in version_update_list if d.rid == dataset_rid))

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def create_dataset(
        self,
        dataset_types: str | list[str] | None = None,
        description: str = "",
        execution_rid: RID | None = None,
        version: DatasetVersion | None = None,
    ) -> RID:
        """Creates a new dataset in the catalog.

        Creates a dataset with specified types and description. The dataset can be associated
        with an execution and initialized with a specific version.

        Args:
            dataset_types: One or more dataset type terms from Dataset_Type vocabulary.
            description: Description of the dataset's purpose and contents.
            execution_rid: Optional execution RID to associate with dataset creation.
            version: Optional initial version number. Defaults to 0.1.0.

        Returns:
            RID: Resource Identifier of the newly created dataset.

        Raises:
            DerivaMLException: If dataset_types are invalid or creation fails.

        Example:
            >>> rid = ml.create_dataset(
            ...     dataset_types=["experiment", "raw_data"],
            ...     description="RNA sequencing experiment data",
            ...     version=DatasetVersion(1, 0, 0)
            ... )
        """

        version = version or DatasetVersion(0, 1, 0)
        dataset_types = dataset_types or []

        type_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables[MLVocab.dataset_type.value]
        defined_types = list(type_path.entities().fetch())

        def check_dataset_type(dtype: str) -> bool:
            for term in defined_types:
                if dtype == term["Name"] or (term["Synonyms"] and ds_type in term["Synonyms"]):
                    return True
            return False

        # Create the entry for the new dataset_table and get its RID.
        ds_types = [dataset_types] if isinstance(dataset_types, str) else dataset_types
        pb = self._model.catalog.getPathBuilder()
        for ds_type in ds_types:
            if not check_dataset_type(ds_type):
                raise DerivaMLException("Dataset type must be a vocabulary term.")
        dataset_table_path = pb.schemas[self._dataset_table.schema.name].tables[self._dataset_table.name]
        dataset_rid = dataset_table_path.insert(
            [
                {
                    "Description": description,
                    "Deleted": False,
                }
            ]
        )[0]["RID"]

        # Get the name of the association table between dataset_table and dataset_type.
        associations = list(self._model.schemas[self._ml_schema].tables[MLVocab.dataset_type].find_associations())
        atable = associations[0].name if associations else None
        pb.schemas[self._ml_schema].tables[atable].insert(
            [{MLVocab.dataset_type: ds_type, "Dataset": dataset_rid} for ds_type in ds_types]
        )
        if execution_rid is not None:
            pb.schemas[self._ml_schema].Dataset_Execution.insert([{"Dataset": dataset_rid, "Execution": execution_rid}])
        self._insert_dataset_versions(
            [DatasetSpec(rid=dataset_rid, version=version)],
            execution_rid=execution_rid,
            description="Initial dataset creation.",
        )
        return dataset_rid

    @validate_call
    def delete_dataset(self, dataset_rid: RID, recurse: bool = False) -> None:
        """Delete a dataset_table from the catalog.

        Args:
            dataset_rid: RID of the dataset_table to delete.
            recurse: If True, delete the dataset_table along with any nested datasets. (Default value = False)
        """
        # Get association table entries for this dataset_table
        # Delete association table entries
        if not self._is_dataset_rid(dataset_rid):
            raise DerivaMLException("Dataset_rid is not a dataset.")

        if parents := self.list_dataset_parents(dataset_rid):
            raise DerivaMLException(f'Dataset_rid "{dataset_rid}" is in a nested dataset: {parents}.')

        pb = self._model.catalog.getPathBuilder()
        dataset_path = pb.schemas[self._dataset_table.schema.name].tables[self._dataset_table.name]

        rid_list = [dataset_rid] + (self.list_dataset_children(dataset_rid=dataset_rid) if recurse else [])
        dataset_path.update([{"RID": r, "Deleted": True} for r in rid_list])

    def find_datasets(self, deleted: bool = False) -> Iterable[dict[str, Any]]:
        """Returns a list of currently available datasets.

        Arguments:
            deleted: If True, included the datasets that have been deleted.

        Returns:
             list of currently available datasets.
        """
        # Get datapath to all the tables we will need: Dataset, DatasetType and the association table.
        pb = self._model.catalog.getPathBuilder()
        dataset_path = pb.schemas[self._dataset_table.schema.name].tables[self._dataset_table.name]
        associations = list(self._model.schemas[self._ml_schema].tables[MLVocab.dataset_type].find_associations())
        atable = associations[0].name if associations else None
        ml_path = pb.schemas[self._ml_schema]
        atable_path = ml_path.tables[atable]

        if deleted:
            filtered_path = dataset_path
        else:
            filtered_path = dataset_path.filter(
                (dataset_path.Deleted == False) | (dataset_path.Deleted == None)  # noqa: E711, E712
            )

        # Get a list of all the dataset_type values associated with this dataset_table.
        datasets = []
        for dataset in filtered_path.entities().fetch():
            ds_types = (
                atable_path.filter(atable_path.Dataset == dataset["RID"]).attributes(atable_path.Dataset_Type).fetch()
            )
            datasets.append(dataset | {MLVocab.dataset_type: [ds[MLVocab.dataset_type] for ds in ds_types]})
        return datasets

    def list_dataset_element_types(self) -> Iterable[Table]:
        """List the types of entities that can be added to a dataset_table.

        Returns:
          :return: An iterable of Table objects that can be included as an element of a dataset_table.
        """

        def domain_table(table: Table) -> bool:
            return table.schema.name == self._model.domain_schema or table.name == self._dataset_table.name

        return [t for a in self._dataset_table.find_associations() if domain_table(t := a.other_fkeys.pop().pk_table)]

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def add_dataset_element_type(self, element: str | Table) -> Table:
        """A dataset_table is a heterogeneous collection of objects, each of which comes from a different table. This
        routine makes it possible to add objects from the specified table to a dataset_table.

        Args:
            element: Name of the table or table object that is to be added to the dataset_table.

        Returns:
            The table object that was added to the dataset_table.
        """
        # Add table to map
        element_table = self._model.name_to_table(element)
        atable_def = Table.define_association([self._dataset_table, element_table])
        try:
            table = self._model.schemas[self._model.domain_schema].create_table(atable_def)
        except ValueError as e:
            if "already exists" in str(e):
                table = self._model.name_to_table(atable_def["table_name"])
            else:
                raise e

        # self.model = self.catalog.getCatalogModel()
        self._dataset_table.annotations.update(self._generate_dataset_download_annotations())
        self._model.model.apply()
        return table

    # @validate_call
    def list_dataset_members(
        self, dataset_rid: RID, recurse: bool = False, limit: int | None = None
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists members of a dataset.

        Returns a dictionary mapping member types to lists of member records. Can optionally
        recurse through nested datasets and limit the number of results.

        Args:
            dataset_rid: Resource Identifier of the dataset.
            recurse: Whether to include members of nested datasets. Defaults to False.
            limit: Maximum number of members to return per type. None for no limit.

        Returns:
            dict[str, list[dict[str, Any]]]: Dictionary mapping member types to lists of members.
                Each member is a dictionary containing the record's attributes.

        Raises:
            DerivaMLException: If dataset_rid is invalid.

        Example:
            >>> members = ml.list_dataset_members("1-abc123", recurse=True)
            >>> for type_name, records in members.items():
            ...     print(f"{type_name}: {len(records)} records")
        """

        if not self._is_dataset_rid(dataset_rid):
            raise DerivaMLException(f"RID is not for a dataset_table: {dataset_rid}")

        # Look at each of the element types that might be in the dataset_table and get the list of rid for them from
        # the appropriate association table.
        members = defaultdict(list)
        pb = self._model.catalog.getPathBuilder()
        for assoc_table in self._dataset_table.find_associations():
            other_fkey = assoc_table.other_fkeys.pop()
            target_table = other_fkey.pk_table
            member_table = assoc_table.table

            # Look at domain tables and nested datasets.
            if target_table.schema.name != self._model.domain_schema and not (
                target_table == self._dataset_table or target_table.name == "File"
            ):
                continue
            member_column = (
                "Nested_Dataset" if target_table == self._dataset_table else other_fkey.foreign_key_columns[0].name
            )

            target_path = pb.schemas[target_table.schema.name].tables[target_table.name]
            member_path = pb.schemas[member_table.schema.name].tables[member_table.name]

            path = member_path.filter(member_path.Dataset == dataset_rid).link(
                target_path,
                on=(member_path.columns[member_column] == target_path.columns["RID"]),
            )
            target_entities = list(path.entities().fetch(limit=limit) if limit else path.entities().fetch())
            members[target_table.name].extend(target_entities)
            if recurse and target_table == self._dataset_table:
                # Get the members for all the nested datasets and add to the member list.
                nested_datasets = [d["RID"] for d in target_entities]
                for ds in nested_datasets:
                    for k, v in self.list_dataset_members(ds, recurse=recurse).items():
                        members[k].extend(v)
        return dict(members)

    @validate_call
    def add_dataset_members(
        self,
        dataset_rid: RID,
        members: list[RID] | dict[str, list[RID]],
        validate: bool = True,
        description: str | None = "",
        execution_rid: RID | None = None,
    ) -> None:
        """Adds members to a dataset.

        Associates one or more records with a dataset. Can optionally validate member types
        and create a new dataset version to track the changes.

        Args:
            dataset_rid: Resource Identifier of the dataset.
            members: List of RIDs to add as dataset members. Can be orginized into a dictionary that indicates the
                table that the member rids belong to.
            validate: Whether to validate member types. Defaults to True.
            description: Optional description of the member additions.
            execution_rid: Optional execution RID to associate with changes.

        Raises:
            DerivaMLException: If:
                - dataset_rid is invalid
                - members are invalid or of wrong type
                - adding members would create a cycle
                - validation fails

        Example:
            >>> ml.add_dataset_members(
            ...     dataset_rid="1-abc123",
            ...     members=["1-def456", "1-ghi789"],
            ...     description="Added sample data"
            ... )
        """
        description = description or "Updated dataset via add_dataset_members"

        def check_dataset_cycle(member_rid, path=None):
            """

            Args:
              member_rid:
              path: (Default value = None)

            Returns:

            """
            path = path or set(dataset_rid)
            return member_rid in path

        if validate:
            existing_rids = set(m["RID"] for ms in self.list_dataset_members(dataset_rid).values() for m in ms)
            if overlap := set(existing_rids).intersection(members):
                raise DerivaMLException(f"Attempting to add existing member to dataset_table {dataset_rid}: {overlap}")

        # Now go through every rid to be added to the data set and sort them based on what association table entries
        # need to be made.
        dataset_elements = {}
        association_map = {
            a.other_fkeys.pop().pk_table.name: a.table.name for a in self._dataset_table.find_associations()
        }

        # Get a list of all the object types that can be linked to a dataset_table.
        if type(members) is list:
            members = set(members)
            for m in members:
                try:
                    rid_info = self._model.catalog.resolve_rid(m)
                except KeyError:
                    raise DerivaMLException(f"Invalid RID: {m}")
                if rid_info.table.name not in association_map:
                    raise DerivaMLException(f"RID table: {rid_info.table.name} not part of dataset_table")
                if rid_info.table == self._dataset_table and check_dataset_cycle(rid_info.rid):
                    raise DerivaMLException("Creating cycle of datasets is not allowed")
                dataset_elements.setdefault(rid_info.table.name, []).append(rid_info.rid)
        else:
            dataset_elements = {t: set(ms) for t, ms in members.items()}
        # Now make the entries into the association tables.
        pb = self._model.catalog.getPathBuilder()
        for table, elements in dataset_elements.items():
            schema_path = pb.schemas[
                self._ml_schema if (table == "Dataset" or table == "File") else self._model.domain_schema
            ]
            fk_column = "Nested_Dataset" if table == "Dataset" else table
            if len(elements):
                # Find out the name of the column in the association table.
                schema_path.tables[association_map[table]].insert(
                    [{"Dataset": dataset_rid, fk_column: e} for e in elements]
                )
        self.increment_dataset_version(
            dataset_rid,
            VersionPart.minor,
            description=description,
            execution_rid=execution_rid,
        )

    @validate_call
    def delete_dataset_members(
        self,
        dataset_rid: RID,
        members: list[RID],
        description: str = "",
        execution_rid: RID | None = None,
    ) -> None:
        """Remove elements to an existing dataset_table.

        Delete elements from an existing dataset. In addition to deleting members, the minor version number of the
        dataset is incremented and the description, if provide is applied to that new version.

        Args:
            dataset_rid: RID of dataset_table to extend or None if a new dataset_table is to be created.
            members: List of member RIDs to add to the dataset_table.
            description: Markdown description of the updated dataset.
            execution_rid: Optional RID of execution associated with this operation.
        """

        members = set(members)
        description = description or "Deletes dataset members"

        # Now go through every rid to be added to the data set and sort them based on what association table entries
        # need to be made.
        dataset_elements = {}
        association_map = {
            a.other_fkeys.pop().pk_table.name: a.table.name for a in self._dataset_table.find_associations()
        }
        # Get a list of all the object types that can be linked to a dataset_table.
        for m in members:
            try:
                rid_info = self._model.catalog.resolve_rid(m)
            except KeyError:
                raise DerivaMLException(f"Invalid RID: {m}")
            if rid_info.table.name not in association_map:
                raise DerivaMLException(f"RID table: {rid_info.table.name} not part of dataset_table")
            dataset_elements.setdefault(rid_info.table.name, []).append(rid_info.rid)
        # Now make the entries into the association tables.
        pb = self._model.catalog.getPathBuilder()
        for table, elements in dataset_elements.items():
            schema_path = pb.schemas[self._ml_schema if table == "Dataset" else self._model.domain_schema]
            fk_column = "Nested_Dataset" if table == "Dataset" else table

            if len(elements):
                atable_path = schema_path.tables[association_map[table]]
                # Find out the name of the column in the association table.
                for e in elements:
                    entity = atable_path.filter(
                        (atable_path.Dataset == dataset_rid) & (atable_path.columns[fk_column] == e),
                    )
                    entity.delete()
        self.increment_dataset_version(
            dataset_rid,
            VersionPart.minor,
            description=description,
            execution_rid=execution_rid,
        )

    @validate_call
    def list_dataset_parents(self, dataset_rid: RID) -> list[str]:
        """Given a dataset_table RID, return a list of RIDs of the parent datasets if this is included in a
        nested dataset.

        Args:
            dataset_rid: return: RID of the parent dataset_table.

        Returns:
            RID of the parent dataset_table.
        """
        if not self._is_dataset_rid(dataset_rid):
            raise DerivaMLException(f"RID: {dataset_rid} does not belong to dataset_table {self._dataset_table.name}")
        # Get association table for nested datasets
        pb = self._model.catalog.getPathBuilder()
        atable_path = pb.schemas[self._ml_schema].Dataset_Dataset
        return [p["Dataset"] for p in atable_path.filter(atable_path.Nested_Dataset == dataset_rid).entities().fetch()]

    @validate_call
    def list_dataset_children(self, dataset_rid: RID, recurse: bool = False) -> list[RID]:
        """Given a dataset_table RID, return a list of RIDs for any nested datasets.

        Args:
            dataset_rid: A dataset_table RID.
            recurse: If True, return a list of nested datasets RIDs.

        Returns:
          list of nested dataset RIDs.

        """
        dataset_dataset_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables["Dataset_Dataset"]
        nested_datasets = list(dataset_dataset_path.entities().fetch())

        def find_children(rid: RID):
            children = [child["Nested_Dataset"] for child in nested_datasets if child["Dataset"] == rid]
            if recurse:
                for child in children.copy():
                    children.extend(find_children(child))
            return children

        return find_children(dataset_rid)

    def _export_vocabulary(self, writer: Callable[[str, str, Table], list[dict[str, Any]]]) -> list[dict[str, Any]]:
        """

        Args:
          writer: Callable[[list[Table]]: list[dict[str: Any]]]:

        Returns:

        """
        vocabs = [
            table
            for s in self._model.schemas.values()
            for table in s.tables.values()
            if self._model.is_vocabulary(table)
        ]
        return [o for table in vocabs for o in writer(f"{table.schema.name}:{table.name}", table.name, table)]

    def _table_paths(
        self,
        dataset: DatasetSpec | None = None,
        snapshot_catalog: DerivaML | None = None,
    ) -> Iterator[tuple[str, str, Table]]:
        paths = self._collect_paths(dataset and dataset.rid, snapshot_catalog)

        def source_path(path: tuple[Table, ...]) -> list[str]:
            """Convert a tuple representing a path into a source path component with FK linkage"""
            path = list(path)
            p = [f"{self._model.ml_schema}:Dataset/RID={{RID}}"]
            for table in path[1:]:
                if table.name == "Dataset_Dataset":
                    p.append("(RID)=(deriva-ml:Dataset_Dataset:Dataset)")
                elif table.name == "Dataset":
                    p.append("(Nested_Dataset)=(deriva-ml:Dataset:RID)")
                elif table.name == "Dataset_Version":
                    p.append(f"(RID)=({self._model.ml_schema}:Dataset_Version:Dataset)")
                else:
                    p.append(f"{table.schema.name}:{table.name}")
            return p

        src_paths = ["/".join(source_path(p)) for p in paths]
        dest_paths = ["/".join([t.name for t in p]) for p in paths]
        target_tables = [p[-1] for p in paths]
        return zip(src_paths, dest_paths, target_tables)

    def _collect_paths(
        self,
        dataset_rid: RID | None = None,
        snapshot: Dataset | None = None,
        dataset_nesting_depth: int | None = None,
    ) -> set[tuple[Table, ...]]:
        snapshot_catalog = snapshot if snapshot else self

        dataset_table = snapshot_catalog._model.schemas[self._ml_schema].tables["Dataset"]
        dataset_dataset = snapshot_catalog._model.schemas[self._ml_schema].tables["Dataset_Dataset"]

        # Figure out what types of elements the dataset contains.
        dataset_associations = [
            a
            for a in self._dataset_table.find_associations()
            if a.table.schema.name != self._ml_schema or a.table.name == "Dataset_Dataset"
        ]
        if dataset_rid:
            # Get a list of the members of the dataset so we can figure out which tables to query.
            dataset_elements = [
                snapshot_catalog._model.name_to_table(e)
                for e, m in snapshot_catalog.list_dataset_members(
                    dataset_rid=dataset_rid,  #  limit=1 Limit seems to make things run slow.
                ).items()
                if m
            ]
            included_associations = [
                a.table for a in dataset_table.find_associations() if a.other_fkeys.pop().pk_table in dataset_elements
            ]
        else:
            included_associations = dataset_associations

        # Get the paths through the schema and filter out all the dataset paths not used by this dataset.
        paths = {
            tuple(p)
            for p in snapshot_catalog._model._schema_to_paths()
            if (len(p) == 1)
            or (p[1] not in dataset_associations)  # Tables in the domain schema
            or (p[1] in included_associations)  # Tables that include members of the dataset
        }
        # Now get paths for nested datasets
        nested_paths = set()
        if dataset_rid:
            for c in snapshot_catalog.list_dataset_children(dataset_rid=dataset_rid):
                nested_paths |= self._collect_paths(c, snapshot=snapshot_catalog)
        else:
            # Initialize nesting depth if not already provided.
            dataset_nesting_depth = (
                self._dataset_nesting_depth() if dataset_nesting_depth is None else dataset_nesting_depth
            )
            if dataset_nesting_depth:
                nested_paths = self._collect_paths(dataset_nesting_depth=dataset_nesting_depth - 1)
        if nested_paths:
            paths |= {
                tuple([dataset_table]),
                (dataset_table, dataset_dataset),
            }
        paths |= {(self._dataset_table, dataset_dataset) + p for p in nested_paths}
        return paths

    def _dataset_nesting_depth(self, dataset_rid: RID | None = None) -> int:
        """Determine the maximum dataset nesting depth in the current catalog.

        Returns:

        """

        def children_depth(dataset_rid: RID, nested_datasets: dict[str, list[str]]) -> int:
            """Return the number of nested datasets for the dataset_rid if provided, otherwise in the current catalog"""
            try:
                children = nested_datasets[dataset_rid]
                return max(map(lambda x: children_depth(x, nested_datasets), children)) + 1 if children else 1
            except KeyError:
                return 0

        # Build up the dataset_table nesting graph...
        pb = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables["Dataset_Dataset"]
        dataset_children = (
            [
                {
                    "Dataset": dataset_rid,
                    "Nested_Dataset": c,
                }  # Make uniform with return from datapath
                for c in self.list_dataset_children(dataset_rid=dataset_rid)
            ]
            if dataset_rid
            else pb.entities().fetch()
        )
        nested_dataset = defaultdict(list)
        for ds in dataset_children:
            nested_dataset[ds["Dataset"]].append(ds["Nested_Dataset"])
        return max(map(lambda d: children_depth(d, dict(nested_dataset)), nested_dataset)) if nested_dataset else 0

    def _dataset_specification(
        self,
        writer: Callable[[str, str, Table], list[dict[str, Any]]],
        dataset: DatasetSpec | None = None,
        snapshot_catalog: DerivaML | None = None,
    ) -> list[dict[str, Any]]:
        """Output a download/export specification for a dataset_table.  Each element of the dataset_table
        will be placed in its own directory.
        The top level data directory of the resulting BDBag will have one subdirectory for element type.
        The subdirectory will contain the CSV indicating which elements of that type are present in the
        dataset_table, and then there will be a subdirectory for each object that is reachable from the
        dataset_table members.

        To simplify reconstructing the relationship between tables, the CVS for each element is included.
        The top level data directory will also contain a subdirectory for any controlled vocabularies used in
        the dataset_table. All assets will be placed into a directory named asset in a subdirectory with the
        asset table name.

        For example, consider a dataset_table that consists of two element types, T1 and T2. T1 has foreign
        key relationships to objects in tables T3 and T4. There are also two controlled vocabularies, CV1 and
        CV2. T2 is an asset table which has two assets in it. The layout of the resulting bdbag would be:
              data
                CV1/
                    cv1.csv
                CV2/
                    cv2.csv
                Dataset/
                    T1/
                        t1.csv
                        T3/
                            t3.csv
                        T4/
                            t4.csv
                    T2/
                        t2.csv
                asset/
                  T2
                    f1
                    f2

        Args:
          writer: Callable[[list[Table]]: list[dict[str:  Any]]]:

        Returns:
            A dataset_table specification.
        """
        element_spec = self._export_vocabulary(writer)
        for path in self._table_paths(dataset=dataset, snapshot_catalog=snapshot_catalog):
            element_spec.extend(writer(*path))
        return element_spec

    def _download_dataset_bag(
        self,
        dataset: DatasetSpec,
        execution_rid: RID | None = None,
        snapshot_catalog: DerivaML | None = None,
    ) -> DatasetBag:
        """Download a dataset onto the local file system.  Create a MINID for the dataset if one doesn't already exist.

        Args:
            dataset: Specification of the dataset to be downloaded.
            execution_rid: Execution RID for the dataset.
            snapshot_catalog: Snapshot catalog for the dataset version if specified.

        Returns:
            Tuple consisting of the path to the dataset, the RID of the dataset that was downloaded and the MINID
            for the dataset.
        """
        if (
            execution_rid
            and execution_rid != DRY_RUN_RID
            and self._model.catalog.resolve_rid(execution_rid).table.name != "Execution"
        ):
            raise DerivaMLException(f"RID {execution_rid} is not an execution")
        minid = self._get_dataset_minid(dataset, snapshot_catalog=snapshot_catalog)

        bag_path = (
            self._materialize_dataset_bag(minid, execution_rid=execution_rid)
            if dataset.materialize
            else self._download_dataset_minid(minid)
        )
        return DatabaseModel(minid, bag_path, self._working_dir).get_dataset()

    def _version_snapshot(self, dataset: DatasetSpec) -> str:
        """Return a catalog with snapshot for the specified dataset version"""
        try:
            version_record = next(
                h for h in self.dataset_history(dataset_rid=dataset.rid) if h.dataset_version == dataset.version
            )
        except StopIteration:
            raise DerivaMLException(f"Dataset version {dataset.version} not found for dataset {dataset.rid}")
        return f"{self._model.catalog.catalog_id}@{version_record.snapshot}"

    def _create_dataset_minid(self, dataset: DatasetSpec, snapshot_catalog: DerivaML | None = None) -> str:
        with TemporaryDirectory() as tmp_dir:
            # Generate a download specification file for the current catalog schema. By default, this spec
            # will generate a minid and place the bag into S3 storage.
            spec_file = Path(tmp_dir) / "download_spec.json"
            with spec_file.open("w", encoding="utf-8") as ds:
                json.dump(self._generate_dataset_download_spec(dataset, snapshot_catalog), ds)
            try:
                self._logger.info(
                    "Downloading dataset %s for catalog: %s@%s"
                    % (
                        "minid" if self._use_minid else "bag",
                        dataset.rid,
                        str(dataset.version),
                    )
                )
                # Generate the bag and put into S3 storage.
                exporter = DerivaExport(
                    host=self._model.catalog.deriva_server.server,
                    config_file=spec_file,
                    output_dir=tmp_dir,
                    defer_download=True,
                    timeout=(10, 610),
                    envars={"RID": dataset.rid},
                )
                minid_page_url = exporter.export()[0]  # Get the MINID launch page

            except (
                DerivaDownloadError,
                DerivaDownloadConfigurationError,
                DerivaDownloadAuthenticationError,
                DerivaDownloadAuthorizationError,
                DerivaDownloadTimeoutError,
            ) as e:
                raise DerivaMLException(format_exception(e))
            # Update version table with MINID.
            if self._use_minid:
                version_path = self._model.catalog.getPathBuilder().schemas[self._ml_schema].tables["Dataset_Version"]
                version_rid = [
                    h for h in self.dataset_history(dataset_rid=dataset.rid) if h.dataset_version == dataset.version
                ][0].version_rid
                version_path.update([{"RID": version_rid, "Minid": minid_page_url}])
        return minid_page_url

    def _get_dataset_minid(
        self,
        dataset: DatasetSpec,
        snapshot_catalog: DerivaML | None = None,
        create: bool = True,
    ) -> DatasetMinid | None:
        """Return a MINID for the specified dataset. If no version is specified, use the latest.

        Args:
            dataset: Specification of the dataset.
            snapshot_catalog: Snapshot catalog for the dataset version if specified.
            create: Create a new MINID if one doesn't already exist.

        Returns:
            New or existing MINID for the dataset.
        """
        rid = dataset.rid

        # Case 1: RID is already a MINID or direct URL
        if rid.startswith("minid"):
            return self._fetch_minid_metadata(f"https://identifiers.org/{rid}", dataset.version)
        if rid.startswith("http"):
            return self._fetch_minid_metadata(rid, dataset.version)

        # Case 2: RID is a dataset RID – validate existence
        if not any(rid == ds["RID"] for ds in self.find_datasets()):
            raise DerivaMLTableTypeError("Dataset", rid)

        # Find dataset version record
        version_str = str(dataset.version)
        history = self.dataset_history(rid)
        try:
            version_record = next(v for v in history if v.dataset_version == version_str)
        except StopIteration:
            raise DerivaMLException(f"Version {version_str} does not exist for RID {rid}")

        # Check or create MINID
        minid_url = version_record.minid
        if not minid_url:
            if not create:
                raise DerivaMLException(f"Minid for dataset {rid} doesn't exist")
            if self._use_minid:
                self._logger.info("Creating new MINID for dataset %s", rid)
            minid_url = self._create_dataset_minid(dataset, snapshot_catalog)

        # Return based on MINID usage
        if self._use_minid:
            return self._fetch_minid_metadata(minid_url, dataset.version)

        return DatasetMinid(
            dataset_version=dataset.version,
            RID=f"{rid}@{version_record.snapshot}",
            location=minid_url,
        )

    def _fetch_minid_metadata(self, url: str, version: DatasetVersion) -> DatasetMinid:
        r = requests.get(url, headers={"accept": "application/json"})
        r.raise_for_status()
        return DatasetMinid(dataset_version=version, **r.json())

    def _download_dataset_minid(self, minid: DatasetMinid) -> Path:
        """Given a RID to a dataset_table, or a MINID to an existing bag, download the bag file, extract it, and
        validate that all the metadata is correct

        Args:
            minid: The RID of a dataset_table or a minid to an existing bag.
        Returns:
            the location of the unpacked and validated dataset_table bag and the RID of the bag and the bag MINID
        """

        # Check to see if we have an existing idempotent materialization of the desired bag. If so, then reuse
        # it.  If not, then we need to extract the contents of the archive into our cache directory.
        bag_dir = self._cache_dir / f"{minid.dataset_rid}_{minid.checksum}"
        if bag_dir.exists():
            self._logger.info(f"Using cached bag for  {minid.dataset_rid} Version:{minid.dataset_version}")
            return Path(bag_dir / f"Dataset_{minid.dataset_rid}")

        # Either bag hasn't been downloaded yet, or we are not using a Minid, so we don't know the checksum yet.
        with TemporaryDirectory() as tmp_dir:
            if self._use_minid:
                # Get bag from S3
                archive_path = fetch_single_file(minid.bag_url)
            else:
                exporter = DerivaExport(host=self._model.catalog.deriva_server.server, output_dir=tmp_dir)
                archive_path = exporter.retrieve_file(minid.bag_url)
                hashes = hash_utils.compute_file_hashes(archive_path, hashes=["md5", "sha256"])
                checksum = hashes["sha256"][0]
                bag_dir = self._cache_dir / f"{minid.dataset_rid}_{checksum}"
                if bag_dir.exists():
                    self._logger.info(f"Using cached bag for  {minid.dataset_rid} Version:{minid.dataset_version}")
                    return Path(bag_dir / f"Dataset_{minid.dataset_rid}")
            bag_path = bdb.extract_bag(archive_path, bag_dir.as_posix())
        bdb.validate_bag_structure(bag_path)
        return Path(bag_path)

    def _materialize_dataset_bag(
        self,
        minid: DatasetMinid,
        execution_rid: RID | None = None,
    ) -> Path:
        """Materialize a dataset_table bag into a local directory

        Args:
            minid: A MINID to an existing bag or a RID of the dataset_table that should be downloaded.

        Returns:
            A tuple containing the path to the bag, the RID of the bag, and the MINID to the bag.
        """

        def update_status(status: Status, msg: str) -> None:
            """Update the current status for this execution in the catalog"""
            if execution_rid and execution_rid != DRY_RUN_RID:
                self._model.catalog.getPathBuilder().schemas[self._ml_schema].Execution.update(
                    [
                        {
                            "RID": execution_rid,
                            "Status": status.value,
                            "Status_Detail": msg,
                        }
                    ]
                )
            self._logger.info(msg)

        def fetch_progress_callback(current, total):
            msg = f"Materializing bag: {current} of {total} file(s) downloaded."
            if execution_rid:
                update_status(Status.running, msg)
            return True

        def validation_progress_callback(current, total):
            msg = f"Validating bag: {current} of {total} file(s) validated."
            if execution_rid:
                update_status(Status.running, msg)
            return True

        # request metadata
        bag_path = self._download_dataset_minid(minid)
        bag_dir = bag_path.parent
        validated_check = bag_dir / "validated_check.txt"

        # If this bag has already been validated, our work is done.  Otherwise, materialize the bag.
        if not validated_check.exists():
            self._logger.info(f"Materializing bag {minid.dataset_rid} Version:{minid.dataset_version}")
            bdb.materialize(
                bag_path.as_posix(),
                fetch_callback=fetch_progress_callback,
                validation_callback=validation_progress_callback,
            )
            validated_check.touch()
        return Path(bag_path)

    def _export_annotation(
        self,
        snapshot_catalog: DerivaML | None = None,
    ) -> list[dict[str, Any]]:
        """Return and output specification for the datasets in the provided model

        Returns:
          An export specification suitable for Chaise.
        """

        # Export specification is a specification for the datasets, plus any controlled vocabulary
        return [
            {
                "source": {"api": False, "skip_root_path": True},
                "destination": {"type": "env", "params": {"query_keys": ["snaptime"]}},
            },
            {
                "source": {"api": "entity"},
                "destination": {
                    "type": "env",
                    "params": {"query_keys": ["RID", "Description"]},
                },
            },
            {
                "source": {"api": "schema", "skip_root_path": True},
                "destination": {"type": "json", "name": "schema"},
            },
        ] + self._dataset_specification(
            self._export_annotation_dataset_element,
            None,
            snapshot_catalog=snapshot_catalog,
        )

    def _export_specification(
        self, dataset: DatasetSpec, snapshot_catalog: DerivaML | None = None
    ) -> list[dict[str, Any]]:
        """
        Generate a specification for export engine for specific dataset.

        Returns:
          a download specification for the datasets in the provided model.

        """

        # Download spec is the spec for any controlled vocabulary and for the dataset_table.
        return [
            {
                "processor": "json",
                "processor_params": {"query_path": "/schema", "output_path": "schema"},
            }
        ] + self._dataset_specification(self._export_specification_dataset_element, dataset, snapshot_catalog)

    @staticmethod
    def _export_specification_dataset_element(spath: str, dpath: str, table: Table) -> list[dict[str, Any]]:
        """Return the download specification for the data object indicated by a path through the data model.

        Args:
          spath: Source path
          dpath: Destination path
          table: Table referenced to by the path

        Returns:
          The download specification that will retrieve that data from the catalog and place it into a BDBag.
        """
        exports = [
            {
                "processor": "csv",
                "processor_params": {
                    "query_path": f"/entity/{spath}",
                    "output_path": dpath,
                },
            }
        ]

        # If this table is an asset table, then we need to output the files associated with the asset.
        asset_columns = {"Filename", "URL", "Length", "MD5", "Description"}
        if asset_columns.issubset({c.name for c in table.columns}):
            exports.append(
                {
                    "processor": "fetch",
                    "processor_params": {
                        "query_path": f"/attribute/{spath}/!(URL::null::)/url:=URL,length:=Length,filename:=Filename,md5:=MD5,asset_rid:=RID",
                        "output_path": "asset/{asset_rid}/" + table.name,
                    },
                }
            )
        return exports

    def _export_annotation_dataset_element(self, spath: str, dpath: str, table: Table) -> list[dict[str, Any]]:
        """Given a path in the data model, output an export specification for the path taken to get to the
        current table.

        Args:
          spath: Source path
          dpath: Destination path
          table: Table referenced to by the path

        Returns:
          The export specification that will retrieve that data from the catalog and place it into a BDBag.
        """
        # The table is the last element of the path.  Generate the ERMRest query by converting the list of tables
        # into a path in the form of /S:T1/S:T2/S:Table
        # Generate the destination path in the file system using just the table names.

        skip_root_path = False
        if spath.startswith(f"{self._ml_schema}:Dataset/"):
            # Chaise will add table name and RID filter, so strip it off.
            spath = "/".join(spath.split("/")[2:])
            if spath == "":
                # This path is to just the dataset table.
                return []
        else:
            # A vocabulary table, so we don't want the root_path.
            skip_root_path = True
        exports = [
            {
                "source": {
                    "api": "entity",
                    "path": spath,
                    "skip_root_path": skip_root_path,
                },
                "destination": {"name": dpath, "type": "csv"},
            }
        ]

        # If this table is an asset table, then we need to output the files associated with the asset.
        asset_columns = {"Filename", "URL", "Length", "MD5", "Description"}
        if asset_columns.issubset({c.name for c in table.columns}):
            exports.append(
                {
                    "source": {
                        "skip_root_path": False,
                        "api": "attribute",
                        "path": f"{spath}/!(URL::null::)/url:=URL,length:=Length,filename:=Filename,md5:=MD5, asset_rid:=RID",
                    },
                    "destination": {"name": "asset/{asset_rid}/" + table.name, "type": "fetch"},
                }
            )
        return exports

    def _generate_dataset_download_spec(
        self, dataset: DatasetSpec, snapshot_catalog: DerivaML | None = None
    ) -> dict[str, Any]:
        """
        Generate a specification for downloading a specific dataset.

        This routine creates a download specification that can be used by the Deriva export processor to download
        a specific dataset as a MINID.
        Returns:
        """
        s3_target = "s3://eye-ai-shared"
        minid_test = False

        catalog_id = self._version_snapshot(dataset)
        post_processors = (
            {
                "post_processors": [
                    {
                        "processor": "cloud_upload",
                        "processor_params": {
                            "acl": "public-read",
                            "target_url": s3_target,
                        },
                    },
                    {
                        "processor": "identifier",
                        "processor_params": {
                            "test": minid_test,
                            "env_column_map": {
                                "RID": "{RID}@{snaptime}",
                                "Description": "{Description}",
                            },
                        },
                    },
                ]
            }
            if self._use_minid
            else {}
        )
        return post_processors | {
            "env": {"RID": "{RID}"},
            "bag": {
                "bag_name": "Dataset_{RID}",
                "bag_algorithms": ["md5"],
                "bag_archiver": "zip",
                "bag_metadata": {},
                "bag_idempotent": True,
            },
            "catalog": {
                "host": f"{self._model.catalog.deriva_server.scheme}://{self._model.catalog.deriva_server.server}",
                "catalog_id": catalog_id,
                "query_processors": [
                    {
                        "processor": "env",
                        "processor_params": {
                            "output_path": "Dataset",
                            "query_keys": ["snaptime"],
                            "query_path": "/",
                        },
                    },
                    {
                        "processor": "env",
                        "processor_params": {
                            "query_path": "/entity/M:=deriva-ml:Dataset/RID={RID}",
                            "output_path": "Dataset",
                            "query_keys": ["RID", "Description"],
                        },
                    },
                ]
                + self._export_specification(dataset, snapshot_catalog),
            },
        }

    def _generate_dataset_download_annotations(self) -> dict[str, Any]:
        post_processors = (
            {
                "type": "BAG",
                "outputs": [{"fragment_key": "dataset_export_outputs"}],
                "displayname": "BDBag to Cloud",
                "bag_idempotent": True,
                "postprocessors": [
                    {
                        "processor": "cloud_upload",
                        "processor_params": {
                            "acl": "public-read",
                            "target_url": "s3://eye-ai-shared/",
                        },
                    },
                    {
                        "processor": "identifier",
                        "processor_params": {
                            "test": False,
                            "env_column_map": {
                                "RID": "{RID}@{snaptime}",
                                "Description": "{Description}",
                            },
                        },
                    },
                ],
            }
            if self._use_minid
            else {}
        )
        return {
            deriva_tags.export_fragment_definitions: {"dataset_export_outputs": self._export_annotation()},
            deriva_tags.visible_foreign_keys: self._dataset_visible_fkeys(),
            deriva_tags.export_2019: {
                "detailed": {
                    "templates": [
                        {
                            "type": "BAG",
                            "outputs": [{"fragment_key": "dataset_export_outputs"}],
                            "displayname": "BDBag Download",
                            "bag_idempotent": True,
                        }
                        | post_processors
                    ]
                }
            },
        }

    def _dataset_visible_fkeys(self) -> dict[str, Any]:
        def fkey_name(fk):
            return [fk.name[0].name, fk.name[1]]

        dataset_table = self._model.schemas["deriva-ml"].tables["Dataset"]

        source_list = [
            {
                "source": [
                    {"inbound": ["deriva-ml", "Dataset_Version_Dataset_fkey"]},
                    "RID",
                ],
                "markdown_name": "Previous Versions",
                "entity": True,
            },
            {
                "source": [
                    {"inbound": ["deriva-ml", "Dataset_Dataset_Nested_Dataset_fkey"]},
                    {"outbound": ["deriva-ml", "Dataset_Dataset_Dataset_fkey"]},
                    "RID",
                ],
                "markdown_name": "Parent Datasets",
            },
            {
                "source": [
                    {"inbound": ["deriva-ml", "Dataset_Dataset_Dataset_fkey"]},
                    {"outbound": ["deriva-ml", "Dataset_Dataset_Nested_Dataset_fkey"]},
                    "RID",
                ],
                "markdown_name": "Child Datasets",
            },
        ]
        source_list.extend(
            [
                {
                    "source": [
                        {"inbound": fkey_name(fkey.self_fkey)},
                        {"outbound": fkey_name(other_fkey := fkey.other_fkeys.pop())},
                        "RID",
                    ],
                    "markdown_name": other_fkey.pk_table.name,
                }
                for fkey in dataset_table.find_associations(max_arity=3, pure=False)
            ]
        )
        return {"detailed": source_list}
