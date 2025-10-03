from typing import Any, Dict, List, Optional

from pyspark.sql import Column

from databricks.ml_features.entities.aggregation import TimeWindow
from databricks.ml_features.entities.data_source import DataSource
from databricks.ml_features.entities.function import Function
from databricks.ml_features_common.entities._feature_store_object import (
    _FeatureStoreObject,
)


class Feature(_FeatureStoreObject):
    """
    Represents a feature definition that combines a data source with aggregation logic.

    :param catalog_name: The catalog name for the feature (required)
    :param schema_name: The schema name for the feature (required)
    :param name: The name of the feature. Leading and trailing whitespace will be stripped.
                 If not provided or empty after stripping, a name will be auto-generated
                 based on the input columns, function, and time window.
    :param source: The data source for this feature
    :param inputs: List of column names from the source to use as input
    :param function: The aggregation function to apply to the input columns
    :param time_window: The time window for the aggregation
    :param description: Optional description of the feature
    """

    INPUTS_FIELD_NAME = "inputs"
    DATA_SOURCE_FIELD_NAME = "data_source"
    FUNCTION_FIELD_NAME = "function"
    TIME_WINDOW_FIELD_NAME = "time_window"

    def __init__(
        self,
        *,
        source: DataSource,
        inputs: List[str],
        function: Function,
        time_window: TimeWindow,
        catalog_name: str,
        schema_name: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """Initialize a Feature object. See class documentation."""
        # Validate and store mandatory catalog and schema names
        if not isinstance(catalog_name, str) or not catalog_name.strip():
            raise ValueError("'catalog_name' must be a non-empty string")
        if not isinstance(schema_name, str) or not schema_name.strip():
            raise ValueError("'schema_name' must be a non-empty string")

        self._catalog_name = catalog_name.strip()
        self._schema_name = schema_name.strip()

        # Strip whitespace from name if provided
        if name is not None and isinstance(name, str):
            name = name.strip()

        self._validate_parameters(name, source, inputs, function, time_window)

        # Handle name construction based on whether name is provided and qualified
        if name:
            if "." in name:
                # If name is already qualified, validate it has the correct prefix and strip it
                expected_prefix = f"{self._catalog_name}.{self._schema_name}."
                if not name.startswith(expected_prefix):
                    raise ValueError(
                        f"Qualified name '{name}' must start with '{expected_prefix}'"
                    )
                # Strip the catalog.schema prefix to get the base name
                self._name = name[len(expected_prefix) :]
            else:
                # If name is unqualified, use it as is
                self._name = name
        else:
            # Generate base name
            self._name = self._generate_name(source, inputs, function, time_window)
        self._source = source
        self._inputs = inputs
        self._function = function
        self._time_window = time_window
        self._description = description

    @property
    def name(self) -> str:
        """The leaf name of the feature."""
        return self._name

    @property
    def full_name(self) -> str:
        """The fully qualified Unity Catalog name of the feature."""
        return f"{self._catalog_name}.{self._schema_name}.{self._name}"

    @property
    def catalog_name(self) -> str:
        """The catalog name of the feature."""
        return self._catalog_name

    @property
    def schema_name(self) -> str:
        """The schema name of the feature."""
        return self._schema_name

    @property
    def source(self) -> DataSource:
        """The data source for this feature."""
        return self._source

    @property
    def inputs(self) -> List[str]:
        """List of column names from the source to use as input."""
        return self._inputs

    @property
    def function(self) -> Function:
        """The aggregation function to apply to the input columns."""
        return self._function

    @property
    def time_window(self) -> TimeWindow:
        """The time window for the aggregation."""
        return self._time_window

    @property
    def description(self) -> Optional[str]:
        """Optional description of the feature."""
        return self._description

    @staticmethod
    def _generate_name(
        source: DataSource,
        inputs: List[str],
        function: Function,
        time_window: TimeWindow,
    ) -> str:
        # ToDo: move this to backend as a part of CreateFeature API
        """Generate a feature name from the provided parameters."""
        return f"{inputs[0]}_{function.name}_{str(time_window)}"

    def computation_function(self) -> Column:
        func = self.function.spark_function(self.inputs)
        if self.time_window:
            func = func.over(
                self.time_window.spark_window(
                    self.source.entity_columns, self.source.order_column
                )
            )
        name = self.full_name
        return func.alias(name)

    def _validate_parameters(
        self,
        name: Optional[str],
        source: DataSource,
        inputs: List[str],
        function: Function,
        time_window: TimeWindow,
    ):
        """Validates the parameters provided to the Feature class."""
        if name is not None and not isinstance(name, str):
            raise ValueError("The 'name' must be a string when provided.")

        # Note: We allow qualified names here since the client validation handles
        # matching catalog/schema names when qualified names are provided

        if not isinstance(source, DataSource):
            raise ValueError("The 'source' must be a DataSource instance.")

        if not isinstance(inputs, list):
            raise ValueError("The 'inputs' must be a list.")

        if not inputs:
            raise ValueError("The 'inputs' must contain at least one column name.")

        for i, column in enumerate(inputs):
            if not isinstance(column, str) or not column.strip():
                raise ValueError(
                    f"All column names in 'inputs' must be non-empty strings. "
                    f"Invalid column at index {i}: {column}"
                )

        if not isinstance(function, Function):
            raise ValueError("The 'function' must be a Function instance.")

        if not isinstance(time_window, TimeWindow):
            raise ValueError("The 'time_window' must be a TimeWindow instance.")

    def _to_yaml_dict(self) -> Dict[str, Any]:
        """Convert the feature to a dictionary that can be used to generate a YAML file."""
        return {
            self.INPUTS_FIELD_NAME: self.inputs,
            self.DATA_SOURCE_FIELD_NAME: self.source.full_name(),
            self.FUNCTION_FIELD_NAME: self.function._to_yaml_dict(),
            self.TIME_WINDOW_FIELD_NAME: self.time_window._to_yaml_dict(),
        }

    @classmethod
    def _from_yaml_dict(
        cls,
        feature_name: str,
        feature_dict: Dict[str, Any],
        data_source: DataSource,
    ) -> "Feature":
        """Create a Feature from a dictionary loaded from YAML."""
        # Parse the function
        function = Function._from_yaml_dict(feature_dict[cls.FUNCTION_FIELD_NAME])

        # Parse the time window
        time_window = TimeWindow._from_yaml_dict(
            feature_dict[cls.TIME_WINDOW_FIELD_NAME]
        )

        # Extract catalog and schema from feature_name if it's qualified
        # For backward compatibility, assume default catalog/schema if not qualified
        if "." in feature_name:
            parts = feature_name.split(".")
            if len(parts) == 3:
                catalog_name, schema_name, base_name = parts
            elif len(parts) == 2:
                # Assume default catalog for 2-level names
                catalog_name = "main"  # Default catalog
                schema_name, base_name = parts
            else:
                raise ValueError(f"Invalid feature name format: {feature_name}")
        else:
            # Unqualified name, use defaults
            catalog_name = "main"  # Default catalog
            schema_name = "default"  # Default schema
            base_name = feature_name

        return cls(
            name=base_name,
            catalog_name=catalog_name,
            schema_name=schema_name,
            source=data_source,
            inputs=feature_dict[cls.INPUTS_FIELD_NAME],
            function=function,
            time_window=time_window,
        )
