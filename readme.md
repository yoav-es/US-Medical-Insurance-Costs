# U.S. Medical Insurance Costs Analysis Report

An analytical report evaluating U.S. medical insurance charges to quantify how demographic and lifestyle factors—including age, BMI, smoking status, and region—drive individual healthcare costs.

## Quick Highlights

- Notebook `Medical_Insurance_Costs_Report.ipynb` - Interactive exploratory data analysis, statistical modeling, and cost driver evaluation
- Environment Python 3.11 core runtime configuration
- Execution Local CLI, Jupyter Notebook, and Docker execution pathways

## Overview

This project analyzes individual medical charges using demographic and health indicators. The goal is to identify primary cost drivers, assess non-linear relationships across age and BMI cohorts, and evaluate regression models (such as Linear Regression and Random Forest) to predict individual insurance costs accurately.

## Features

- Data cleaning, missing value checks, and feature encoding
- Exploratory Data Analysis (EDA) with distribution plots, correlation heatmaps, and scatter plots
- Comparative regression modeling to estimate charges based on patient profiles
- Factor impact analysis highlighting high-risk categories such as smoking status
- Automated report export to static HTML format

## Project Structure

- `Medical_Insurance_Costs_Report.ipynb` — Primary interactive analysis notebook
- `tests` — Unit and integration tests
- `scripts` — Helper and automation scripts
- `reports` — Generated static HTML report outputs
- `requirements.txt` — Dependency configuration
- `.github/workflows` — CI/CD pipeline configurations
- `Dockerfile` / `docker-compose.yml` — Container setup files

## Prerequisites & Environment

- Python 3.11+
- Core dependencies
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

## Installation & Setup

1. Clone the repository
   ```bash
   git clone [https://github.com/yourusername/insurance_costs_analysis.git](https://github.com/yourusername/insurance_costs_analysis.git)
   cd insurance_costs_analysis
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

## Development & Code Quality

### Testing

Run the test suite

```bash
pytest tests -v
```

### Pre-commit & Formatting

Install and run formatting tools (Black, Ruff, isort)

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Execution & Report Generation

### Local Execution

Generate the executed notebook and HTML report locally

```bash
python -m nbconvert --to notebook --execute Medical_Insurance_Costs_Report.ipynb --output reports/executed_Medical_Insurance_Costs_Report.ipynb
python -m nbconvert --to html reports/executed_Medical_Insurance_Costs_Report.ipynb --output reports/Medical_Insurance_Costs_Report.html
```

### Docker Execution (Isolated Environment)

Build and run using Docker Compose

```bash
docker compose build
docker compose run --rm report
```

Or run via interactive helper scripts

- Linux / macOS / WSL: `bash scripts/run_report_docker.sh`
- Windows: `powershell -ExecutionPolicy Bypass -File scripts/run_report_docker.ps1`

Outputs `reports/executed_Medical_Insurance_Costs_Report.ipynb`, `reports/Medical_Insurance_Costs_Report.html`

## Usage & Workflow

Launch the interactive Jupyter notebook environment

```bash
jupyter notebook Medical_Insurance_Costs_Report.ipynb
```

Typical analytical workflow
1. Data Review: Understand dataset schema, column types, and structural properties.
2. Data Cleaning & Formatting: Remove duplicates, handle missing values, and correct data types.
3. Exploratory Data Analysis (EDA): Visualize statistical distributions, correlations, and key relationships.
4. Analysis & Modeling: Execute domain-specific analysis, answer core questions, or evaluate models.
   - Primary cost driver identification across demographic variables
   - Regression model training and evaluation (Linear Regression vs. Random Forest)
5. Conclusions: Synthesize findings, document limitations, and outline actionable next steps.

## Continuous Integration

CI pipelines are managed via GitHub Actions (`.github/workflows/ci.yml`), which automatically runs tests, checks code style, and executes the report build on repository updates.

## Data Source

This report uses the Medical Cost Personal Dataset from Kaggle: https://www.kaggle.com/datasets/mirichoi0218/insurance

- **Required Files**: `insurance.csv`
- **Location**: Place the required files into the `data/` directory.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.