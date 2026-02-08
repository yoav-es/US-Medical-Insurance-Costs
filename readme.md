# U.S. Medical Insurance Costs

This project analyzes U.S. medical insurance costs by examining how geographic region, BMI categories, and smoking status influence annual charges. Key summary statistics and cross-tabulations reveal which factors drive higher expenses and how they interact. The dataset is sourced from a Kaggle exercise and is based on simulated U.S. insurance records.

## Features

* Computes mean, median, standard deviation, and IQR of charges per region.
* Groups patients by BMI category (Underweight, Healthy, Overweight, Obese) and compares costs.
* Builds pivot tables and correlations showing how smoking amplifies BMI-driven costs.
* Produces bar charts, histograms, and dual-axis plots with a unified figure size.

## Prerequisites

* Python 3.10+
* pandas
* matplotlib
* seaborn
* Jupyter Notebook / nbconvert

## Installation

Clone the repository and install the required packages:

    git clone https://github.com/yoav-es/U.S.-Medical-Insurance-Costs.git
    cd "U.S. Medical Insurance Costs"
    pip install -r requirements.txt

## Usage

Launch the Jupyter Notebook to run the analysis step-by-step:

    jupyter notebook us-medical-insurance-costs.ipynb

Or generate an executed report from the command line:

    python -m nbconvert --to notebook --execute us-medical-insurance-costs.ipynb --output report.ipynb
    python -m nbconvert --to html report.ipynb --output report.html

To run the test suite:

    pytest -q

To build and run via Docker:

    docker compose build
    docker compose run --rm report

## Files

* **us-medical-insurance-costs.ipynb** — Main analysis notebook
* **insurance_costs/** — Reusable Python package (data I/O, processing, analysis, visualization)
* **tests/** — pytest test suite
* **requirements.txt** — Runtime and development dependencies
* **pyproject.toml** — Package metadata and dev extras
* **Dockerfile** / **docker-compose.yml** — Reproducible report generation
* **scripts/** — Docker helper scripts for Linux/macOS and Windows
* **.github/workflows/ci.yml** — CI pipeline: tests and notebook execution

## Data Source

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance). Place `insurance.csv` in the project root before running.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.