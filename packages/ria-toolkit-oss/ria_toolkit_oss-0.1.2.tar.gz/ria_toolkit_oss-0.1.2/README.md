<h2 align="center">
  <br>
  <img src="https://riahub.ai/qoherent/ria-toolkit-oss/raw/branch/main/docs/images/ria_logo.svg" alt="RIA Toolkit OSS", width="400">
</h2>

<h3 align="center">RIA Toolkit OSS, By <a href="https://qoherent.ai/">Qoherent</a></h3>

<h4 align="center">Let's build intelligent radios together 📡🚀</h4>

<p align="center">
  <!-- PyPI -->
  <a href="https://pypi.org/project/ria-toolkit-oss">
    <img src="https://img.shields.io/pypi/v/ria-toolkit-oss"/>
  </a>
  <!-- Conda (RIA Hub) -->
  <a href="https://riahub.ai/qoherent/-/packages/conda/ria-toolkit-oss">
    <img src="https://img.shields.io/badge/conda-ria--toolkit--oss-green.svg" alt="Conda on RIA Hub">
  </a>
  <!-- License -->
  <a href="https://www.gnu.org/licenses/agpl-3.0">
    <img src="https://img.shields.io/badge/License-AGPLv3-blue.svg" />
  </a>
  <!-- Docs -->
  <a href="https://ria-toolkit-oss.readthedocs.io">
    <img src="https://img.shields.io/badge/docs-ria--toolkit--oss-blue"/>
  </a>
  <!-- Python Version -->
  <a href="https://www.python.org/downloads">
    <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Version">
  </a>
</p>

# RIA Toolkit OSS

RIA Toolkit OSS is the open-source version of the RIA Toolkit, providing the fundamental components to help engineers and researchers get started building, testing, and deploying radio intelligence applications.

## 🌟 Key features

- Core classes for loading, managing, and interacting with machine learning assets, including recordings, models, and datasets.

- Fundamental recording augmentations and impairments for radio ML dataset preparation.

