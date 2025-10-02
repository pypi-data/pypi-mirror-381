# Guide to Perturbation Expression Prediction Benchmark

## Overview

This task evaluates a model’s ability to predict the expression of masked genes using the remaining unmasked genes as context, across both CRISPR perturbed and unperturbed control cells. The Replogle K562 Essentials[^replogle-k562-essentials] dataset is a Perturb-seq resource profiling essential gene knockdowns in the K562 leukemia cell line, providing a benchmark set of perturbation and matched control cells. 

Within this dataset, we first compute log fold change values for all genes by comparing perturbed cells to their matched controls. The model is then evaluated on its ability to predict expression changes based on cell context, and these predictions are compared directly against the observed log fold changes.


- Single cell perturbation datasets contain perturbed and control cells. Matched controls have been determined for each condition and are stored in the unstructured portion of the AnnData under the key `control_cell_map`.
- The differential expression results are also stored in the unstructured portion of the AnnData in the key `de_results_wilcoxon`. This analysis utilized the Wilcoxon rank-sum test.

This benchmark is designed for evaluation by any model that produces a prediction matrix whose cell ids (rows) and gene names (columns) can be ordered identically to  those used by the dataset. The task ensures alignment by validating gene and cell indices against the dataset. The predictions provided to the task can be in any unit (e.g. counts, log transformed) that is monotonic to the differential expression results (log2FC).

## Dataset Functionality and Parameters

The data preprocessing method accomplishes the following:

- Perturbed cells and their matched controls are selected and indexed to create a new AnnData object for each condition. Conditions are stored in AnnData `obs` metadata column defined by the parameter ``{condition_key}``.
- In the control matched data, the perturbations are labeled as ``{perturb}``, and control cells are labeled as ``{control_name}``.
- For each condition, a subset of DE genes are sampled and their default values are masked. These become the prediction targets for the model.
- The objective is for the model to predict the masked expression values for the prediction targets per cell and per condition.

### Data Parameters

The following parameters are used in loading the data:

- `condition_key`: The name of the column in `adata.obs` and in the DE results containing condition labels for perturbations and controls. Default is "condition".
- `control_name`: The name used to denote control samples in the `condition_key` column of the metadata (`adata.obs`). Default is "ctrl".
- `de_gene_col`: The name of the column in the DE results indicating gene identifiers to be considered for masking. Default is "gene_id".
- `de_metric_col`: The name of the metric column in the differential expression data. Default is "logfoldchange".
- `de_pval_col`: The name of the p-value column in the differential expression data. Default is "de_pval_col".

### Masking Parameters

The following parameters control masking of the DE genes:

- `percent_genes_to_mask`: The fraction of DE genes per condition to mask as prediction targets for the model. Default value is 0.5.
- `min_de_genes_to_mask`: Minimum number of sampled DE genes required for a condition to be eligible for masking. This threshold is applied after the genes are sampled. Default value is 5.
- `pval_threshold`: Maximum adjusted p-value for DE filtering based on the output of the DE analysis. This data must be in the column `pval_adj`. Default value is 1e-4.
- `min_logfoldchange`: Minimum absolute log-fold change to determine when a gene is considered differentially expressed. This data must be in the column `logfoldchange`. Only used when the DE analysis uses Wilcoxon rank-sum. Default value is 1.
- `target_conditions_override`: An externally supplied list of target conditions for customized masking. This overrides the default sampling of genes for masking in `target_conditions_dict`. 

The parameters `condition_key` and `control_name` are as described above and also used for masking. Parameters shared with other single-cell datasets (e.g., `path`, `organism`, `task_inputs_dir`, `random_seed`) are also required but not described here.

### Saving the Dataset

To cache and reuse dataset outputs without re-running preprocessing, the outputs of the dataset can be saved with the `store_task_inputs` method of the [`SingleCellPerturbationDataset`](../autoapi/czbenchmarks/datasets/single_cell_perturbation/index.html):

  ```python
  task_inputs_dir = dataset.store_task_inputs()
  ```

## Task Functionality and Parameters 

This task evaluates predictions of perturbation-induced changes in gene expression against their ground truth values by correlating their values. The predictions provided to the task can be in any format that is monotonic with the differential expression results. Predicted changes are computed per condition as the difference in mean expression between perturbed and matched control cells, for the subset of masked genes.

