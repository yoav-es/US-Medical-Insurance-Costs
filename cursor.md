Cursor assistant prompt — change summary for this project

Use this prompt with Cursor (or any assistant) to generate a concise, actionable summary of changes made to a repository, and to extract the automation/scripts that were added so they can be applied to other projects.

Prompt:

You are a repository assistant. Given this project's working tree and git history, produce a concise, actionable summary that a developer can reuse to apply the same refactor/automation to another repository.

Answer the sections below using 2–8 short bullets each. Prefer Docker-based, OS-agnostic commands. Where relevant, mention file paths and exact commands.

1) What did you change in this project?
  - Extracted notebook logic into a small package `insurance_costs/` with modules: `data_io.py`, `processing.py`, `analysis.py`, `viz.py`, and `__init__.py` (version 1.0.0).
  - Added unit tests under `tests/` (test_io.py, test_processing.py, test_analysis.py, test_analysis_extra.py, test_viz.py); 8 tests pass with pytest.
  - Added developer and CI infra: `requirements.txt`, `.pre-commit-config.yaml`, `pyproject.toml`, `.github/workflows/ci.yml` (runs tests and executes the notebook).
  - Added reproducible report tooling: `Dockerfile`, `docker-compose.yml`, interactive runners `scripts/run_report_docker.sh` and `scripts/run_report_docker.ps1`.
  - Unified all plot sizes to `figsize=(8, 5)` across both notebook cells and `viz.py` functions.
  - Added meaningful code comments throughout the notebook explaining statistical reasoning and visualization choices.
  - Updated README.md to match portfolio style (consistent with biodiversity repo); fixed typos in notebook markdown cells.
  - Renamed output artifacts from `*-executed.*` to `report.ipynb` / `report.html`.
  - Updated `.gitignore` to exclude generated report outputs but include `insurance.csv` (the project dataset).
  - Configured `pyproject.toml` with `setuptools.build_meta` and package discovery so `pip install -e .` works; CI installs the package in editable mode.

2) What did you add that might be problematic or worth reviewing?
  - Notebook outputs have stale `display_data` cells missing `metadata` fields; nbconvert strict validation rejects them. Workaround: use `--ClearOutputPreprocessor.enabled=True` when executing, or fix metadata with a script before running.
  - Large Docker image install steps (build-essential, ipykernel) increase image size — note trade-offs if you later add PDF export.
  - Report artifacts (`report.ipynb`, `report.html`) are gitignored — decide whether to upload as CI artifacts instead.
  - The notebook still contains inline analysis code alongside the extracted package; the package functions are available for reuse but the notebook doesn't call them directly (to preserve the original cell structure and ordering).

3) What required multiple fixes / iteration and why?
  - Notebook cell edits: the `EditNotebook` tool requires exact string matches; solved by using Python `repr()` to extract precise cell content before editing.
  - PowerShell quoting: multi-line Python commands and heredocs don't work in PowerShell's shell; solved by writing helper `.py` scripts or using single-line commands with careful escaping.
  - Plot ordering: initial attempt to replace inline code with package function calls via a runner cell broke the notebook structure (plots separated from their section headlines); solved by reverting and keeping inline code, applying only minimal figsize changes in-place.
  - Notebook metadata validation: `display_data` outputs from older Jupyter versions lacked `metadata: {}`; nbconvert rejected the notebook before any preprocessor could clear them; solved by patching the JSON directly.
  - Kernel errors in CI: nbconvert failed with "No such kernel named python3"; fixed by installing `ipykernel` and registering a `python3` kernel in the Dockerfile and CI.
  - Module not found in CI: tests failed with `ModuleNotFoundError: No module named 'insurance_costs'` because CI doesn't add the project root to `sys.path`; fixed by adding `pip install -e .` to the CI workflow and configuring `[tool.setuptools.packages.find]` in `pyproject.toml`.
  - Missing dataset in CI: notebook execution failed with `FileNotFoundError: insurance.csv`; the `.gitignore` had `*.csv` which excluded the dataset from the repo; fixed by adding `!insurance.csv` exception to `.gitignore` and committing the file.

4) Automation, CI/CD, Docker, and helper scripts added (path, purpose, exact command)
  - `.github/workflows/ci.yml` — CI that installs deps, runs tests, registers kernel, executes notebook.
    - Trigger: push / pull_request to main, master, cursor-refactor.
  - `Dockerfile` — image used to run/execute notebook and produce report; installs runtime deps and `ipykernel`.
    - Build: `docker compose build`
  - `docker-compose.yml` — defines `report` service that mounts project and runs commands.
    - Run report one-liner: `docker compose run --rm report`
  - `scripts/run_report_docker.sh` (bash) — interactive runner: build, execute notebook, export HTML; use: `bash scripts/run_report_docker.sh`
  - `scripts/run_report_docker.ps1` (PowerShell) — Windows interactive runner; use: `powershell -ExecutionPolicy Bypass -File .\scripts\run_report_docker.ps1`
  - `requirements.txt` — runtime deps for CI/Docker (linters kept in pre-commit only, not in runtime).
  - Local report generation (without Docker):
    - `python -m nbconvert --to notebook --execute us-medical-insurance-costs.ipynb --output report.ipynb`
    - `python -m nbconvert --to html report.ipynb --output report.html`

5) Checklist to apply same improvements to another repository
  - 1) Create small package folder and extract reusable functions (data_io, processing, analysis, viz); add `__init__.py` and set package version.
  - 2) Add unit tests (pytest). Run locally; fix imports and fixtures.
  - 3) Add `requirements.txt` (runtime only) and `.pre-commit-config.yaml` for linting; avoid installing linters in runtime image.
  - 4) Add `pyproject.toml` with project metadata, runtime dependencies, and dev extras.
  - 5) Add `Dockerfile` and `docker-compose.yml` that install runtime deps and `ipykernel`; register a `python3` kernel (for nbconvert).
  - 6) Add interactive scripts: `run_report_docker.sh` and `run_report_docker.ps1` that call `docker compose` one-liners.
  - 7) Add CI workflow: checkout, setup-python, pip install -r requirements.txt, pip install -e ., register ipykernel, run pytest, execute notebook with nbconvert.
  - 8) Ensure the dataset CSV is committed (add `!dataset.csv` exception to `.gitignore` if CSVs are ignored).
  - 9) Unify plot sizes and add code comments explaining statistical reasoning.
  - 10) Update README to follow consistent portfolio style across repos.
  - 11) Rename output artifacts to `report.*` and update `.gitignore`.
  - 12) Fix any notebook validation issues (missing metadata on display_data outputs) before committing.

Constraints reminder:
- Keep answers concise when generating the summary.
- Prefer Docker-based commands for cross-platform compatibility.
- Flag trade-offs for large installs (TeX/Playwright).

Use this updated prompt with Cursor to produce the final change-summary you asked for when applying this pattern to other projects.
