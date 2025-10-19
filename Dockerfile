FROM python:3.12-slim-bookworm AS builder

# Set environment variables for non-interactive mode and Python unbuffered output
ENV PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

# Install build dependencies required for popular Python packages (like cryptography, numpy, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*