The task class also calculates a baseline prediction (`compute_baseline` method), which takes as input a `baseline_type`, either `median` (default) or `mean`, that calculates the median or mean expression values, respectively, across all masked values in the dataset.

The following parameters are used by the task input class, via the [`PerturbationExpressionPredictionTaskInput`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) class:  

- `adata`: The AnnData object produced when the data are loaded by the dataset class ([`SingleCellPerturbationDataset`](../autoapi/czbenchmarks/datasets/single_cell_perturbation/index.html)), containing control-matched and masked data.
- `pred_effect_operation`: This determines how to compute the effect between treated and control mean predictions. There are two possible values: "difference" uses `mean(treated) - mean(control)` and is generally safe across scales; "ratio" uses `log((mean(treated)+eps)/(mean(control)+eps))` when means are all positive. The default is "ratio".
- `cell_index`: Sequence of user-provided cell index is vertically aligned with `cell_representation` matrix, which contains the predictions from the model.
- `gene_index`: Sequence of user-provided gene names is horizontally aligned with `cell_representation` matrix, which contains the predictions from the model.

The main task, [`PerturbationExpressionPredictionTask`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) requires only an optional random seed as input. The dataclass ([`PerturbationExpressionPredictionTaskInput`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html)) and a matrix of model predictions is required to be provided to the `run` method which executes the task.

The task returns an object of type [`PerturbationExpressionPredictionOutput`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) (a Pydantic model), which contains the following:

- `pred_mean_change_dict`: The predicted fold change for the masked genes based on the model.
- `true_mean_change_dict`: The ground truth fold change based on the differential expression results provided by the dataset.

These outputs are then provided to the metric for computation of the [Spearman correlation](../autoapi/czbenchmarks/metrics/implementations/index.html).


### Notes on Loading Model Predictions

When a user loads in model predictions, the cells and genes whose expression values are predicted should each be a subset of those in the dataset. At the start of the task, validation is performed to ensure these criteria are met. 

It is essential that the mapping of the cells (rows) and genes (columns) from the model expression predictions to those in the dataset is correct. Thus, the [`PerturbationExpressionPredictionTaskInput`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) requires a `gene_index` and `cell_index` to be provided by the user for validation.

If the user has an AnnData (model_adata) with model predictions, and a [`SingleCellPerturbationDataset`](../autoapi/czbenchmarks/datasets/single_cell_perturbation/index.html) with loaded data, [`PerturbationExpressionPredictionTaskInput`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) can be prepared using the [`build_task_input_from_predictions`](../autoapi/czbenchmarks/tasks/single_cell/perturbation_expression_prediction/index.html) function:

  ```python
  task_input = build_task_input_from_predictions(predictions_adata=model_adata, dataset_adata=dataset.adata)
  ```

## Metrics

The task produces a per-condition correlation by comparing predicted and ground-truth expression values for the masked genes. The comparison metric is:

- **Spearman correlation (rank)**: Rank correlation between the raw predicted and ground truth values. As this is a rank metric, the predictions can be supplied in any units that are monotonic to the ground truth data, the later of which is in units of log fold change (log2FC).


Results are generated for each perturbation condition separately. Downstream reporting may aggregate scores across conditions (e.g., mean and standard deviation).

For large-scale benchmarks, metrics can be exported to CSV/JSON via the provided [`czbenchmarks.tasks.utils.print_metrics_summary helper`](../autoapi/czbenchmarks/tasks/utils/index.html), or integrated into custom logging frameworks.

## Example Usage

For example use cases, see the example script `examples/example_perturbation_expression_prediction.py`.  

In this example, random predictions are generated for the cells and genes and provided to the task as representative model predictions for calculating the final metric. This serves as an example of the workflow for running the task to completion.

[^replogle-k562-essentials]: Replogle, J. M., Elgamal, R. M., Abbas, A. et al. Mapping information-rich genotype–phenotype landscapes with genome-scale Perturb-seq. Cell, 185(14):2559–2575.e28 (2022). [DOI](https://doi.org/10.1016/j.cell.2022.05.013)
