# vecta_sdk/vecta/connectors/file_store_connector.py
"""File store connector for ingesting documents from file systems."""

from typing import List, Optional
import os
import uuid

from vecta.connectors.base import BaseFileStoreConnector
from vecta.core.schemas import ChunkData


class FileStoreConnector(BaseFileStoreConnector):
    """
    Connector for file stores that ingests documents using thepipe.

    This connector creates ChunkData objects from files on disk,
    treating each thepipe chunk as a "page" in our system.
    """

    def __init__(
        self,
        file_paths: List[str],
        base_path: str = "/mnt/file_stores",
    ):
        """
        Initialize file store connector.

        Args:
            file_paths: List of file paths to ingest (relative to base_path)
            base_path: Base directory where files are stored
        """
        super().__init__()
        self.file_paths = file_paths
        self.base_path = base_path
        self._chunks_cache: Optional[List[ChunkData]] = None

    def get_all_chunks(self) -> List[ChunkData]:
        """
        Retrieve all chunks by ingesting files with thepipe.

        Returns:
            List of ChunkData objects containing ingested content
        """
        if self._chunks_cache is not None:
            return self._chunks_cache

        try:
            from thepipe.scraper import scrape_file
            from thepipe.chunker import chunk_by_page
        except ImportError:
            raise ImportError(
                "thepipe is required for file store ingestion. "
                "Install with: pip install thepipe-api"
            )

        all_chunks: List[ChunkData] = []

        for file_path in self.file_paths:
            full_path = os.path.join(self.base_path, file_path)

            if not os.path.exists(full_path):
                print(f"Warning: File not found: {full_path}")
                continue

            try:
                # Ingest file using thepipe
                thepipe_chunks = scrape_file(
                    filepath=full_path,
                    chunking_method=chunk_by_page,
                    include_output_images=False,
                )

                # Convert thepipe chunks to ChunkData
                for idx, thepipe_chunk in enumerate(thepipe_chunks):
                    # Generate unique chunk ID
                    chunk_id = f"{file_path}_{idx}_{uuid.uuid4().hex[:8]}"

                    # Extract document name from path
                    doc_name = os.path.basename(thepipe_chunk.path or file_path)

                    # Create metadata
                    metadata = {
                        "source_path": doc_name,
                        "page_nums": [idx],
                        "file_path": file_path,
                        "chunk_index": idx,
                    }

                    # Create ChunkData directly
                    chunk_data = ChunkData(
                        id=chunk_id,
                        content=thepipe_chunk.text or "",
                        metadata=metadata,
                        source_path=doc_name,
                        page_nums=[idx],
                    )

                    all_chunks.append(chunk_data)

            except Exception as e:
                print(f"Error ingesting file {full_path}: {e}")
                continue

        self._chunks_cache = all_chunks
        return all_chunks

    def get_chunk_by_id(self, chunk_id: str) -> ChunkData:
        """
        Retrieve a specific chunk by its ID.

        Args:
            chunk_id: The unique identifier for the chunk

        Returns:
            ChunkData object for the specified chunk
        """
        all_chunks = self.get_all_chunks()

        for chunk in all_chunks:
            if chunk.id == chunk_id:
                return chunk

        raise ValueError(f"Chunk with ID '{chunk_id}' not found")

    def clear_cache(self) -> None:
        """Clear the cached chunks to force re-ingestion."""
        self._chunks_cache = None
