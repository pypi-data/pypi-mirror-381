# vecta_sdk/vecta/api_client.py
"""API client for the Vecta RAG benchmarking platform."""

import os
import requests
from typing import List, Optional, Dict, Any, Union, Callable, Tuple
from urllib.parse import urljoin

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
    VectaInactiveBenchmarkError,
    VectaUsageLimitError,
)
from vecta.core.schemas import (
    ChunkData,
    BenchmarkEntry,
    VectorDBType,
    FileStoreType,
    DataSourceType,
    EvaluationType,
    BenchmarkResults,
    RetrievalAndGenerationResults,
    GenerationOnlyResults,
    RenameRequest,
    VectorDBSchema,
)
from vecta.connectors.base import BaseDataSourceConnector
from vecta.core.benchmark import VectaClient


class VectaAPIClient:
    """
    API client that orchestrates between local Vecta SDK evaluation and remote server operations.

    The server handles AI operations (benchmark generation, evaluation scoring).
    The client handles local RAG pipeline evaluation using the Vecta SDK.
    """

    def __init__(
        self,
        api_key: Optional[str] = os.getenv("VECTA_API_KEY"),
        base_url: str = os.getenv("VECTA_API_BASE_URL", "https://vecta.up.railway.app"),
        timeout: int = 600,
    ):
        """
        Initialize the Vecta API client.

        Args:
            api_key: Your Vecta API key
            base_url: Base URL for the Vecta API
            timeout: Request timeout in seconds
        """
        if not api_key:
            raise ValueError(
                "API key is required. Set VECTA_API_KEY environment variable."
            )

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "vecta-sdk/0.1.0",
            }
        )

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Any:
        """Make an HTTP request to the API."""
        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))

        kwargs.setdefault("timeout", self.timeout)
        if params:
            kwargs["params"] = params
        if json_data:
            kwargs["json"] = json_data

        try:
            response = self.session.request(method, url, **kwargs)

            if response.status_code in [200, 201]:
                return response.json() if response.content else {}
            elif response.status_code == 401:
                raise VectaAuthenticationError("Invalid API key")
            elif response.status_code == 403:
                raise VectaForbiddenError("Access forbidden - check your plan limits")
            elif response.status_code == 404:
                raise VectaNotFoundError("Resource not found")
            elif response.status_code == 400:
                error_data = response.json() if response.content else {}
                error_msg = error_data.get("error", "Bad request")
                if "message" in error_data:
                    error_msg += f": {error_data['message']}"

                if "not enough chunks" in error_msg.lower():
                    raise VectaInsufficientDataError(error_msg)
                elif "benchmark not found" in error_msg.lower():
                    raise VectaNoBenchmarkError(error_msg)
                elif "benchmark is not active" in error_msg.lower():
                    raise VectaInactiveBenchmarkError(error_msg)
                else:
                    raise VectaBadRequestError(error_msg)
            elif response.status_code == 429:
                error_data = response.json() if response.content else {}
                if isinstance(error_data, dict):
                    error_name = str(error_data.get("error", "")).lower()
                    message = error_data.get("message")
                    if error_name == "token usage limit exceeded":
                        raise VectaUsageLimitError(
                            message=message
                            or "Token usage limit exceeded. Please upgrade your plan or wait for the next billing cycle.",
                            current_usage=error_data.get("current_usage", 0),
                            limit=error_data.get("limit", 0),
                            plan=error_data.get("plan", "unknown"),
                        )
                    elif message:
                        raise VectaRateLimitError(f"Rate limit exceeded: {message}")
                raise VectaRateLimitError("Rate limit exceeded")
            elif response.status_code >= 500:
                raise VectaServerError("Server error occurred")
            else:
                raise VectaAPIError(
                    f"Request failed with status {response.status_code}"
                )

        except requests.exceptions.Timeout:
            raise VectaAPIError(f"Request timed out after {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise VectaAPIError("Failed to connect to Vecta API")
        except requests.exceptions.RequestException as e:
            raise VectaAPIError(f"Request failed: {e}")

    # Data Source Management
    def connect_local_database(
        self,
        data_source_connector: BaseDataSourceConnector,
        db_type: VectorDBType,
        collection_name: str,
        name: Optional[str] = None,
        schema: Optional[VectorDBSchema] = None,
    ) -> Dict[str, Any]:
        """Connect a local vector database and upload its chunks."""
        config = {
            "collection_name": collection_name,
            "host": "__LOCAL__",
        }

        data_source_config = {
            "source_type": "chroma_local",
            "db_type": db_type.value,
            "connection_config": config,
            "schema": schema.model_dump() if schema else None,
        }

        data_source = self._make_request(
            "POST", "/data-sources", json_data=data_source_config
        )

        # Upload chunks
        print("Uploading chunks to server...")
        chunks = data_source_connector.get_all_chunks()
        print(f"Found {len(chunks)} chunks to upload")

        if chunks:
            self._upload_chunks_in_batches(data_source["id"], chunks)
            data_source = self._make_request(
                "POST", f'/data-sources/{data_source["id"]}/sync'
            )

        return data_source

    def connect_chroma_cloud(
        self,
        tenant: str,
        database_name: str,
        api_key: str,
        collection_name: str,
        schema: Optional[VectorDBSchema] = None,
    ) -> Dict[str, Any]:
        """Connect to Chroma Cloud vector database."""
        config = {
            "tenant": tenant,
            "database": database_name,
            "api_key": api_key,
            "collection_name": collection_name,
        }

        data_source_config = {
            "source_type": DataSourceType.CHROMA_CLOUD.value,
            "db_type": VectorDBType.CHROMA_CLOUD.value,
            "connection_config": config,
            "schema": schema.model_dump() if schema else None,
        }

        print("Connecting Chroma Cloud database...")
        data_source = self._make_request(
            "POST", "/data-sources", json_data=data_source_config
        )
        print(f"Successfully connected! Data source ID: {data_source['id']}")
        return data_source

    def connect_pinecone(
        self,
        api_key: str,
        index_name: str,
        namespace: str = "",
        schema: Optional[VectorDBSchema] = None,
    ) -> Dict[str, Any]:
        """Connect to Pinecone vector database."""
        config = {
            "api_key": api_key,
            "index_name": index_name,
            "namespace": namespace,
            "collection_name": index_name,
        }

        data_source_config = {
            "source_type": DataSourceType.PINECONE.value,
            "db_type": VectorDBType.PINECONE.value,
            "connection_config": config,
            "schema": schema.model_dump() if schema else None,
        }

        print("Connecting Pinecone database...")
        data_source = self._make_request(
            "POST", "/data-sources", json_data=data_source_config
        )
        print(f"Successfully connected! Data source ID: {data_source['id']}")
        return data_source

    def upload_local_files(
        self,
        file_paths: List[str],
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Upload local files to create a file store data source.

        Args:
            file_paths: List of local file paths to upload
            name: Optional name for the data source

        Returns:
            Data source information
        """
        # Upload files to server
        files = []
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise ValueError(f"File not found: {file_path}")

            with open(file_path, "rb") as f:
                files.append(
                    (
                        "files",
                        (os.path.basename(file_path), f, "application/octet-stream"),
                    )
                )

        # Create multipart request
        response = requests.post(
            f"{self.base_url}/data-sources/upload-files",
            files=files,
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=self.timeout,
        )

        if response.status_code != 201:
            raise VectaAPIError(f"Failed to upload files: {response.text}")

        return response.json()

    def _upload_chunks_in_batches(
        self, data_source_id: str, chunks: List[ChunkData], batch_size: int = 100
    ):
        """Upload chunks to server in batches."""
        total_batches = (len(chunks) + batch_size - 1) // batch_size

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size]
            batch_num = i // batch_size + 1

            print(f"Uploading batch {batch_num}/{total_batches} ({len(batch)} chunks)")

            chunk_data = [
                {"id": chunk.id, "content": chunk.content, "metadata": chunk.metadata}
                for chunk in batch
            ]

            self._make_request(
                "POST",
                f"/data-sources/{data_source_id}/chunks",
                json_data={"chunks": chunk_data},
            )

    def list_data_sources(self) -> List[Dict[str, Any]]:
        """List all data sources."""
        return self._make_request("GET", "/data-sources")

    def get_data_source(self, data_source_id: str) -> Dict[str, Any]:
        """Get data source details."""
        return self._make_request("GET", f"/data-sources/{data_source_id}")

    def sync_data_source(self, data_source_id: str) -> Dict[str, Any]:
        """Sync data source metadata."""
        return self._make_request("POST", f"/data-sources/{data_source_id}/sync")

    def rename_data_source(
        self, data_source_id: str, data: RenameRequest
    ) -> Dict[str, Any]:
        """Rename a data source."""
        return self._make_request(
            "PATCH", f"/data-sources/{data_source_id}", json_data=data.model_dump()
        )

    def delete_data_source(self, data_source_id: str) -> Dict[str, Any]:
        """Delete a data source."""
        return self._make_request("DELETE", f"/data-sources/{data_source_id}")

    def delete_chunk(self, data_source_id: str, chunk_id: str) -> Dict[str, Any]:
        """Delete a chunk from a data source."""
        return self._make_request(
            "DELETE", f"/data-sources/{data_source_id}/chunks/{chunk_id}"
        )

    # Benchmark Management
    def create_benchmark(
        self,
        data_source_id: str,
        questions_count: int = 100,
        similarity_threshold: float = 0.7,
        description: Optional[str] = None,
        random_seed: Optional[int] = None,
        wait_for_completion: bool = True,
    ) -> Dict[str, Any]:
        """Create and generate a benchmark on the server using AI."""
        config = {
            "data_source_id": data_source_id,
            "questions_count": questions_count,
            "similarity_threshold": similarity_threshold,
            "description": description,
            "random_seed": random_seed,
        }

        benchmark = self._make_request("POST", "/benchmarks", json_data=config)

        print(f"Generating {questions_count} questions using AI...")
        benchmark = self._make_request(
            "POST", f'/benchmarks/{benchmark["id"]}/generations'
        )

        if wait_for_completion:
            print("Waiting for benchmark generation to complete...")
            benchmark = self._wait_for_benchmark_completion(benchmark["id"])

        return benchmark

    def _wait_for_benchmark_completion(
        self, benchmark_id: str, poll_interval: int = 5, max_wait: int = 1800
    ) -> Dict[str, Any]:
        """Wait for benchmark generation to complete."""
        import time

        start_time = time.time()

        while time.time() - start_time < max_wait:
            benchmark = self._make_request("GET", f"/benchmarks/{benchmark_id}")

            if benchmark["status"] == "active":
                print("Benchmark generation completed!")
                return benchmark
            elif benchmark["status"] == "error":
                raise VectaAPIError("Benchmark generation failed")

            print(f"Status: {benchmark['status']}...")
            time.sleep(poll_interval)

        raise VectaAPIError(f"Benchmark generation timed out after {max_wait} seconds")

    def download_benchmark(self, benchmark_id: str) -> List[BenchmarkEntry]:
        """Download benchmark entries for local evaluation."""
        print("Downloading benchmark entries...")
        data = self._make_request("GET", f"/benchmarks/{benchmark_id}/entries")
        entries = [BenchmarkEntry(**entry) for entry in data]
        print(f"Downloaded {len(entries)} benchmark entries")
        return entries

    def export_benchmark(self, benchmark_id: str) -> str:
        """Export benchmark as CSV."""
        print("Exporting benchmark as CSV...")
        return self._make_request("GET", f"/benchmarks/{benchmark_id}/exports/csv")

    def list_benchmarks(self) -> List[Dict[str, Any]]:
        """List all benchmarks."""
        return self._make_request("GET", "/benchmarks")

    def get_benchmark(self, benchmark_id: str) -> Dict[str, Any]:
        """Get benchmark details."""
        return self._make_request("GET", f"/benchmarks/{benchmark_id}")

    def _ensure_benchmark_active(self, benchmark_id: str) -> Dict[str, Any]:
        """Fetch benchmark and verify it is active before running evaluations."""
        benchmark = self.get_benchmark(benchmark_id)
        raw_status = (benchmark.get("status") or "").strip()

        if raw_status.lower() != "active":
            name = benchmark.get("name") or benchmark_id
            status_display = raw_status or "unknown"
            message = (
                f'Benchmark "{name}" is not active (current status: {status_display}). '
                "Activate the benchmark before running evaluations."
            )
            raise VectaInactiveBenchmarkError(message)

        return benchmark

    def rename_benchmark(
        self, benchmark_id: str, data: RenameRequest
    ) -> Dict[str, Any]:
        """Rename a benchmark."""
        return self._make_request(
            "PATCH", f"/benchmarks/{benchmark_id}", json_data=data.model_dump()
        )

    def delete_benchmark(self, benchmark_id: str) -> Dict[str, Any]:
        """Delete a benchmark."""
        return self._make_request("DELETE", f"/benchmarks/{benchmark_id}")

    # Local Evaluation with Server-side Computation
    def evaluate_retrieval(
        self,
        benchmark_id: str,
        retrieval_function: Callable[[str], List[str]],
        evaluation_name: str = "API Evaluation",
    ) -> BenchmarkResults:
        """Evaluate a retrieval function locally and upload results to server."""
        print(f"Starting retrieval evaluation: {evaluation_name}")

        self._ensure_benchmark_active(benchmark_id)

        benchmark_entries = self.download_benchmark(benchmark_id)

        vecta_client = VectaClient(data_source_connector=None)
        vecta_client.benchmark_entries = benchmark_entries

        print("Running local evaluation...")
        results = vecta_client.evaluate_retrieval(retrieval_function, evaluation_name)

        print(f"Evaluation completed in {results.duration_seconds} seconds")

        self._upload_evaluation_results(
            benchmark_id=benchmark_id,
            evaluation_type=EvaluationType.RETRIEVAL_ONLY,
            evaluation_name=evaluation_name,
            results=results,
        )

        return results

    def evaluate_retrieval_and_generation(
        self,
        benchmark_id: str,
        retrieval_generation_function: Callable[[str], Tuple[List[str], str]],
        evaluation_name: str = "API RAG Evaluation",
    ) -> RetrievalAndGenerationResults:
        """Evaluate a retrieval + generation function using server-side evaluation."""
        print(f"Starting retrieval + generation evaluation: {evaluation_name}")

        self._ensure_benchmark_active(benchmark_id)

        benchmark_entries = self.download_benchmark(benchmark_id)

        vecta_client = VectaClient(data_source_connector=None)
        vecta_client.benchmark_entries = benchmark_entries

        print("Running retrieval and generation locally...")
        results = vecta_client.evaluate_retrieval_and_generation(
            retrieval_generation_function, evaluation_name
        )

        print(f"Evaluation completed in {results.duration_seconds} seconds")

        self._upload_evaluation_results(
            benchmark_id=benchmark_id,
            evaluation_type=EvaluationType.RETRIEVAL_AND_GENERATION,
            evaluation_name=evaluation_name,
            results=results,
        )

        return results

    def evaluate_generation_only(
        self,
        benchmark_id: str,
        generation_function: Callable[[str], str],
        evaluation_name: str = "API Generation Evaluation",
    ) -> GenerationOnlyResults:
        """Evaluate a generation function using server-side evaluation."""
        print(f"Starting generation evaluation: {evaluation_name}")

        self._ensure_benchmark_active(benchmark_id)

        benchmark_entries = self.download_benchmark(benchmark_id)

        vecta_client = VectaClient(data_source_connector=None)
        vecta_client.benchmark_entries = benchmark_entries

        print("Running generation locally...")
        results = vecta_client.evaluate_generation_only(
            generation_function, evaluation_name
        )

        print(f"Evaluation completed in {results.duration_seconds} seconds")

        self._upload_evaluation_results(
            benchmark_id=benchmark_id,
            evaluation_type=EvaluationType.GENERATION_ONLY,
            evaluation_name=evaluation_name,
            results=results,
        )

        return results

    def _upload_evaluation_results(
        self,
        benchmark_id: str,
        evaluation_type: EvaluationType,
        evaluation_name: str,
        results: Union[
            BenchmarkResults, RetrievalAndGenerationResults, GenerationOnlyResults
        ],
    ):
        """Upload evaluation results to server for storage."""
        print("Uploading evaluation results to server...")

        evaluation_data = {
            "benchmark_id": benchmark_id,
            "evaluation_type": evaluation_type.value,
            "evaluation_name": evaluation_name,
            "results": results.model_dump(),
        }

        self._make_request("POST", "/evaluations", json_data=evaluation_data)
        print("Results uploaded successfully!")

    # Evaluation Management
    def list_evaluations(self) -> List[Dict[str, Any]]:
        """List all evaluations."""
        return self._make_request("GET", "/evaluations")

    def get_evaluation(self, evaluation_id: str) -> Dict[str, Any]:
        """Get evaluation details."""
        return self._make_request("GET", f"/evaluations/{evaluation_id}")

    def export_evaluation(self, evaluation_id: str) -> bytes:
        """Export evaluation as PDF report."""
        return self._make_request("GET", f"/evaluations/{evaluation_id}/exports/pdf")

    def rename_evaluation(
        self, evaluation_id: str, data: RenameRequest
    ) -> Dict[str, Any]:
        """Rename an evaluation."""
        return self._make_request(
            "PATCH", f"/evaluations/{evaluation_id}", json_data=data.model_dump()
        )

    def delete_evaluation(self, evaluation_id: str) -> Dict[str, Any]:
        """Delete an evaluation."""
        return self._make_request("DELETE", f"/evaluations/{evaluation_id}")

    # Server-side evaluation endpoints
    def evaluate_retrieval_and_generation_server(
        self,
        benchmark_id: str,
        evaluation_name: str,
        evaluation_results: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Evaluate retrieval and generation results on the server."""
        self._ensure_benchmark_active(benchmark_id)

        data = {
            "benchmark_id": benchmark_id,
            "evaluation_name": evaluation_name,
            "evaluation_results": evaluation_results,
        }
        return self._make_request(
            "POST", "/evaluations/evaluate-retrieval-and-generation", json_data=data
        )

    def evaluate_generation_only_server(
        self,
        benchmark_id: str,
        evaluation_name: str,
        evaluation_results: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Evaluate generation-only results on the server."""
        self._ensure_benchmark_active(benchmark_id)

        data = {
            "benchmark_id": benchmark_id,
            "evaluation_name": evaluation_name,
            "evaluation_results": evaluation_results,
        }
        return self._make_request(
            "POST", "/evaluations/evaluate-generation-only", json_data=data
        )
