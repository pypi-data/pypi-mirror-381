import logging
from typing import Any, Dict, List

import pandas as pd
import scipy as sp
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    make_scorer,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ..constants import RANDOM_SEED
from ..metrics import metrics_registry
from ..metrics.types import MetricResult, MetricType
from ..tasks.types import CellRepresentation
from ..types import ListLike
from .constants import MIN_CLASS_SIZE, N_FOLDS
from .task import Task, TaskInput, TaskOutput
from .utils import filter_minimum_class

logger = logging.getLogger(__name__)


class MetadataLabelPredictionTaskInput(TaskInput):
    """Pydantic model for MetadataLabelPredictionTask inputs."""

    labels: ListLike
    n_folds: int = N_FOLDS
    min_class_size: int = MIN_CLASS_SIZE


class MetadataLabelPredictionOutput(TaskOutput):
    """Output for label prediction task."""

    results: List[Dict[str, Any]]  # List of dicts with classifier, split, and metrics


class MetadataLabelPredictionTask(Task):
    """Task for predicting labels from embeddings using cross-validation.

    Evaluates multiple classifiers (Logistic Regression, KNN) using k-fold
    cross-validation. Reports standard classification metrics.

    Args:
        random_seed (int): Random seed for reproducibility
    """

    display_name = "Label Prediction"
    description = "Predict labels from embeddings using cross-validated classifiers and standard metrics."
    input_model = MetadataLabelPredictionTaskInput

    def __init__(
        self,
        *,
        random_seed: int = RANDOM_SEED,
    ):
        super().__init__(random_seed=random_seed)

    def _run_task(
        self,
        cell_representation: CellRepresentation,
        task_input: MetadataLabelPredictionTaskInput,
    ) -> MetadataLabelPredictionOutput:
        """Runs cross-validation prediction task.

        Evaluates multiple classifiers using k-fold cross-validation on the
        cell representation data. Stores results for metric computation.

        Args:
            cell_representation: gene expression data or embedding for task
            task_input: Pydantic model with inputs for the task

        Returns:
            MetadataLabelPredictionOutput: Pydantic model with results from cross-validation
        """
        # FIXME BYOTASK: this is quite baroque and should be broken into sub-tasks
        logger.info("Starting prediction task for labels")
        cell_representation = (
            cell_representation.copy()
        )  # Protect from destructive operations

        logger.info(
            f"Initial data shape: {cell_representation.shape}, labels shape: {task_input.labels.shape}"
        )

        # Filter classes with minimum size requirement
        cell_representation, labels = filter_minimum_class(
            cell_representation,
            task_input.labels,
            min_class_size=task_input.min_class_size,
        )
        logger.info(f"After filtering: {cell_representation.shape} samples remaining")

        # Determine scoring metrics based on number of classes
        n_classes = len(labels.unique())
        target_type = "binary" if n_classes == 2 else "macro"
        logger.info(
            f"Found {n_classes} classes, using {target_type} averaging for metrics"
        )

        scorers = {
            "accuracy": make_scorer(accuracy_score),
            "f1": make_scorer(f1_score, average=target_type),
            "precision": make_scorer(precision_score, average=target_type),
            "recall": make_scorer(recall_score, average=target_type),
            "auroc": make_scorer(
                roc_auc_score,
                average="macro",
                multi_class="ovr",
                response_method="predict_proba",
            ),
        }

        # Setup cross validation
        skf = StratifiedKFold(
            n_splits=task_input.n_folds, shuffle=True, random_state=self.random_seed
        )
        logger.info(
            f"Using {task_input.n_folds}-fold cross validation with random_seed {self.random_seed}"
        )

        # Create classifiers
        classifiers = {
            "lr": Pipeline(
                [("scaler", StandardScaler()), ("lr", LogisticRegression())]
            ),
            "knn": Pipeline(
                [("scaler", StandardScaler()), ("knn", KNeighborsClassifier())]
            ),
            "rf": Pipeline(
                [("rf", RandomForestClassifier(random_state=self.random_seed))]
            ),
        }
        logger.info(f"Created classifiers: {list(classifiers.keys())}")

        # Store results
        results = []

        # Run cross validation for each classifier
        labels = pd.Categorical(labels.astype(str))
        for name, clf in classifiers.items():
            logger.info(f"Running cross-validation for {name}...")
            cv_results = cross_validate(
                clf,
                cell_representation,
                labels.codes,
                cv=skf,
                scoring=scorers,
                return_train_score=False,
            )

            for fold in range(task_input.n_folds):
                fold_results = {"classifier": name, "split": fold}
                for metric in scorers.keys():
                    fold_results[metric] = cv_results[f"test_{metric}"][fold]
                results.append(fold_results)
                logger.debug(f"{name} fold {fold} results: {fold_results}")

        logger.info("Completed cross-validation for all classifiers")

        return MetadataLabelPredictionOutput(results=results)

    def _compute_metrics(
        self,
        _: MetadataLabelPredictionTaskInput,
        task_output: MetadataLabelPredictionOutput,
    ) -> List[MetricResult]:
        """Computes classification metrics across all folds.

        Aggregates results from cross-validation and computes mean metrics
        per classifier and overall.

        Args:
            _: (unused) Pydantic model with input for the task
            task_output: Pydantic model results from cross-validation

        Returns:
            List of MetricResult objects containing mean metrics across all
            classifiers and per-classifier metrics
        """
        logger.info("Computing final metrics...")
        results = task_output.results
        results_df = pd.DataFrame(results)
        metrics_list = []

        classifiers = results_df["classifier"].unique()
        all_classifier_names = ",".join(sorted(classifiers))
        params = {"classifier": f"MEAN({all_classifier_names})"}
        # Calculate overall metrics across all classifiers
        metrics_list.extend(
            [
                MetricResult(
                    metric_type=MetricType.MEAN_FOLD_ACCURACY,
                    value=metrics_registry.compute(
                        MetricType.MEAN_FOLD_ACCURACY, results_df=results_df
                    ),
                    params=params,
                ),
                MetricResult(
                    metric_type=MetricType.MEAN_FOLD_F1_SCORE,
                    value=metrics_registry.compute(
                        MetricType.MEAN_FOLD_F1_SCORE, results_df=results_df
                    ),
                    params=params,
                ),
                MetricResult(
                    metric_type=MetricType.MEAN_FOLD_PRECISION,
                    value=metrics_registry.compute(
                        MetricType.MEAN_FOLD_PRECISION, results_df=results_df
                    ),
                    params=params,
                ),
                MetricResult(
                    metric_type=MetricType.MEAN_FOLD_RECALL,
                    value=metrics_registry.compute(
                        MetricType.MEAN_FOLD_RECALL, results_df=results_df
                    ),
                    params=params,
                ),
                MetricResult(
                    metric_type=MetricType.MEAN_FOLD_AUROC,
                    value=metrics_registry.compute(
                        MetricType.MEAN_FOLD_AUROC, results_df=results_df
                    ),
                    params=params,
                ),
            ]
        )

        # Calculate per-classifier metrics
        for clf in results_df["classifier"].unique():
            params = {"classifier": clf}
            metrics_list.extend(
                [
                    MetricResult(
                        metric_type=MetricType.MEAN_FOLD_ACCURACY,
                        value=metrics_registry.compute(
                            MetricType.MEAN_FOLD_ACCURACY,
                            results_df=results_df,
                            classifier=clf,
                        ),
                        params=params,
                    ),
                    MetricResult(
                        metric_type=MetricType.MEAN_FOLD_F1_SCORE,
                        value=metrics_registry.compute(
                            MetricType.MEAN_FOLD_F1_SCORE,
                            results_df=results_df,
                            classifier=clf,
                        ),
                        params=params,
                    ),
                    MetricResult(
                        metric_type=MetricType.MEAN_FOLD_PRECISION,
                        value=metrics_registry.compute(
                            MetricType.MEAN_FOLD_PRECISION,
                            results_df=results_df,
                            classifier=clf,
                        ),
                        params=params,
                    ),
                    MetricResult(
                        metric_type=MetricType.MEAN_FOLD_RECALL,
                        value=metrics_registry.compute(
                            MetricType.MEAN_FOLD_RECALL,
                            results_df=results_df,
                            classifier=clf,
                        ),
                        params=params,
                    ),
                    MetricResult(
                        metric_type=MetricType.MEAN_FOLD_AUROC,
                        value=metrics_registry.compute(
                            MetricType.MEAN_FOLD_AUROC,
                            results_df=results_df,
                            classifier=clf,
                        ),
                        params=params,
                    ),
                ]
            )

        return metrics_list

    def compute_baseline(
        self,
        expression_data: CellRepresentation,
        **kwargs,
    ) -> CellRepresentation:
        """Set a baseline cell representation using raw gene expression.

        Instead of using embeddings from a model, this method uses the raw gene
        expression matrix as features for classification. This provides a baseline
        performance to compare against model-generated embeddings for classification
        tasks.

        Args:
            expression_data: gene expression data or embedding

        Returns:
            Baseline embedding
        """
        # Convert sparse matrix to dense if needed
        if sp.sparse.issparse(expression_data):
            expression_data = expression_data.toarray()
        return expression_data
