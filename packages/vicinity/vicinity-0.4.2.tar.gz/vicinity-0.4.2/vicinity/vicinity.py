"""A small vector store."""

from __future__ import annotations

import logging
from io import open
from pathlib import Path
from time import perf_counter
from typing import Any, Iterable, Sequence, Type, Union

import numpy as np
import orjson
from numpy import typing as npt
from orjson import JSONEncodeError

from vicinity import Metric
from vicinity.backends import AbstractBackend, BasicBackend, BasicVectorStore, get_backend_class
from vicinity.datatypes import Backend, PathLike, SimilarityResult

logger = logging.getLogger(__name__)


class Vicinity:
    """
    Work with vector representations of items.

    Supports functions for calculating fast batched similarity
    between items or composite representations of items.
    """

    def __init__(
        self,
        items: Sequence[Any],
        backend: AbstractBackend,
        metadata: Union[dict[str, Any], None] = None,
        vector_store: BasicVectorStore | None = None,
    ) -> None:
        """
        Initialize a Vicinity instance with an array and list of items.

        :param items: The items in the vector space.
            A list of items. Length must be equal to the number of vectors, and
            aligned with the vectors.
        :param backend: The backend to use for the vector space.
        :param metadata: A dictionary containing metadata about the vector space.
        :param vector_store: A simple vector store only used for storing actual vectors.
        :raises ValueError: If the length of the items and vectors are not the same.
        """
        if len(items) != len(backend):
            raise ValueError(
                "Your vector space and list of items are not the same length: " f"{len(backend)} != {len(items)}"
            )
        self.items: list[Any] = list(items)
        self.backend: AbstractBackend = backend
        self.metadata = metadata or {}
        self.vector_store = vector_store

    def get_vector_by_index(self, index: int | Iterable[int]) -> npt.NDArray:
        """Get a vector by index."""
        if isinstance(index, int):
            index = [index]
        if not all(0 <= i < len(self.items) for i in index):
            raise ValueError("Index out of bounds.")
        if self.vector_store is None:
            raise ValueError(
                "No vector store was provided. To get items by index, create a vicinity index by passing store_vectors=True on index creation."
            )
        return self.vector_store.get_by_index(list(index))

    def __len__(self) -> int:
        """The number of the items in the vector space."""
        return len(self.items)

    @classmethod
    def from_vectors_and_items(
        cls: type[Vicinity],
        vectors: npt.NDArray,
        items: Sequence[Any],
        backend_type: Backend | str = Backend.BASIC,
        store_vectors: bool = False,
        **kwargs: Any,
    ) -> Vicinity:
        """
        Create a Vicinity instance from vectors and items.

        :param vectors: The vectors to use.
        :param items: The items to use.
        :param backend_type: The type of backend to use.
        :param store_vectors: Whether to store the raw vectors in the backend.
        :param **kwargs: Additional arguments to pass to the backend.
        :return: A Vicinity instance.
        """
        backend_type = Backend(backend_type)
        backend_cls = get_backend_class(backend_type)
        arguments = backend_cls.argument_class(**kwargs)
        backend = backend_cls.from_vectors(vectors, **arguments.dict())
        if store_vectors:
            vector_store = BasicVectorStore(vectors=vectors)
        else:
            vector_store = None

        return cls(items, backend, vector_store=vector_store)

    @property
    def dim(self) -> int:
        """The dimensionality of the vectors."""
        return self.backend.dim

    @property
    def metric(self) -> str:
        """The metric used by the backend."""
        return self.backend.arguments.metric

    def query(
        self,
        vectors: npt.NDArray,
        k: int = 10,
    ) -> SimilarityResult:
        """
        Find the nearest neighbors to some arbitrary vector.

        Use this to look up the nearest neighbors to a vector that is not in the vocabulary.

        :param vectors: The vectors to find the nearest neighbors to.
        :param k: The number of most similar items to retrieve.
        :return: For each item in the input, the num most similar items are returned in the form of
            (NAME, DISTANCE) tuples.
        """
        vectors = np.asarray(vectors)
        if np.ndim(vectors) == 1:
            vectors = vectors[None, :]

        out = []
        for index, distances in self.backend.query(vectors, k):
            distances.clip(min=0, out=distances)
            out.append([(self.items[idx], dist) for idx, dist in zip(index, distances)])

        return out

    def query_threshold(
        self,
        vectors: npt.NDArray,
        threshold: float = 0.5,
        max_k: int = 100,
    ) -> SimilarityResult:
        """
        Find the nearest neighbors to some arbitrary vector with some threshold. Note: the output is not sorted.

        :param vectors: The vectors to find the most similar vectors to.
        :param threshold: The threshold to use.
        :param max_k: The maximum number of neighbors to consider for the threshold query.

        :return: For each item in the input, the items above the threshold are returned in the form of
                (NAME, DISTANCE) tuples.
        """
        vectors = np.asarray(vectors)
        if np.ndim(vectors) == 1:
            vectors = vectors[None, :]

        out = []
        for indices, distances in self.backend.threshold(vectors, threshold, max_k=max_k):
            distances.clip(min=0, out=distances)
            out.append([(self.items[idx], dist) for idx, dist in zip(indices, distances)])

        return out

    def save(
        self,
        folder: PathLike,
        overwrite: bool = False,
    ) -> None:
        """
        Save a Vicinity instance in a fast format.

        The Vicinity fast format stores the words and vectors of a Vicinity instance
        separately in a JSON and numpy format, respectively.

        :param folder: The path to which to save the JSON file. The vectors are saved separately. The JSON contains a path to the numpy file.
        :param overwrite: Whether to overwrite the JSON and numpy files if they already exist.
        :raises ValueError: If the path is not a directory.
        :raises JSONEncodeError: If the items are not serializable.
        """
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=overwrite)

        if not path.is_dir():
            raise ValueError(f"Path {path} should be a directory.")

        items_dict = {"items": self.items, "metadata": self.metadata, "backend_type": self.backend.backend_type.value}
        try:
            with open(path / "data.json", "wb") as file_handle:
                file_handle.write(orjson.dumps(items_dict))
        except JSONEncodeError as e:
            raise JSONEncodeError(f"Items could not be encoded to JSON because they are not serializable: {e}")

        self.backend.save(path)
        if self.vector_store is not None:
            store_path = path / "store"
            store_path.mkdir(exist_ok=overwrite)
            self.vector_store.save(store_path)

    @classmethod
    def load(cls, filename: PathLike) -> Vicinity:
        """
        Load a Vicinity instance in fast format.

        As described above, the fast format stores the words and vectors of the
        Vicinity instance separately and is drastically faster than loading from
        .txt files.

        :param filename: The filename to load.
        :return: A Vicinity instance.
        """
        folder_path = Path(filename)

        with open(folder_path / "data.json", "rb") as file_handle:
            data: dict[str, Any] = orjson.loads(file_handle.read())
        items: Sequence[Any] = data["items"]

        metadata: dict[str, Any] = data["metadata"]
        backend_type = Backend(data["backend_type"])

        backend_cls: type[AbstractBackend] = get_backend_class(backend_type)
        backend = backend_cls.load(folder_path)
        if Path(folder_path / "store").exists():
            vector_store = BasicVectorStore.load(folder_path / "store")
        else:
            vector_store = None

        instance = cls(items, backend, metadata=metadata, vector_store=vector_store)

        return instance

    def insert(self, tokens: Sequence[Any], vectors: npt.NDArray) -> None:
        """
        Insert new items into the vector space.

        :param tokens: A list of items to insert into the vector space.
        :param vectors: The vectors to insert into the vector space.
        :raises ValueError: If the tokens and vectors are not the same length.
        """
        if len(tokens) != len(vectors):
            raise ValueError(f"Your tokens and vectors are not the same length: {len(tokens)} != {len(vectors)}")

        if vectors.shape[1] != self.dim:
            raise ValueError("The inserted vectors must have the same dimension as the backend.")

        self.items.extend(tokens)
        self.backend.insert(vectors)
        if self.vector_store is not None:
            self.vector_store.insert(vectors)

    def delete(self, tokens: Sequence[Any]) -> None:
        """
        Delete tokens from the vector space.

        The removal of tokens is done in place. If the tokens are not in the vector space,
        a ValueError is raised.

        :param tokens: A list of tokens to remove from the vector space.
        :raises ValueError: If any passed tokens are not in the vector space.
        """
        tokens_to_find = list(tokens)
        curr_indices = []
        for idx, elem in enumerate(self.items):
            matching_tokens = [t for t in tokens_to_find if t == elem]
            if matching_tokens:
                curr_indices.append(idx)
                for t in matching_tokens:
                    tokens_to_find.remove(t)

        if tokens_to_find:
            raise ValueError(f"Tokens {tokens_to_find} were not in the vector space.")

        self.backend.delete(curr_indices)
        if self.vector_store is not None:
            self.vector_store.delete(curr_indices)

        # Delete items starting from the highest index
        for index in sorted(curr_indices, reverse=True):
            self.items.pop(index)

    def push_to_hub(
        self,
        repo_id: str,
        token: str | None = None,
        private: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Push the Vicinity instance to the Hugging Face Hub.

        :param repo_id: The repository ID on the Hugging Face Hub
        :param token: Optional authentication token for private repositories
        :param private: Whether to create a private repository
        :param **kwargs: Additional arguments passed to Dataset.push_to_hub()
        """
        from vicinity.integrations.huggingface import push_to_hub

        push_to_hub(
            repo_id=repo_id,
            token=token,
            private=private,
            items=self.items,
            backend=self.backend,
            metadata=self.metadata,
            vector_store=self.vector_store,
            **kwargs,
        )

    @classmethod
    def load_from_hub(cls: Type[Vicinity], repo_id: str, token: str | None = None, **kwargs: Any) -> Vicinity:
        """
        Load a Vicinity instance from the Hugging Face Hub.

        :param repo_id: The repository ID on the Hugging Face Hub.
        :param token: Optional authentication token for private repositories.
        :param **kwargs: Additional arguments passed to Dataset.load_from_hub().
        :return: A Vicinity instance.
        """
        from vicinity.integrations.huggingface import load_from_hub

        items, vector_store, backend, config = load_from_hub(repo_id=repo_id, token=token)
        return Vicinity(items, backend, metadata=config["metadata"], vector_store=vector_store)

    def evaluate(
        self,
        full_vectors: npt.NDArray,
        query_vectors: npt.NDArray,
        k: int = 10,
        epsilon: float = 1e-3,
    ) -> tuple[float, float]:
        """
        Evaluate the Vicinity instance on the given query vectors.

        Computes recall and measures QPS (Queries Per Second).
        For recall calculation, the same methodology is used as in the ann-benchmarks repository.

        NOTE: this is only supported for Cosine and Euclidean metric backends.

        :param full_vectors: The full dataset vectors used to build the index.
        :param query_vectors: The query vectors to evaluate.
        :param k: The number of nearest neighbors to retrieve.
        :param epsilon: The epsilon threshold for recall calculation.
        :return: A tuple of (QPS, recall).
        :raises ValueError: If the metric is not supported by the BasicBackend.
        """
        try:
            # Validate and map the metric using Metric.from_string
            metric_enum = Metric.from_string(self.metric)
            if metric_enum not in BasicBackend.supported_metrics:
                raise ValueError(f"Unsupported metric '{metric_enum.value}' for BasicBackend.")
            basic_metric = metric_enum.value
        except ValueError as e:
            raise ValueError(
                f"Unsupported metric '{self.metric}' for evaluation with BasicBackend. "
                f"Supported metrics are: {[m.value for m in BasicBackend.supported_metrics]}"
            ) from e

        # Create ground truth Vicinity instance
        gt_vicinity = Vicinity.from_vectors_and_items(
            vectors=full_vectors,
            items=self.items,
            backend_type=Backend.BASIC,
            metric=basic_metric,
        )

        # Compute ground truth results
        gt_distances = [[dist for _, dist in neighbors] for neighbors in gt_vicinity.query(query_vectors, k=k)]

        # Start timer for approximate query
        start_time = perf_counter()
        run_results = self.query(query_vectors, k=k)
        elapsed_time = perf_counter() - start_time

        # Compute QPS
        num_queries = len(query_vectors)
        qps = num_queries / elapsed_time if elapsed_time > 0 else float("inf")

        # Extract approximate distances
        approx_distances = [[dist for _, dist in neighbors] for neighbors in run_results]

        # Compute recall using the ground truth and approximate distances
        recalls = []
        for _gt_distances, _approx_distances in zip(gt_distances, approx_distances):
            t = _gt_distances[k - 1] + epsilon
            recall = sum(1 for dist in _approx_distances if dist <= t) / k
            recalls.append(recall)

        mean_recall = float(np.mean(recalls))
        return qps, mean_recall
