"""Base connector interfaces for data sources."""

from abc import ABC, abstractmethod
from typing import List, Any
from vecta.core.schemas import ChunkData, VectorDBSchema


class BaseDataSourceConnector(ABC):
    """Abstract base interface for all data source connectors."""

    @abstractmethod
    def get_all_chunks(self) -> List[ChunkData]:
        """
        Retrieve all chunks from the data source.

        Returns:
            List of ChunkData objects containing id, content, and metadata.
        """
        pass

    @abstractmethod
    def semantic_search(self, query_str: str, k: int = 10) -> List[ChunkData]:
        """
        Perform similarity search to find top-k most similar chunks.

        Args:
            query_str: The text query to search with
            k: Number of top similar chunks to return

        Returns:
            List of ChunkData objects ranked by similarity
        """
        pass

    @abstractmethod
    def get_chunk_by_id(self, chunk_id: str) -> ChunkData:
        """
        Retrieve a specific chunk by its ID.

        Args:
            chunk_id: The unique identifier for the chunk

        Returns:
            ChunkData object for the specified chunk
        """
        pass


class BaseVectorDBConnector(BaseDataSourceConnector):
    """Abstract base class for vector database connectors that require schema configuration."""

    def __init__(self, schema: VectorDBSchema):
        """
        Initialize the connector with database schema configuration.

        Args:
            schema: Schema defining how to extract data from this database (REQUIRED)
        """
        if schema is None:
            raise ValueError("Schema is required for vector database connectors")
        self.schema = schema

    def _create_chunk_data_from_raw(self, raw_result: Any) -> ChunkData:
        """
        Helper method to create ChunkData from raw database result using schema.

        Args:
            raw_result: Raw result from database query

        Returns:
            ChunkData object with extracted information
        """
        return ChunkData.from_schema_extraction(self.schema, raw_result)


class BaseFileStoreConnector(BaseDataSourceConnector):
    """Abstract base class for file store connectors that ingest documents directly."""

    def __init__(self):
        """Initialize the file store connector."""
        pass

    def semantic_search(self, query_str: str, k: int = 10) -> List[ChunkData]:
        """
        File store connectors don't support semantic search directly.

        Data must be loaded into a vector database for searching.

        Args:
            query_str: The text query to search with
            k: Number of top similar chunks to return

        Raises:
            NotImplementedError: File stores don't support direct search
        """
        raise NotImplementedError(
            "File store connectors don't support semantic search directly. "
            "Data must be loaded into a vector database first."
        )
