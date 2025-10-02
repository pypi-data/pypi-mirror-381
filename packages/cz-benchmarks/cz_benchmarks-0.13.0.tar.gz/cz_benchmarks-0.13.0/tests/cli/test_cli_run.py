# import argparse
# import datetime
# from pathlib import Path
# from unittest.mock import MagicMock, call

# from pytest_mock import MockFixture

# from czbenchmarks import runner
# from czbenchmarks.constants import PROCESSED_DATASETS_CACHE_PATH
# from czbenchmarks.cli.cli_run import (
#     get_model_arg_permutations,
#     get_processed_dataset_cache_path,
#     main,
#     run_task,
#     run_multi_dataset_task,
#     run_with_inference,
#     run_without_inference,
#     set_processed_datasets_cache,
# )
# from czbenchmarks.cli.types import (
#     CacheOptions,
#     DatasetDetail,
#     ModelArgs,
#     ModelArgsDict,
#     ModelDetail,
#     TaskArgs,
#     TaskResult,
# )
# from czbenchmarks.datasets import (
#     utils as dataset_utils,
#     types as dataset_types,
# )
# from czbenchmarks.metrics.types import MetricResult, MetricType
# from czbenchmarks.models.types import ModelType
# from czbenchmarks.tasks.clustering import ClusteringTask
# from czbenchmarks.tasks.embedding import EmbeddingTask


# def test_main(mocker: MockFixture) -> None:
#     # Setup mocks
#     mock_task_results = []
#     mock_run = mocker.patch(
#         "czbenchmarks.cli.cli_run.run", return_value=mock_task_results
#     )
#     mock_write_results = mocker.patch(
#         "czbenchmarks.cli.cli_run.write_results",
#         return_value=None,
#     )
#     mock_task_args = MagicMock()
#     mock_task_args.task = MagicMock()
#     mock_parse_task_args = mocker.patch(
#         "czbenchmarks.cli.cli_run.parse_task_args", return_value=mock_task_args
#     )
#     mock_aggregated_results = MagicMock()
#     mock_aggregate_results = mocker.patch(
#         "czbenchmarks.cli.cli_run.cli_utils.aggregate_task_results",
#         return_value=mock_aggregated_results,
#     )

#     # Handle empty inputs
#     main(
#         argparse.Namespace(
#             models=[],
#             tasks=[],
#             datasets=[],
#             output_file=None,
#             output_format=None,
#             batch_json=[],
#             batch_random_seeds=[],
#             batch_aggregate_metrics=False,
#             remote_cache_url=None,
#             remote_cache_upload="never",
#             remote_cache_upload_results=False,
#         )
#     )
#     expected_cache_options = CacheOptions(
#         remote_cache_url="",
#         download_embeddings=False,
#         upload_embeddings=False,
#         upload_results=False,
#     )
#     mock_run.assert_called_once_with(
#         dataset_names=[],
#         model_args=[],
#         task_args=[],
#         cache_options=expected_cache_options,
#     )
#     mock_write_results.assert_called_once_with(
#         mock_task_results,
#         output_format=None,
#         output_file=None,
#         cache_options=expected_cache_options,
#     )
#     mock_parse_task_args.assert_not_called()
#     mock_aggregate_results.assert_not_called()

#     # Reset mocked functions
#     mock_parse_task_args.reset_mock()
#     mock_run.reset_mock()
#     mock_write_results.reset_mock()
#     mock_aggregate_results.reset_mock()

