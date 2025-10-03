class OfflineStoreConfig:
    """Represents an offline store configuration for managed pipelines to materialize features.
    The pipeline may materialize features into multiple tables updated at separate cadences.
    Each table will have a unique postfix after the table_name_prefix."""

    def __init__(self, *, catalog_name: str, schema_name: str, table_name_prefix: str):
        """
        Initialize an OfflineStoreConfig instance.

        Args:
            catalog_name: The catalog name for the offline table
            schema_name: The schema name for the offline table
            table_name_prefix: The table name prefix for the offline table
        """
        self.catalog_name = catalog_name
        self.schema_name = schema_name
        self.table_name_prefix = table_name_prefix