- A unified interface for interacting with software-defined radios, including [USRP](https://www.ettus.com/products/), [BladeRF](https://www.nuand.com/), [PlutoSDR](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html), and [bladeRF](https://www.nuand.com/bladerf-1/). (Support for [RTL-SDR](https://www.rtl-sdr.com/), [HackRF](https://greatscottgadgets.com/hackrf/), and [thinkRF](https://thinkrf.com/) coming soon!).

## 💡 Want More RIA?

- **[RIA Toolkit](https://qoherent.ai/riatoolkit/)**: The full, unthrottled set of tools for developing, testing, and deploying radio intelligence applications.

- **[RIA Hub](https://qoherent.ai/riahub/)**: Wield the RIA Toolkit, plus purpose-built automations, directly in your browser without the need to write code or set up infrastructure. Additionally, unlock access to Qoherent's rich IP library as well as community projects. 

- **[RIA RAN](https://qoherent.ai/intelligent-5g-ran/)**: Radio intelligence solutions engineered to seamlessly integrate with existing RAN environments, including ORAN-compliant networks.

## 🚀 Getting started

RIA Hub Toolkit OSS can be installed either as a Conda package or as a standard Python package. 

Please note that SDR drivers must be installed separately. Refer to the relevant guide in the project documentation for setup instructions: [SDR Guides](https://ria-toolkit-oss.readthedocs.io/en/latest/sdr_guides/).

### Installation with Conda (recommended)

Conda package for RIA Toolkit OSS are available on RIA Hub: [RIA Hub Conda Package Registry: `ria-toolkit-oss`](https://riahub.ai/qoherent/-/packages/conda/ria-toolkit-oss).

RIA Toolkit OSS can be installed into any Conda environment. However, it is recommended to install within the base environment of [Radioconda](https://github.com/radioconda/radioconda-installer), which includes [GNU Radio](https://www.gnuradio.org/) and several pre-configured libraries for common SDR devices.

Please follow the steps below to install RIA Toolkit OSS using Conda:

1. Before installing RIA Toolkit OSS into your Conda environment, update the Conda package manager:

    ```bash
    conda update --force conda
    ```

    This ensures that the Conda package manager is fully up-to-date, allowing new or updated packages to be installed into the base environment without conflicts.

2. Add RIA Hub to your Conda channel configuration:

    ```bash
    conda config --add channels https://riahub.ai/api/packages/qoherent/conda
    ```

3. Activate your Conda environment and install RIA Toolkit OSS. For example, with Radioconda:

    ```bash
    conda activate base
    conda install ria-toolkit-oss
    ```

4. After installing RIA Toolkit OSS, verify that the installation was successful by running:

    ```bash
    conda list
    ```

    If installation was successful, you should see a line item for `ria-toolkit-oss`:

    ```bash
    ria-toolkit-oss           <version>                  <build>    https://riahub.ai/api/packages/qoherent/conda
    ```

### Installation with pip

RIA Toolkit OSS is available as a standard Python package on both RIA Hub and PyPI:
- [RIA Hub PyPI Package Registry: `ria-toolkit-oss`](https://riahub.ai/qoherent/-/packages/pypi/ria-toolkit-oss)
- [PyPI: `ria-toolkit-oss`](https://pypi.org/project/ria-toolkit-oss/)

These packages can be installed into a standard Python virtual environment using [pip](https://pip.pypa.io/en/stable/). For help getting started with Python virtual environments, please refer to the following tutorial: [Python Virtual Environments](https://www.w3schools.com/python/python_virtualenv.asp).

Please follow the steps below to install RIA Toolkit OSS using pip:

1. Create and activate a Python virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    <details>
    <summary><strong>Windows (Command Prompt)</strong></summary>

    ```commandline
    python -m venv venv
    venv\Scripts\activate
    ```

    </details>

2. Install RIA Toolkit OSS from PyPI with pip:

    ```bash
    pip install ria-toolkit-oss
    ```

    RIA Toolkit OSS can also be installed from RIA Hub. However, RIA Hub does not yet support a proxy or cache for public packages. We intend to add this missing functionality soon. In the meantime, please use the `--no-deps` option with pip to skip automatic dependency installation, and then manually install each dependency afterward.

### Installation from source

Finally, RIA Toolkit OSS can be installed directly from the source code. This approach is only recommended if you require an unpublished or development version of the project. Follow the steps below to install RIA Toolkit OSS from source:

1. Clone the repository. For example:

    ```bash
    git clone https://riahub.ai/qoherent/ria-toolkit-oss.git
    ```

2. Navigate into the project directory:

    ```bash
    cd ria-toolkit-oss
    ```

3. Install with pip:

    ```bash
    pip install .
    ```

### Basic usage 

Once the project is installed, you can import modules, functions, and classes from the Toolkit for use in your Python code. For example, you can use the following import statement to access the `Recording` object:

```python
from ria_toolkit_oss.datatypes import Recording
```

Additional usage information is provided in the project documentation: [RIA Toolkit OSS Documentation](https://ria-toolkit-oss.readthedocs.io/).

## 🐛 Issues

Kindly report any issues on RIA Hub: [RIA Toolkit OSS Issues Board](https://riahub.ai/qoherent/ria-toolkit-oss/issues).

## 🤝 Contribution

Contributions are always welcome! Whether it's an enhancement, bug fix, or new example, your input is valuable. If you'd like to contribute to the project, please reach out to the project maintainers.

If you have a larger project in mind, please [contact us](https://www.qoherent.ai/contact/) directly, we'd love to collaborate with you. 🚀

## 🖊️ Authorship

RIA Toolkit OSS is developed and maintained by [Qoherent](https://qoherent.ai/), with the invaluable support of many independent contributors.

If you are doing research with RIA Toolkit OSS, please cite the project:

```
[1] Qoherent Inc., "Radio Intelligence Apps Toolkit OSS," 2025. [Online]. Available: https://riahub.ai/qoherent/ria-toolkit-oss
```

If you like what we're doing, don't forget to give the project a star! ⭐

## 📄 License

RIA Toolkit OSS is **free and open-source**, released under AGPLv3. 

Alternative permissive and commercial licensing options are available upon request. Please [contact us](https://qoherent.ai/contact/) for further details.

## 💻 Developer information

This project adheres to [Qoherent's Coding Guidelines](https://github.com/qoherent/.github/blob/main/docs/CODING.md). We kindly ask you to review them before getting started.

### Poetry

To ensure a consistent development environment, this project uses [Poetry](https://python-poetry.org/) for dependency management. You can initialize a new Poetry environment by running `install` from anywhere within the project:
```bash
poetry install
```

Running `install` when a `poetry.lock` file is present resolves and installs all dependencies listed in `pyproject.toml`, but Poetry uses the exact versions listed in `poetry.lock` to ensure that the package versions are consistent for everyone working on your project. Please note that the project itself will be installed in editable mode.

Unit tests can be run with the following command:
```bash
poetry run pytest
```

Source and wheels archives can be built with the following command:
```bash
poetry build
```

For more information on basic Poetry usage, start [here](https://python-poetry.org/docs/basic-usage/).

### Sphinx

Project documentation is auto-generated from project docstrings using [Sphinx](https://www.sphinx-doc.org/en/master/). Therefore, all importable components require complete and comprehensive docstrings, complete with [doctest](https://docs.python.org/3/library/doctest.html) usage examples.

It's recommended to use `sphinx-autobuild`, which eliminates the need to manually rebuild the docs after making changes:
```bash
poetry run sphinx-autobuild docs/source docs/build/html
```

When using `sphinx-autobuild`, the docs will automatically be served at http://127.0.0.1:8000.

To build the project documentation manually, navigate to the `docs` directory and run the following commands:
```bash
poetry run make clean
poetry run make html
```

Once the documentation is built, you can view it by opening `docs/build/html/index.html` in a web browser. Please note that this strategy requires manually rebuilding the documentation to view updates.

For more information on basic Sphinx usage, start [here](https://sphinx-rtd-tutorial.redatatypeshedocs.io/en/latest/index.html).

### tox

This project uses [`tox`](https://tox.wiki/en/latest/index.html) to streamline testing and release. tox runs linting and formatting checks and tests
the package across multiple version of Python.

Use the following command to run tests with tox:
```bash
poetry run tox
```

For more information on basic tox usage, start [here](https://tox.wiki/en/latest/user_guide.html).