#     # Handle complex inputs
#     main(
#         argparse.Namespace(
#             models=["SCGPT", "SCVI"],
#             tasks=["embedding", "clustering"],
#             embedding_task_label_key=["cell_type"],
#             clustering_task_label_key=["cell_type"],
#             clustering_task_set_baseline=True,
#             scgpt_model_variant=["human"],
#             scvi_model_variant=["homo_sapiens", "mus_musculus"],
#             datasets=["tsv2_blood", "tsv2_heart"],
#             output_file="output_file.yaml",
#             output_format="yaml",
#             batch_json=[""],
#             batch_random_seeds=[],
#             batch_aggregate_metrics=False,
#             remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#             remote_cache_upload_embeddings=True,
#             remote_cache_upload_results=True,
#             remote_cache_download_embeddings=False,
#         )
#     )
#     expected_cache_options = CacheOptions(
#         remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#         download_embeddings=False,
#         upload_embeddings=True,
#         upload_results=True,
#     )
#     mock_run.assert_called_once_with(
#         dataset_names=["tsv2_blood", "tsv2_heart"],
#         model_args=[
#             ModelArgs(name="SCGPT", args={"model_variant": ["human"]}),
#             ModelArgs(
#                 name="SCVI", args={"model_variant": ["homo_sapiens", "mus_musculus"]}
#             ),
#         ],
#         task_args=[mock_task_args, mock_task_args],
#         cache_options=expected_cache_options,
#     )
#     mock_write_results.assert_called_once_with(
#         mock_task_results,
#         output_format="yaml",
#         output_file="output_file.yaml",
#         cache_options=expected_cache_options,
#     )
#     assert mock_parse_task_args.call_count == 2
#     mock_aggregate_results.assert_not_called()

#     # Reset mocked functions
#     mock_parse_task_args.reset_mock()
#     mock_run.reset_mock()
#     mock_write_results.reset_mock()
#     mock_aggregate_results.reset_mock()

#     # Handle batch inputs
#     main(
#         argparse.Namespace(
#             models=["SCGENEPT"],
#             tasks=["perturbation"],
#             datasets=[],
#             output_file="output_file.yaml",
#             output_format="yaml",
#             batch_json=[
#                 '{"datasets": ["adamson_perturb"], "scgenept_dataset_name": ["adamson"], "scgenept_gene_pert": ["AEBPB+ctrl", "AEBPB+dox"]}',
#                 '{"datasets": ["norman_perturb"], "scgenept_dataset_name": ["norman"], "scgenept_gene_pert": ["NTGC+ctrl", "NTGC+dox"]}',
#             ],
#             batch_random_seeds=[1, 2],
#             batch_aggregate_metrics=None,
#             remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#             remote_cache_download_embeddings=True,
#             remote_cache_upload_embeddings=True,
#             remote_cache_upload_results=False,
#         )
#     )
#     expected_cache_options = CacheOptions(
#         remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#         download_embeddings=True,
#         upload_embeddings=True,
#         upload_results=False,
#     )
#     mock_run.assert_has_calls(
#         [
#             *[
#                 call(
#                     dataset_names=["adamson_perturb"],
#                     model_args=[
#                         ModelArgs(
#                             name="SCGENEPT",
#                             args={
#                                 "dataset_name": ["adamson"],
#                                 "gene_pert": ["AEBPB+ctrl", "AEBPB+dox"],
#                             },
#                         )
#                     ],
#                     task_args=[mock_task_args],
#                     cache_options=expected_cache_options,
#                 )
#                 for _ in range(2)  # once for each random seed
#             ],
#             *[
#                 call(
#                     dataset_names=["norman_perturb"],
#                     model_args=[
#                         ModelArgs(
#                             name="SCGENEPT",
#                             args={
#                                 "dataset_name": ["norman"],
#                                 "gene_pert": ["NTGC+ctrl", "NTGC+dox"],
#                             },
#                         )
#                     ],
#                     task_args=[mock_task_args],
#                     cache_options=expected_cache_options,
#                 )
#                 for _ in range(2)  # once for each random seed
#             ],
#         ]
#     )
#     mock_aggregate_results.assert_called_once_with(mock_task_results)


