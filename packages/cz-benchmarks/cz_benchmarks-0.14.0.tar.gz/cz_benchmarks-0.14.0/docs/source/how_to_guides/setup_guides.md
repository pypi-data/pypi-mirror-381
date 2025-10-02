# Setup Guides

## macOS Development Setup

For macOS users, follow these steps to set up your development environment:

### Prerequisites

1. **Install Tool for Python Environment and Dependency Management**  
    There are multiple tools for managing Python environments and dependencies. Popular ones include [pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), [Miniconda](https://docs.conda.io/en/latest/miniconda.html), and [Anaconda](https://www.anaconda.com/products/distribution). An alternative, [uv](https://docs.astral.sh/uv/getting-started/installation/), is described below.
    
Choose your favorite and make sure it is correctly installed.

2. **Install Xcode Command Line Tools**  
    Xcode provides essential compiler tools for macOS. Run the following command in your terminal to install it:

    ```bash
    xcode-select --install
    ```

### Setting Up the Environment

1. **Create a Virtual Environment**  
    It is highly recommended to create a virtual environment to isolate your project dependencies. The steps vary dependeing on the tool, one example is provided below for `pip` and `venv`:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

2. **Install Dependencies**  
    Install the required Python packages:

Mac requires an additional dependency, `hnswlib`, which should be installed with the package manager.

    - Install the package in editable mode with development dependencies:

      ```bash
      pip install -e ".[dev]"
      ```

---

## Using `uv` for Dependency Management

`uv` is a tool that simplifies Python dependency management. Follow these steps to set it up:

1. **Install `uv`**  
    Use `pip` to install `uv`:

    ```bash
    pip install uv
    ```

2. **Install the Required Python Version**  
    Ensure the correct Python version is installed for your project:

    ```bash
    uv python install
    ```

3. **Sync Dependencies**  
    Install all required dependencies, including extras, by running:

    ```bash
    uv sync --all-extras
    ```
4. **`hnswlib` Package Installation Error**
    
    If the `hnswlib` package fails to install with an error like `fatal error: Python.h: No such file or directory`, ensure you have installed Python development headers files and static libraries. On Ubuntu, this can be done via `sudo apt-get install python3-dev`.

> 💡 **Tip**: For more details, refer to the [official `uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/).
