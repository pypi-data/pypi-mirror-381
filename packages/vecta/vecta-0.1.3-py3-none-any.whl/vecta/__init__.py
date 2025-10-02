# vecta_sdk/vecta/__init__.py
"""Vecta: An open source benchmarking package for RAG retrieval systems."""

from vecta.core.benchmark import VectaClient
from vecta.api_client import VectaAPIClient
from vecta.core.dataset_importer import BenchmarkDatasetImporter
from vecta.core.schemas import (
    ChunkData,
    BenchmarkEntry,
    EvaluationMetrics,
    GenerationMetrics,
    BenchmarkResults,
    RetrievalAndGenerationResults,
    GenerationOnlyResults,
    VectorDBType,
    FileStoreType,
    DataSourceType,
    EvaluationType,
    VectorDBSchema,
    SyntheticQuestion,
    ChunkJudgment,
    RenameRequest,
    UsageInfo,
)
from vecta.connectors.chroma_local_connector import ChromaLocalConnector
from vecta.connectors.chroma_cloud_connector import ChromaCloudConnector
from vecta.connectors.pinecone_connector import PineconeConnector
from vecta.connectors.azure_cosmos_connector import AzureCosmosConnector
from vecta.connectors.databricks_connector import DatabricksConnector
from vecta.connectors.langchain_connector import (
    LangChainVectorStoreConnector,
)
from vecta.connectors.llama_index_connector import LlamaIndexConnector
from vecta.connectors.pgvector_connector import PgVectorConnector
from vecta.connectors.weaviate_connector import WeaviateConnector
from vecta.connectors.file_store_connector import FileStoreConnector
from vecta.exceptions import (
    VectaAPIError,
    VectaAuthenticationError,
    VectaNotFoundError,
    VectaBadRequestError,
    VectaServerError,
    VectaForbiddenError,
    VectaRateLimitError,
    VectaInsufficientDataError,
    VectaNoBenchmarkError,
    VectaUsageLimitError,
)

__version__ = "0.1.0"
__all__ = [
    "VectaClient",
    "VectaAPIClient",
    "BenchmarkDatasetImporter",
    "ChunkData",
    "BenchmarkEntry",
    "EvaluationMetrics",
    "GenerationMetrics",
    "BenchmarkResults",
    "RetrievalAndGenerationResults",
    "GenerationOnlyResults",
    "VectorDBType",
    "FileStoreType",
    "DataSourceType",
    "EvaluationType",
    "VectorDBSchema",
    "SyntheticQuestion",
    "ChunkJudgment",
    "RenameRequest",
    "UsageInfo",
    "ChromaLocalConnector",
    "ChromaCloudConnector",
    "PineconeConnector",
    "AzureCosmosConnector",
    "DatabricksConnector",
    "LangChainVectorStoreConnector",
    "LlamaIndexConnector",
    "PgVectorConnector",
    "WeaviateConnector",
    "FileStoreConnector",
    "VectaAPIError",
    "VectaAuthenticationError",
    "VectaNotFoundError",
    "VectaBadRequestError",
    "VectaServerError",
    "VectaForbiddenError",
    "VectaRateLimitError",
    "VectaInsufficientDataError",
    "VectaNoBenchmarkError",
    "VectaUsageLimitError",
]