# def test_run_with_inference(mocker: MockFixture) -> None:
#     # Setup mocks
#     dataset_names = ["tsv2_blood", "tsv2_heart"]
#     mock_processed_data = MagicMock()
#     mock_processed_data.organism = dataset_types.Organism.HUMAN
#     mock_load_dataset = mocker.patch.object(
#         dataset_utils, "load_dataset", return_value=mock_processed_data
#     )
#     mock_run_inference = mocker.patch.object(
#         runner, "run_inference", return_value=mock_processed_data
#     )
#     mock_task_results = [MagicMock()]
#     mock_run_task = mocker.patch(
#         "czbenchmarks.cli.cli_run.run_task", return_value=mock_task_results
#     )
#     mocker.patch(
#         "czbenchmarks.cli.cli_run.get_processed_dataset_cache_filename",
#         return_value="test_dataset.dill",
#     )
#     mocker.patch(
#         "czbenchmarks.cli.cli_run.cli_utils.get_version",
#         return_value="0.0.0+test",
#     )
#     mocker.patch(
#         "czbenchmarks.cli.cli_run.utils.get_remote_last_modified",
#         return_value=datetime.datetime.now(datetime.timezone.utc),
#     )
#     mock_download = mocker.patch(
#         "czbenchmarks.cli.cli_run.utils.download_file_from_remote"
#     )
#     model_args = [
#         ModelArgs(name="SCGPT", args={}),
#         ModelArgs(
#             name="SCVI",
#             args={"model_variant": ["homo_sapiens", "mus_musculus"]},
#         ),
#     ]
#     embedding_task_args = TaskArgs(
#         name="embedding",
#         task=EmbeddingTask(label_key="cell_type"),
#         set_baseline=False,
#         baseline_args={},
#     )
#     clustering_task_args = TaskArgs(
#         name="clustering",
#         task=ClusteringTask(label_key="cell_type"),
#         set_baseline=True,
#         baseline_args={},
#     )
#     task_args = [embedding_task_args, clustering_task_args]

#     # Run tasks with mocked data
#     task_results = run_with_inference(
#         dataset_names=dataset_names,
#         model_args=model_args,
#         task_args=task_args,
#         cache_options=CacheOptions(
#             remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#             download_embeddings=True,
#             upload_embeddings=False,
#             upload_results=False,
#         ),
#     )

#     # Verify results
#     assert mock_load_dataset.call_count == 6  # 2 datasets * 3 model variants
#     assert len(task_results) == 12  # # 2 datasets * 3 model variants * 2 tasks

#     # Check that inference was run for each model variant, for each dataset
#     assert mock_run_inference.call_args_list == [
#         call("SCGPT", mock_processed_data, gpu=True),
#         call("SCVI", mock_processed_data, gpu=True, model_variant="homo_sapiens"),
#         call("SCVI", mock_processed_data, gpu=True, model_variant="mus_musculus"),
#         call("SCGPT", mock_processed_data, gpu=True),
#         call("SCVI", mock_processed_data, gpu=True, model_variant="homo_sapiens"),
#         call("SCVI", mock_processed_data, gpu=True, model_variant="mus_musculus"),
#     ]

#     # Check that the cache was used
#     mock_download.assert_called_with(
#         "s3://cz-benchmarks-results-dev/test/0.0.0+test/processed-datasets/test_dataset.dill",
#         Path(PROCESSED_DATASETS_CACHE_PATH).expanduser().absolute(),
#     )

#     # Check that each task was run for each model variant, for each dataset
#     assert mock_run_task.call_args_list == [
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCGPT": {}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCGPT": {}},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "homo_sapiens"}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "homo_sapiens"}},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "mus_musculus"}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "mus_musculus"}},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCGPT": {}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCGPT": {}},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "homo_sapiens"}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "homo_sapiens"}},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "mus_musculus"}},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {"SCVI": {"model_variant": "mus_musculus"}},
#             clustering_task_args,
#         ),
#     ]


# def test_run_without_inference(mocker: MockFixture) -> None:
#     # Setup mocks
#     mock_processed_data = MagicMock()
#     mock_load_dataset = mocker.patch.object(
#         dataset_utils, "load_dataset", return_value=mock_processed_data
#     )
#     mock_task_results = [MagicMock()]
#     mock_run_task = mocker.patch(
#         "czbenchmarks.cli.cli_run.run_task", return_value=mock_task_results
#     )
#     dataset_names = ["tsv2_blood", "tsv2_heart"]
#     embedding_task_args = TaskArgs(
#         name="embedding",
#         task=EmbeddingTask(label_key="cell_type"),
#         set_baseline=False,
#         baseline_args={},
#     )
#     clustering_task_args = TaskArgs(
#         name="clustering",
#         task=ClusteringTask(label_key="cell_type"),
#         set_baseline=True,
#         baseline_args={},
#     )
#     task_args = [embedding_task_args, clustering_task_args]

#     # Run tasks with mocked data
#     task_results = run_without_inference(
#         dataset_names=dataset_names,
#         task_args=task_args,
#     )

