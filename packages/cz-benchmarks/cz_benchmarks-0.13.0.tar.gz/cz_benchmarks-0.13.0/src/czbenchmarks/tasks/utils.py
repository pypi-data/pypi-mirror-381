import logging
from typing import List, Literal

import numpy as np
import pandas as pd
import scanpy as sc
from anndata import AnnData

from ..constants import RANDOM_SEED
from ..tasks.types import CellRepresentation
from ..types import ListLike
from .constants import FLAVOR, KEY_ADDED, OBSM_KEY

logger = logging.getLogger(__name__)

MULTI_DATASET_TASK_NAMES = frozenset(["cross_species"])

TASK_NAMES = frozenset(
    {
        "clustering",
        "embedding",
        "sequential",
        "label_prediction",
        "integration",
        "perturbation",
    }.union(MULTI_DATASET_TASK_NAMES)
)


def print_correlation_metrics_baseline_and_model(
    metrics_df: pd.DataFrame,
    moderate_correlation_threshold: float = 0.3,
    precision: int = 4,
):
    """Print a summary table of all metrics.
    Args:
        metrics_dict: Dictionary of model prediction metric values
        baseline_metrics_dict: Dictionary of baseline metric values
        moderate_correlation_threshold: Threshold for considering a correlation as moderate
        precision: Precision for the summary table
    """

    # Get basic statistics using describe()
    describe_stats = metrics_df.describe()

    # Create column name mapping from describe() output to original names
    column_mapping = {
        "count": "Number of conditions",
        "mean": "Mean correlation",
        "std": "Standard Deviation",
        "min": "Min correlation",
        "25%": "25th percentile",
        "50%": "Median correlation",
        "75%": "75th percentile",
        "max": "Max correlation",
    }

    # Rename the index to match original column names
    describe_stats = describe_stats.rename(index=column_mapping)

    # Add custom statistics that aren't in describe()
    custom_stats = {}
    for col in metrics_df.columns:
        s = metrics_df[col]
        custom_stats[col] = {
            f"Number of correlations > {moderate_correlation_threshold}": sum(
                s > moderate_correlation_threshold
            ),
            "Number of negative correlations": sum(s < 0),
        }

    # Convert custom stats to DataFrame and append to describe stats
    custom_df = pd.DataFrame(custom_stats).rename_axis("Statistic")
    summary = pd.concat([describe_stats, custom_df])

    with pd.option_context("display.precision", precision):
        print(summary.to_string())


def print_metrics_summary(metrics_list):
    """Print a nice summary table of all metrics.

    Args:
        metrics_list: List of MetricResult objects or dict with metric lists
    """
    # Handle both list and dict inputs for backward compatibility
    if isinstance(metrics_list, dict):
        # Convert dict format to flat list
        all_metrics = []
        for metric_results in metrics_list.values():
            all_metrics.extend(metric_results)
        metrics_list = all_metrics

    if not metrics_list:
        print("No metrics to display.")
        return

    # Group metrics by type
    from collections import defaultdict

    grouped_metrics = defaultdict(list)

    for metric in metrics_list:
        metric_name = (
            metric.metric_type.value
            if hasattr(metric.metric_type, "value")
            else str(metric.metric_type)
        )
        grouped_metrics[metric_name].append(metric)

    # Determine grouping strategy based on available parameters
    sample_metric = metrics_list[0]
    grouping_keys = list(sample_metric.params.keys()) if sample_metric.params else []

    print("\n=== Metrics Summary ===")

    if "condition" in grouping_keys:
        # Group by condition (perturbation-style)
        _print_condition_grouped_metrics(grouped_metrics)
    elif "classifier" in grouping_keys:
        # Group by classifier (label prediction-style)
        _print_classifier_grouped_metrics(grouped_metrics)
    else:
        # Simple metric listing
        _print_simple_metrics(grouped_metrics)

    # Overall statistics
    print("\nOverall Statistics:")
    for metric_name, results in grouped_metrics.items():
        values = [r.value for r in results if not np.isnan(r.value)]
        if values:
            print(
                f"{metric_name.replace('_', ' ').title()}: "
                f"mean={np.mean(values):.4f}, std={np.std(values):.4f}, "
                f"count={len(values)}"
            )


def _print_condition_grouped_metrics(grouped_metrics):
    """Print metrics grouped by condition."""
    # Extract all unique conditions
    all_conditions = set()
    for results in grouped_metrics.values():
        for result in results:
            if "condition" in result.params:
                all_conditions.add(result.params["condition"])

    all_conditions = sorted(all_conditions)

    if not all_conditions:
        _print_simple_metrics(grouped_metrics)
        return

    # Create summary table
    summary_data = []
    for condition in all_conditions:
        row = {"condition": condition}

        for metric_name, results in grouped_metrics.items():
            # Find result for this condition
            condition_result = next(
                (r for r in results if r.params.get("condition") == condition), None
            )
            if condition_result:
                row[metric_name] = f"{condition_result.value:.4f}"
            else:
                row[metric_name] = "N/A"

        summary_data.append(row)

    # Print table
    if summary_data:
        df = pd.DataFrame(summary_data)
        print(df.to_string(index=False))
        print(f"\nResults across {len(all_conditions)} conditions")


