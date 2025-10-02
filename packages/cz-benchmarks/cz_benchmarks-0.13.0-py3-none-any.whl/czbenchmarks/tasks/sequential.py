import logging
from typing import List

import pandas as pd

from czbenchmarks.types import ListLike

from ..constants import RANDOM_SEED
from ..metrics.types import MetricResult, MetricType
from .task import Task, TaskInput, TaskOutput
from .types import CellRepresentation

logger = logging.getLogger(__name__)


class SequentialOrganizationTaskInput(TaskInput):
    """Pydantic model for Sequential Organization inputs."""

    obs: pd.DataFrame
    input_labels: ListLike
    k: int = 15
    normalize: bool = True
    adaptive_k: bool = False


class SequentialOrganizationOutput(TaskOutput):
    """Output for sequential organization task."""

    # Sequential organization doesn't produce predicted labels like clustering,
    # but we store the embedding for metric computation
    embedding: CellRepresentation


class SequentialOrganizationTask(Task):
    """Task for evaluating sequential consistency in embeddings.

    This task computes sequential quality metrics for embeddings using time point labels.
    Evaluates how well embeddings preserve sequential organization between cells.

    Args:
        random_seed (int): Random seed for reproducibility
    """

    display_name = "Sequential Organization"
    description = "Evaluate sequential consistency in embeddings using time point labels and k-NN based metrics."
    input_model = SequentialOrganizationTaskInput

    def __init__(self, *, random_seed: int = RANDOM_SEED):
        super().__init__(random_seed=random_seed)

    def _run_task(
        self,
        cell_representation: CellRepresentation,
        task_input: SequentialOrganizationTaskInput,
    ) -> SequentialOrganizationOutput:
        """Runs the sequential evaluation task.

        Gets embedding coordinates for metric computation.

        Args:
            cell_representation: gene expression data or embedding for task
            task_input: Pydantic model with inputs for the task

        Returns:
            SequentialOrganizationOutput: Pydantic model with embedding data
        """
        # Store the cell representation (embedding) for metric computation
        return SequentialOrganizationOutput(embedding=cell_representation)

    def _compute_metrics(
        self,
        task_input: SequentialOrganizationTaskInput,
        task_output: SequentialOrganizationOutput,
    ) -> List[MetricResult]:
        """Computes sequential consistency metrics.

        Args:
            task_input: Pydantic model with inputs for the task
            task_output: Pydantic model with outputs from _run_task

        Returns:
            List of MetricResult objects containing sequential metrics
        """
        from ..metrics import metrics_registry

        results = []
        embedding = task_output.embedding
        labels = task_input.input_labels

        # Embedding Silhouette Score with sequential labels
        results.append(
            MetricResult(
                metric_type=MetricType.SILHOUETTE_SCORE,
                value=metrics_registry.compute(
                    MetricType.SILHOUETTE_SCORE,
                    X=embedding,
                    labels=labels,
                ),
                params={},
            )
        )

        # Sequential alignment
        results.append(
            MetricResult(
                metric_type=MetricType.SEQUENTIAL_ALIGNMENT,
                value=metrics_registry.compute(
                    MetricType.SEQUENTIAL_ALIGNMENT,
                    X=embedding,
                    labels=labels,
                    k=task_input.k,
                    normalize=task_input.normalize,
                    adaptive_k=task_input.adaptive_k,
                ),
                params={},
            )
        )

        return results