#     # Verify results
#     assert mock_load_dataset.call_count == 2  # once for each dataset
#     assert len(task_results) == 4  # # 2 datasets * 2 tasks

#     # Check that each task was run for each dataset
#     assert mock_run_task.call_args_list == [
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_blood",
#             mock_processed_data,
#             {},
#             clustering_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {},
#             embedding_task_args,
#         ),
#         call(
#             "tsv2_heart",
#             mock_processed_data,
#             {},
#             clustering_task_args,
#         ),
#     ]


# def test_run_task() -> None:
#     # Setup mocks
#     mock_dataset = MagicMock()
#     mock_dataset.organism = dataset_types.Organism.HUMAN
#     model_args: dict[str, ModelArgsDict] = {
#         ModelType.SCVI.value: {"model_variant": "homo_sapiens"}
#     }
#     mock_task_args = MagicMock()
#     mock_task_args.name = "clustering"
#     mock_task_args.task = MagicMock()
#     mock_task_args.task.display_name = "clustering"
#     mock_task_run_result = {
#         ModelType.SCVI: [
#             MetricResult(
#                 metric_type=MetricType.ADJUSTED_RAND_INDEX,
#                 value=0.1,
#                 params={"random_seed": 42},
#             )
#         ]
#     }
#     mock_task_args.task.run.return_value = mock_task_run_result

#     # Run task and check results
#     task_results = run_task(
#         "tsv2_heart",
#         dataset=mock_dataset,
#         model_args=model_args,
#         task_args=mock_task_args,
#     )
#     assert task_results == [
#         TaskResult(
#             task_name="clustering",
#             task_name_display="clustering",
#             model=ModelDetail(type="SCVI", args={"model_variant": "homo_sapiens"}),
#             datasets=[DatasetDetail(name="tsv2_heart", organism="homo_sapiens")],
#             metrics=[
#                 MetricResult(
#                     metric_type=MetricType.ADJUSTED_RAND_INDEX,
#                     value=0.1,
#                     params={"random_seed": 42},
#                 )
#             ],
#         )
#     ]


# def test_run_multi_dataset_task() -> None:
#     # Setup mocks
#     model_args: dict[str, ModelArgsDict] = {
#         ModelType.UCE.value: {"model_variant": "4l"}
#     }
#     mock_task_args = MagicMock()
#     mock_task_args.name = "cross_species"
#     mock_task_args.set_baseline = False
#     mock_task_args.task = MagicMock()
#     mock_task_args.task.display_name = "cross-species integration"
#     mock_dataset_names = ["human_spermatogenesis", "mouse_spermatogenesis"]
#     mock_embedded_datasets = [MagicMock() for _ in range(2)]
#     mock_embedded_datasets[0].organism = dataset_types.Organism.HUMAN
#     mock_embedded_datasets[1].organism = dataset_types.Organism.MOUSE
#     mock_task_run_result = {
#         ModelType.UCE: [
#             MetricResult(metric_type=MetricType.ENTROPY_PER_CELL, value=0.1, params={}),
#             MetricResult(metric_type=MetricType.BATCH_SILHOUETTE, value=0.1, params={}),
#         ]
#     }
#     mock_task_args.task.run.return_value = mock_task_run_result

#     # Run task and check results
#     task_results = run_multi_dataset_task(
#         dataset_names=mock_dataset_names,
#         embeddings=mock_embedded_datasets,
#         model_args=model_args,
#         task_args=mock_task_args,
#     )
#     assert task_results == [
#         TaskResult(
#             task_name="cross_species",
#             task_name_display="cross-species integration",
#             model=ModelDetail(type="UCE", args={"model_variant": "4l"}),
#             datasets=[
#                 DatasetDetail(name="human_spermatogenesis", organism="homo_sapiens"),
#                 DatasetDetail(name="mouse_spermatogenesis", organism="mus_musculus"),
#             ],
#             metrics=[
#                 MetricResult(
#                     metric_type=MetricType.ENTROPY_PER_CELL, value=0.1, params={}
#                 ),
#                 MetricResult(
#                     metric_type=MetricType.BATCH_SILHOUETTE, value=0.1, params={}
#                 ),
#             ],
#         )
#     ]