def _print_classifier_grouped_metrics(grouped_metrics):
    """Print metrics grouped by classifier."""
    # Extract all unique classifiers
    all_classifiers = set()
    for results in grouped_metrics.values():
        for result in results:
            if "classifier" in result.params:
                all_classifiers.add(result.params["classifier"])

    all_classifiers = sorted(all_classifiers)

    # Create summary table
    summary_data = []
    for classifier in all_classifiers:
        row = {"classifier": classifier}

        for metric_name, results in grouped_metrics.items():
            # Find result for this classifier
            classifier_result = next(
                (r for r in results if r.params.get("classifier") == classifier), None
            )
            if classifier_result:
                row[metric_name] = f"{classifier_result.value:.4f}"
            else:
                row[metric_name] = "N/A"

        summary_data.append(row)

    # Print table
    if summary_data:
        df = pd.DataFrame(summary_data)
        print(df.to_string(index=False))
        print(f"\nResults across {len(all_classifiers)} classifiers")


def _print_simple_metrics(grouped_metrics):
    """Print simple metric listing without grouping."""
    for metric_name, results in grouped_metrics.items():
        print(f"\n{metric_name.replace('_', ' ').title()}:")
        for i, result in enumerate(results):
            params_str = (
                ", ".join([f"{k}={v}" for k, v in result.params.items()])
                if result.params
                else ""
            )
            params_display = f" ({params_str})" if params_str else ""
            print(f"  {i + 1}: {result.value:.4f}{params_display}")


def cluster_embedding(
    adata: AnnData,
    n_iterations: int = 2,
    flavor: Literal["leidenalg", "igraph"] = FLAVOR,
    use_rep: str = "X",
    key_added: str = KEY_ADDED,
    *,
    random_seed: int = RANDOM_SEED,
) -> List[int]:
    """Cluster cells in embedding space using the Leiden algorithm.

    Computes nearest neighbors in the embedding space and runs the Leiden
    community detection algorithm to identify clusters.

    Args:
        adata: AnnData object containing the embedding
        n_iterations: Number of iterations for the Leiden algorithm
        flavor: Flavor of the Leiden algorithm
        use_rep: Key in adata.obsm containing the embedding coordinates
                  If None, embedding is assumed to be in adata.X
        key_added: Key in adata.obs to store the cluster assignments
        random_seed (int): Random seed for reproducibility
    Returns:
        List of cluster assignments as integers
    """
    sc.pp.neighbors(adata, use_rep=use_rep, random_state=random_seed)
    sc.tl.leiden(
        adata,
        key_added=key_added,
        flavor=flavor,
        n_iterations=n_iterations,
        random_state=random_seed,
    )
    return list(adata.obs[key_added])


def filter_minimum_class(
    features: np.ndarray,
    labels: np.ndarray | pd.Series,
    min_class_size: int = 10,
) -> tuple[np.ndarray, np.ndarray | pd.Series]:
    """Filter data to remove classes with too few samples.

    Removes classes that have fewer samples than the minimum threshold.
    Useful for ensuring enough samples per class for ML tasks.

    Args:
        features: Feature matrix of shape (n_samples, n_features)
        labels: Labels array of shape (n_samples,)
        min_class_size: Minimum number of samples required per class

    Returns:
        Tuple containing:
            - Filtered feature matrix
            - Filtered labels as categorical data
    """
    label_name = labels.name if hasattr(labels, "name") else "unknown"
    logger.info(f"Label composition ({label_name}):")

    class_counts = pd.Series(labels).value_counts()
    logger.info(f"Total classes before filtering: {len(class_counts)}")

    filtered_counts = class_counts[class_counts >= min_class_size]
    logger.info(
        f"Total classes after filtering (min_class_size={min_class_size}): {len(filtered_counts)}"
    )

    labels = pd.Series(labels) if isinstance(labels, np.ndarray) else labels
    class_counts = labels.value_counts()

    valid_classes = class_counts[class_counts >= min_class_size].index
    valid_indices = labels.isin(valid_classes)

    features_filtered = features[valid_indices]
    labels_filtered = labels[valid_indices]

    return features_filtered, pd.Categorical(labels_filtered)


