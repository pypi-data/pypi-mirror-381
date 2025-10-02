import logging
import sys
import argparse
from typing import Optional
import anndata as ad
import pandas as pd
import numpy as np
import hydra
from hydra.utils import instantiate
import omegaconf

from czbenchmarks.datasets import SingleCellPerturbationDataset
from czbenchmarks.constants import RANDOM_SEED
from czbenchmarks.tasks.single_cell import (
    PerturbationExpressionPredictionTask,
)

from czbenchmarks.tasks.single_cell.perturbation_expression_prediction import (
    build_task_input_from_predictions,
)
from czbenchmarks.tasks.utils import (
    print_metrics_summary,
    print_correlation_metrics_baseline_and_model,
)
from czbenchmarks.tasks.types import CellRepresentation

from czbenchmarks.utils import initialize_hydra
from czbenchmarks.file_utils import download_file_from_remote


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


class Colors:
    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Run perturbation expression prediction task"
    )
    parser.add_argument(
        "--percent_genes_to_mask",
        type=float,
        default=0.5,
        help="Percentage of genes to mask",
    )
    parser.add_argument(
        "--min_logfoldchange",
        type=float,
        default=1.0,
        help="Minimum absolute log-fold change for DE filtering",
    )
    parser.add_argument(
        "--pval_threshold",
        type=float,
        default=1e-4,
        help="Adjusted p-value threshold for DE filtering",
    )
    parser.add_argument(
        "--min_de_genes_to_mask",
        type=int,
        default=5,
        help="Minimum number of DE genes required to mask a condition",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose metric output",
    )
    return parser.parse_args()


# TODO: Replace with `load_local_dataset()`
def load_dataset_config(
    dataset_name: str,
    config_name: str = "datasets",
    dataset_update_dict: Optional[dict] = None,
):
    """Customize dataset class instantiation parameters using cli args

    Args:
        dataset_name: Name of the dataset to load
        dataset_update_dict: Optional dictionary of dataset parameters to update

    Returns:
        Dataset configuration
    """
    initialize_hydra()
    cfg = hydra.compose(config_name=config_name)
    dataset_cfg = cfg.datasets[dataset_name]
    if dataset_update_dict:
        with omegaconf.open_dict(dataset_cfg) as d:
            d.update(dataset_update_dict)

    return dataset_cfg


def generate_random_model_predictions(dataset, n_cells, n_genes):
    """This demonstrates the expected format for the model predictions.
    This should be an anndata file where the obs.index contains the cell
    barcodes and the var.index contains the genes. These should be the same or a
    subset of the genes and cells in the dataset. The X matrix should be the
    model predictions.
    """

    rng = np.random.default_rng(RANDOM_SEED)
    model_predictions: CellRepresentation = rng.random((n_cells, n_genes))
    # Put the predictions in an anndata object
    model_adata = ad.AnnData(X=model_predictions)

    # The same genes and cells (or a subset of them) should be in the model adata.
    model_adata.obs.index = (
        dataset.adata.obs.index.to_series()
        .sample(frac=1, random_state=RANDOM_SEED)
        .values
    )
    model_adata.var.index = (
        dataset.adata.var.index.to_series()
        .sample(frac=1, random_state=RANDOM_SEED)
        .values
    )
    return model_adata


if __name__ == "__main__":
    """Runs a task to calculate perturbation metrics. 

    As input, this uses a SingleCellPerturbationDataset. Currently, this assumes 
    data from the Replogle et al. 2022 dataset. Additionally, this contains 
    differentially expressed genes for each perturbation. The extent of the 
    perturbation is merged with the Wilcoxon test.
    
    The dataset is filtered based on the type of statistical test, along with the minimum 
    number of differentially expressed genes, maximum p-value, and the minimum 
    log fold change or standardized mean difference. During the dataset generation, 
    the specified percentage of genes to mask is randomly selected.
    
    The dataset can be saved after filtering, and then loaded back in.
    
    In this example, a random model output is used. Instead, any model output of
    the same shape as the dataset's adata can be used.
    
    The task computes the log fold change in model predicted expression of 
    differentially expressed genes between perturbed and non-targeting groups.
    It then calculates the correlation between ground truth and predicted log 
    fold change for each condition using a variety of metrics.    
    """

    args = parse_args()
    dataset_name = "replogle_k562_essential_perturbpredict"
    logging.info(f"Loading dataset for {dataset_name} with args: {args}")

    dataset_update_dict = {
        "percent_genes_to_mask": args.percent_genes_to_mask,
        "min_logfoldchange": args.min_logfoldchange,
        "pval_threshold": args.pval_threshold,
        "min_de_genes_to_mask": args.min_de_genes_to_mask,
    }

    dataset_cfg = load_dataset_config(
        dataset_name=dataset_name, dataset_update_dict=dataset_update_dict
    )
    dataset_cfg["path"] = download_file_from_remote(dataset_cfg["path"])

    # Instantiate dataset and load data
    dataset: SingleCellPerturbationDataset = instantiate(dataset_cfg)
    dataset.load_data()
    dataset.validate()

    # This generates sample model anndata. In applications,
    # this should contain the model predictions and should be
    # provided by the user.
    model_adata = generate_random_model_predictions(
        dataset, dataset.adata.shape[0], dataset.adata.shape[1]
    )
    model_output = model_adata.X

    # Run task
    logger.info("Creating task input from predictions and dataset")
    task = PerturbationExpressionPredictionTask()
    task_input = build_task_input_from_predictions(
        predictions_adata=model_adata,
        dataset_adata=dataset.adata,
        pred_effect_operation="difference",
    )
    metrics_dict = task.run(cell_representation=model_output, task_input=task_input)
    metrics_df = pd.DataFrame(
        {
            "Model": [
                x.value
                for x in metrics_dict
                if x.metric_type.value == "spearman_correlation_calculation"
            ]
        }
    )

    # Inspect metrics
    print(
        Colors.BOLD
        + "\n------------------------------------------------------------"
        + Colors.END
    )
    print(
        Colors.BLUE
        + Colors.BOLD
        + "Summary over all conditions of correlations between mean \n"
        "predicted and ground truth changes in gene expression values." + Colors.END
    )
    print("\nDataset: Replogle K562 Essentials")
    print(
        Colors.BOLD
        + "------------------------------------------------------------\n"
        + Colors.END
    )
    print_correlation_metrics_baseline_and_model(metrics_df)

    if args.verbose:
        print(
            Colors.BOLD
            + "\n------------------------------------------------------------"
            + Colors.END
        )
        print(
            Colors.BLUE
            + Colors.BOLD
            + "Correlations between mean predicted and ground truth  \n"
            "changes in gene expression values for each condition." + Colors.END
        )
        print("\nDataset: Replogle K562 Essentials")
        print(
            Colors.BOLD
            + "------------------------------------------------------------\n"
            + Colors.END
        )

        print("\nModel Predictions \n")
        print_metrics_summary(metrics_dict)
