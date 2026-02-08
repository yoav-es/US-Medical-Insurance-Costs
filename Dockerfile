FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \\
    && apt-get install -y --no-install-recommends build-essential \\
    && pip install --no-cache-dir -r requirements.txt \\
    && python -m ipykernel install --user --name=python3 || true \\
    && apt-get remove -y build-essential \\
    && rm -rf /var/lib/apt/lists/*
COPY . .
CMD [\"sh\"]