def run_standard_scrna_workflow(
    adata: AnnData,
    n_top_genes: int = 3000,
    n_pcs: int = 50,
    obsm_key: str = OBSM_KEY,
    random_state: int = RANDOM_SEED,
) -> CellRepresentation:
    """Run a standard preprocessing workflow for single-cell RNA-seq data.


    This function performs common preprocessing steps for scRNA-seq analysis:
    1. Normalization of counts per cell
    2. Log transformation
    3. Identification of highly variable genes
    4. Subsetting to highly variable genes
    5. Principal component analysis

    Args:
        adata: AnnData object containing the raw count data
        n_top_genes: Number of highly variable genes to select
        n_pcs: Number of principal components to compute
        random_state: Random seed for reproducibility
    """
    adata = adata.copy()

    # Standard preprocessing steps for single-cell data
    sc.pp.normalize_total(adata)  # Normalize counts per cell
    sc.pp.log1p(adata)  # Log-transform the data

    # Identify highly variable genes using Seurat method
    # FIXME: should n_top_genes be set to min(n_top_genes, n_genes)?
    sc.pp.highly_variable_genes(adata, n_top_genes=n_top_genes)

    # Subset to only highly variable genes to reduce noise
    adata = adata[:, adata.var["highly_variable"]].copy()

    # Run PCA for dimensionality reduction
    sc.pp.pca(adata, n_comps=n_pcs, key_added=obsm_key, random_state=random_state)

    return adata.obsm[obsm_key]


def is_not_count_data(
    matrix: CellRepresentation,
    sample_size: int | float = 1_000,
    tol: float = 1e-2,
    random_seed: int = RANDOM_SEED,
) -> bool:
    """
    Guess if a matrix contains log-normalized (non-integer) values by inspecting random cell sums.

    This function randomly picks a subset of rows (cells), sums their values, and checks if any
    of those sums are not close to integers, which would indicate the data is not raw counts.

    Args:
        matrix: Expression matrix (cells x genes).
        sample_size: How many cells to check (default: 1000 or all if fewer).
        tol: Allowed deviation from integer for sum to be considered integer-like.

    Returns:
        bool: True if at least one sampled cell sum is non-integer (suggesting log-normalized data).
    """
    total_cells = matrix.shape[0]
    n = int(min(sample_size, total_cells))
    indices = np.random.default_rng(random_seed).choice(total_cells, n, replace=False)
    row_totals = matrix[indices].sum(axis=1)
    if np.any(np.abs(row_totals - np.round(row_totals)) > tol):
        return True
    return False


def aggregate_cells_to_samples(
    embeddings: CellRepresentation,
    labels: ListLike,
    sample_ids: ListLike,
    aggregation_method: Literal["mean", "median"] = "mean",
) -> tuple[np.ndarray, pd.Series, pd.Series]:
    """Aggregate cell-level embeddings to sample level.

    This function groups cells by sample ID and aggregates their embeddings
    using the specified method. It also ensures that each sample has a
    consistent label (taking the first occurrence for each sample).

    Args:
        embeddings: Cell-level embeddings of shape (n_cells, d)
        labels: Cell-level labels, length n_cells
        sample_ids: Sample/donor identifiers for grouping cells, length n_cells
        aggregation_method: Method to aggregate embeddings ("mean" or "median")

    Returns:
        Tuple containing:
            - sample_embeddings: Aggregated embeddings (n_samples, d)
            - sample_labels: Labels for each sample (length n_samples)
            - sample_ids_out: Sample identifiers (length n_samples)

    Raises:
        ValueError: If inputs have mismatched lengths
    """
    embeddings = np.asarray(embeddings)
    labels = pd.Series(labels)
    sample_ids = pd.Series(sample_ids)

    if len(embeddings) != len(labels) or len(labels) != len(sample_ids):
        raise ValueError(
            f"Mismatched lengths: embeddings={len(embeddings)}, "
            f"labels={len(labels)}, sample_ids={len(sample_ids)}"
        )

    # Create DataFrame with embeddings and metadata
    emb_df = pd.DataFrame(embeddings)
    emb_df["sample_id"] = sample_ids
    emb_df["label"] = labels

    # Group by sample and aggregate embeddings (excluding non-numeric columns)
    numeric_cols = emb_df.select_dtypes(include=[np.number]).columns
    sample_emb_df = (
        emb_df[numeric_cols.tolist() + ["sample_id"]]
        .groupby("sample_id")
        .agg(aggregation_method)
    )
    sample_embeddings = sample_emb_df.values

    # Get unique labels per sample (take first occurrence)
    sample_labels_df = emb_df[["sample_id", "label"]].groupby("sample_id").first()
    sample_labels_df = sample_labels_df.reindex(sample_emb_df.index)

    return (
        sample_embeddings,
        sample_labels_df["label"],
        pd.Series(sample_emb_df.index.values, name="sample_id"),
    )
