# --- STAGE 1: Build & Dependency Install ---
FROM python:3.12-slim-bookworm AS builder

# Set environment variables for non-interactive mode and Python unbuffered output
ENV PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

# Install build dependencies required for popular Python packages (like cryptography, numpy, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the dependency files
COPY ./requirements.txt .
COPY ./.flake8 .  

# Install dependencies (including FastAPI and Uvicorn)
# 2. Install Flake8 and other dependencies
RUN pip install --no-cache-dir flake8 && \
    pip install --no-cache-dir -r requirements.txt

RUN echo "Running Flake8 code quality check..." && \
    flake8 .
    
# --- STAGE 2: Production Runtime ---
# Use a minimal Python image for the final container
FROM python:3.12-slim-bookworm AS production

# Set the working directory
WORKDIR /app

# Create a non-root user and set permissions
ARG USER_NAME=user
ARG UID=1000
RUN groupadd ${USER_NAME}
# Add a non-root user with a home directory
RUN adduser --system --uid ${UID} --home /app ${USER_NAME}
# Ensure the non-root user owns the /app directory
RUN chown -R ${USER_NAME}:${USER_NAME} /app

# Copy only the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Copy application code
COPY . .
COPY main.py .
COPY config.py .

# Switch to the non-root user for execution (Security Best Practice)
USER ${USER_NAME}

# Expose the port Uvicorn runs on
EXPOSE 8000

# Command to run the application using Uvicorn
# 'main:app' assumes your FastAPI application instance is named 'app' inside 'main.py'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]