from __future__ import annotations

import logging
import math

import numpy as np
import faiss


logger = logging.getLogger(__name__)


class ApproximateNearestNeighborSearch:
    """
    A wrapper around the FAISS library for approximate nearest neighbor search over passage embeddings.
    """

    def __init__(self, metric: str = "l2", gpu_id: int = -1):
        self.metric = metric
        self.gpu_id = gpu_id

        self.anns_index: faiss.Index | None = None
        self.passage_metadatas: list[dict] | None = None

    def make_index(
        self,
        passage_vectors: np.ndarray,
        passage_metadatas: list[dict] | None = None,
    ):
        """
        Build an ANN index from passage vectors.
        """
        dim = passage_vectors.shape[1]

        # Choose index type based on metric
        if self.metric == "inner-product":
            # c.f., https://github.com/facebookresearch/contriever/blob/main/src/index.py
            self.anns_index = faiss.IndexFlatIP(dim)
        elif self.metric == "hnsw-inner-product":
            store_n = 128 # neighbors to store per node
            ef_search = 128 # search depth
            # ef_construction = 200 # construction time search depth
            self.anns_index = faiss.IndexHNSWFlat(
                dim, store_n, faiss.METRIC_INNER_PRODUCT
            )
            self.anns_index.hnsw.efSearch = ef_search
            # self.anns_index.hnsw.efConstruction = ef_construction
        else:
            self.anns_index = faiss.IndexFlatL2(dim)

        # Convert to GPU index if needed
        if self.gpu_id >= 0:
            logger.info(f"Converting CPU index to GPU index (GPU ID: {self.gpu_id}) ...")
            res = faiss.StandardGpuResources()
            co = faiss.GpuClonerOptions()
            co.useFloat16 = True
            self.anns_index = faiss.index_cpu_to_gpu(
                res, self.gpu_id, self.anns_index, co
            )
        else:
            logger.info("Using CPU index mode")

        # Add vectors to the index in batches (to avoid memory issues)
        # self.anns_index.add(passage_vectors)
        INDEXING_BATCH_SIZE = 1000000
        n_iterations = math.ceil(len(passage_vectors) / INDEXING_BATCH_SIZE)
        it = 1
        for i in range(0, len(passage_vectors), INDEXING_BATCH_SIZE):
            logger.info(f"Iteration [{it}/{n_iterations}]: Indexing {i}-{min(i+INDEXING_BATCH_SIZE, len(passage_vectors))-1} passage embeddings")
            self.anns_index.add(passage_vectors[i:i+INDEXING_BATCH_SIZE])
            it += 1

        # Save ID and metadata mappings
        self.passage_metadatas = passage_metadatas

    def search(
        self,
        query_vectors: np.ndarray,
        top_k: int = 1,
        batch_size: int = 1024
    ) -> tuple[
        list[list[int]],
        list[list[dict]] | None,
        list[list[float]]
    ]:
        """
        Perform ANN search for the given queries with batching.
        """

        # # (query_size, top_k), (query_size, top_k)
        # batch_scores, batch_indices = self.anns_index.search(query_vectors, top_k)

        # if self.metric not in {"inner-product", "hnsw-inner-product"}:
        #     batch_scores = 1.0 / (batch_scores + 1.0)

        # # Convert numpy results to Python lists
        # batch_indices = batch_indices.tolist()
        # batch_scores = batch_scores.tolist()

        # # Map indices to metadata if available
        # batch_metadatas = (
        #     [[self.passage_metadatas[i] for i in indices] for indices in batch_indices]
        #     if self.passage_metadatas is not None else None
        # )

        # # return batch_indices, batch_ids, batch_metadatas, batch_scores
        # return batch_indices, batch_metadatas, batch_scores

        n_queries = len(query_vectors)
        all_indices = []
        all_metadatas = [] if self.passage_metadatas is not None else None
        all_scores = []

        for begin_i in range(0, n_queries, batch_size):
            end_i = min(begin_i + batch_size, n_queries)
            batch_vectors = query_vectors[begin_i: end_i]

            # (batch_size, top_k), (batch_size, top_k)
            batch_scores, batch_indices = self.anns_index.search(batch_vectors, top_k)

            if self.metric not in {"inner-product", "hnsw-inner-product"}:
                batch_scores = 1.0 / (batch_scores + 1.0)

            # Convert numpy results to Python lists
            batch_indices = batch_indices.tolist()
            batch_scores = batch_scores.tolist()

            all_indices.extend(batch_indices)
            all_scores.extend(batch_scores)

            # Map indices to metadata if available
            if self.passage_metadatas is not None:
                batch_metadatas = [
                    [self.passage_metadatas[i] for i in indices]
                    for indices in batch_indices
                ]
                all_metadatas.extend(batch_metadatas)

        return all_indices, all_metadatas, all_scores

    def save(self, path: str) -> None:
        """
        Save the ANN index to a file.
        """
        faiss.write_index(self.anns_index, path)

    def load(self, path: str) -> None:
        """
        Load a FAISS index from a file.
        """
        self.anns_index = faiss.read_index(path)