# def test_get_model_arg_permutations(mocker: MockFixture) -> None:
#     # 0 permutations for empty input
#     assert get_model_arg_permutations([]) == {}

#     # 1 (empty) permutation for a model with no args
#     assert get_model_arg_permutations([ModelArgs(name="SCGENEPT", args={})]) == {
#         "SCGENEPT": [{}]
#     }

#     # 1 permutation for a model with a single arg
#     assert get_model_arg_permutations(
#         [ModelArgs(name="SCGENEPT", args={"model_variant": ["norman"]})]
#     ) == {"SCGENEPT": [{"model_variant": "norman"}]}

#     # 2 permutations for a model with 1 set of  2 args
#     assert get_model_arg_permutations(
#         [ModelArgs(name="SCGENEPT", args={"model_variant": ["norman", "adamson"]})]
#     ) == {
#         "SCGENEPT": [{"model_variant": "norman"}, {"model_variant": "adamson"}],
#     }

#     # 4 permutations for a model with 2 sets of 2 args
#     assert get_model_arg_permutations(
#         [
#             ModelArgs(
#                 name="SCGENEPT",
#                 args={
#                     "model_variant": ["norman", "adamson"],
#                     "gene_pert": ["CEBPB+ctrl", "CEBPB+dox"],
#                 },
#             )
#         ]
#     ) == {
#         "SCGENEPT": [
#             {"model_variant": "norman", "gene_pert": "CEBPB+ctrl"},
#             {"model_variant": "norman", "gene_pert": "CEBPB+dox"},
#             {"model_variant": "adamson", "gene_pert": "CEBPB+ctrl"},
#             {"model_variant": "adamson", "gene_pert": "CEBPB+dox"},
#         ]
#     }


# def test_get_processed_dataset_cache_path() -> None:
#     # The cache key for a model with no args is {dataset_name}_{model_name}.dill
#     assert (
#         get_processed_dataset_cache_path("tsv2_heart", model_name="SCVI", model_args={})
#         == Path("~/.cz-benchmarks/processed_datasets/tsv2_heart_SCVI.dill")
#         .expanduser()
#         .absolute()
#     )
#     # Model args are sorted and included in the cache key
#     assert (
#         get_processed_dataset_cache_path(
#             "norman_perturb",
#             model_name="SCGENEPT",
#             model_args={"model_variant": "norman", "gene_pert": "CEBPB+ctrl"},
#         )
#         == Path(
#             "~/.cz-benchmarks/processed_datasets/norman_perturb_SCGENEPT_gene_pert-CEBPB+ctrl_model_variant-norman.dill"
#         )
#         .expanduser()
#         .absolute()
#     )


# def test_set_processed_datasets_cache(mocker: MockFixture) -> None:
#     mocker.patch(
#         "czbenchmarks.cli.cli_run.get_processed_dataset_cache_filename",
#         return_value="test_dataset.dill",
#     )
#     mock_upload = mocker.patch(
#         "czbenchmarks.cli.cli_run.utils.upload_file_to_remote",
#     )
#     mock_dataset = MagicMock()
#     mocker.patch(
#         "czbenchmarks.cli.cli_run.cli_utils.get_version",
#         return_value="0.0.0+test",
#     )
#     set_processed_datasets_cache(
#         dataset=mock_dataset,
#         dataset_name="tsv2_heart",
#         model_name="SCVI",
#         model_args={"model_variant": "homo_sapiens"},
#         cache_options=CacheOptions(
#             remote_cache_url="s3://cz-benchmarks-results-dev/test/",
#             download_embeddings=False,
#             upload_embeddings=True,
#             upload_results=False,
#         ),
#     )
#     expected_serialize_path = (
#         (Path(PROCESSED_DATASETS_CACHE_PATH) / "test_dataset.dill")
#         .expanduser()
#         .absolute()
#     )
#     mock_dataset.unload_data.assert_called_once()
#     mock_dataset.serialize.assert_called_once_with(str(expected_serialize_path))
#     mock_dataset.load_data.assert_called_once()
#     mock_upload.assert_called_once_with(
#         expected_serialize_path,
#         "s3://cz-benchmarks-results-dev/test/0.0.0+test/processed-datasets/",
#         overwrite_existing=True,
#     )
