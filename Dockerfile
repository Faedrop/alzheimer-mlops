FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=100 --retries 5 -r requirements.txt

COPY src/ src/
COPY config.yaml .

CMD ["python", "-m", "src.train"]