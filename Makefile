# Define the Docker Compose file path
COMPOSE_FILE = docker-compose.yaml

# Define the service name for the application container (e.g., 'app' from docker-compose.yml)
APP_SERVICE = gateway

# Default target when 'make' is run without arguments
.PHONY: default
default: up

# ------------------------------------
# BASIC LIFECYCLE COMMANDS
# ------------------------------------

.PHONY: up
# Starts the services in detached mode (in the background)
up:
	@echo "Starting Docker Compose services..."
	docker compose -f $(COMPOSE_FILE) up -d

.PHONY: down
# Stops and removes containers, networks, and volumes
down:
	@echo "Stopping and removing Docker Compose services..."
	docker compose -f $(COMPOSE_FILE) down -v

.PHONY: build
# Builds or rebuilds all services' images
build:
	@echo "Building application images..."
	docker compose -f $(COMPOSE_FILE) build --no-

# ------------------------------------
# kubernetes COMMANDS
# ------------------------------------
.PHONY: docker_run_registry
docker_run_registry:
	docker run -d -p 5000:5000 --name registry registry:2


.PHONY: kube_image
build_kube_image:
	@echo "Building application images and pushing to local registry"
	docker build -t gateway:prod ./gateway --no-cache 
	docker start registry 
	docker tag gateway:prod localhost:5000/gateway:prod 
	docker push localhost:5000/gateway:prod

.PHONY: kube_apply
kube_apply:
	kubectl apply -f kube/configmap.yaml
	kubectl apply -f kube/secret.yaml
	kubectl apply -f kube/deployment.yaml
	kubectl apply -f kube/service.yaml

.PHONY: kube_port_forward
kube_port_forward:
	kubectl port-forward svc/gateway-service-clusterip 8000:80



.PHONY: logs
# Follows the logs of all services
logs:
	docker compose -f $(COMPOSE_FILE) logs -f

# ------------------------------------
# APPLICATION-SPECIFIC COMMANDS
# ------------------------------------

.PHONY: shell
# Opens a shell inside the main application container
shell:
	@echo "Opening shell in the $(APP_SERVICE) container..."
	docker compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) /bin/bash

.PHONY: lint
# Runs a custom command (e.g., linting) inside the main application container
lint:
	@echo "Running linting tools..."
	docker compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) flake8 /app

# --- The Consolidated Command ---

# The 'run' target depends on 'down' and 'build' before running 'up'.
# When you run 'make run', Make executes the prerequisite targets in order: down -> build -> up.
run: down build up
	@echo "⚡️ Service stack is up and running. Use 'make logs' to view output"