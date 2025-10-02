import os
from typing import Dict, Optional, Union
from pathlib import Path

import hydra
import yaml
from hydra.utils import instantiate
from omegaconf import OmegaConf

from czbenchmarks.datasets.dataset import Dataset
from czbenchmarks.datasets.types import Organism
from czbenchmarks.file_utils import download_file_from_remote
from czbenchmarks.utils import initialize_hydra


def load_dataset(
    dataset_name: str,
    config_path: Optional[str] = None,
) -> Dataset:
    """
    Load, download (if needed), and instantiate a dataset using Hydra configuration.

    Args:
        dataset_name (str): Name of the dataset as specified in the configuration.
        config_path (Optional[str]): Optional path to a custom config YAML file. If not provided,
            only the package's default config is used.

    Returns:
        Dataset: Instantiated dataset object with data loaded.

    Raises:
        FileNotFoundError: If the custom config file does not exist.
        ValueError: If the specified dataset is not found in the configuration.

    Notes:
        - Merges custom config with default config if provided.
        - Downloads dataset file if a remote path is specified using `download_file_from_remote`.
        - Uses Hydra for instantiation and configuration management.
        - The returned dataset object is an instance of the `Dataset` class or its subclass.
    """
    initialize_hydra()

    # Load default config first and make it unstructured
    cfg = OmegaConf.create(
        OmegaConf.to_container(hydra.compose(config_name="datasets"), resolve=True)
    )

    # If custom config provided, load and merge it
    if config_path is not None:
        # Expand user path (handles ~)
        config_path = os.path.expanduser(config_path)
        config_path = os.path.abspath(config_path)

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Custom config file not found: {config_path}")

        # Load custom config
        with open(config_path) as f:
            custom_cfg = OmegaConf.create(yaml.safe_load(f))

        # Merge configs
        cfg = OmegaConf.merge(cfg, custom_cfg)

    if dataset_name not in cfg.datasets:
        raise ValueError(f"Dataset {dataset_name} not found in config")

    dataset_info = cfg.datasets[dataset_name]

    # Handle local caching and remote downloading
    dataset_info["path"] = download_file_from_remote(dataset_info["path"])

    # Instantiate the dataset using Hydra
    dataset = instantiate(dataset_info)

    # Load the dataset into memory
    dataset.load_data()

    return dataset


def list_available_datasets() -> Dict[str, Dict[str, str]]:
    """
    Return a sorted list of all dataset names defined in the `datasets.yaml` Hydra configuration.

    Returns:
        List[str]: Alphabetically sorted list of available dataset names.

    Notes:
        - Loads configuration using Hydra.
        - Extracts dataset names from the `datasets` section of the configuration.
        - Sorts the dataset names alphabetically for easier readability.
    """
    initialize_hydra()

    # Load the datasets configuration
    cfg = OmegaConf.to_container(hydra.compose(config_name="datasets"), resolve=True)

    # Extract dataset names
    datasets = {
        name: {
            "organism": str(dataset_info.get("organism", "Unknown")),
            "url": dataset_info.get("path", "Unknown"),
        }
        for name, dataset_info in cfg.get("datasets", {}).items()
    }

    # Sort alphabetically for easier reading
    datasets = dict(sorted(datasets.items()))

    return datasets


def load_local_dataset(
    dataset_class: str,
    organism: Organism,
    path: Union[str, Path],
    **kwargs,
) -> Dataset:
    """
    Instantiate a dataset directly from arguments without requiring a YAML file.

    This function is completely independent from load_dataset() and directly
    instantiates the dataset class without using OmegaConf objects.

    Args:
        target: The full import path to the Dataset class to instantiate.
        organism: The organism of the dataset.
        path: The local or remote path to the dataset file.
        **kwargs: Additional key-value pairs for the dataset config.

    Returns:
        Instantiated dataset object with data loaded.

    Example:
        dataset = load_local_dataset(
            target="czbenchmarks.datasets.SingleCellLabeledDataset",
            organism=Organism.HUMAN,
            path="example-small.h5ad",
        )
    """

    if not dataset_class:
        raise ValueError("The 'dataset_class' argument must be non-empty")
    if not dataset_class.startswith("czbenchmarks.datasets."):
        raise ValueError(
            f"Invalid dataset class {dataset_class!r}. Must start with 'czbenchmarks.datasets.'"
        )

    if isinstance(path, str):
        path = Path(path)

    resolved_path = path.expanduser().resolve()

    if not resolved_path.exists():
        raise FileNotFoundError(f"Local dataset file not found: {resolved_path}")

    module_path, class_name = dataset_class.rsplit(".", 1)
    module = __import__(module_path, fromlist=[class_name])
    DatasetClass = getattr(module, class_name)

    dataset = DatasetClass(path=str(resolved_path), organism=organism, **kwargs)
    dataset.load_data()

    return dataset
