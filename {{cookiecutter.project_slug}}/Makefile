# === GLOBAL VARIABLES ======================================================
PROJECT_SRC={{cookiecutter.project_slug}}
DOCKER_IMAGE={{cookiecutter.project_image}}
DOCKER_COMPOSE_APP={{cookiecutter.project_slug}}
TEST_COVERAGE_PERCENTAGE=80
TAG=latest
BASE_IMAGE=
EXTRA_ARGS=

# === COMMANDS ==============================================================
# Installs the Python dependencies
install:
	pip3 install -r requirements.txt

# Installs the dev Python dependencies
install-dev:
	echo "Installing DEV dependencies"
	pip3 install -e ".[dev]"

download:
	pip3 download -r requirements.txt

# Installs the dev Python dependencies
download-dev:
	echo "Installing DEV dependencies"
	pip3 download ".[dev]"

# Runs the Unit tests
unit:
	python3 -m pytest tests/unit -v

# Runs the component tests
component:
	python -m pytest tests/component -v

# Tests coverage check and reports
coverage:
	coverage run -m pytest tests -v
	coverage report --fail-under=$(TEST_COVERAGE_PERCENTAGE)

# Runs all the QA tooling
qa: unit component coverage

# Runs all the QA tooling in the dev docker container
docker-qa: docker-qa-build
	docker-compose run --rm $(DOCKER_COMPOSE_APP) make qa

# Locks the dependency file (from setup.py)
freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-annotate --no-emit-index-url --output-file requirements.txt setup.py --cache-dir /tmp/pip-compile-cache

# Upgrades the dependencies lock file
freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-annotate --no-emit-index-url --output-file requirements.txt --upgrade setup.py --cache-dir /tmp/pip-compile-cache

# Gets a shell inside the development container (note: You can sudo this)
docker-shell: docker-qa-build
	docker-compose run --rm $(DOCKER_COMPOSE_APP) bash

#build an image for the compose tag.
docker-qa-build: TAG=latest-staging
docker-qa-build: EXTRA_ARGS=--build-arg INSTALL_SUFFIX="-dev"
docker-qa-build: docker-build
# Alias for docker-shell
shell:
	make docker-shell

# Builds a production docker container
docker-build-production:
	docker build . -t $(DOCKER_IMAGE):latest-production

# Builds a production docker container
docker-build:
	docker build --force-rm $(EXTRA_ARGS) --build-arg SSH_PRIVATE_KEY="$$(cat $(SSH_KEY))" . -t $(BASE_IMAGE)$(DOCKER_IMAGE):$(TAG)

docker-push: docker-build
	docker push $(BASE_IMAGE)$(DOCKER_IMAGE):$(TAG)

{%- if cookiecutter.docker_compose_external_network != '' %}
network:
# Note: This network is defined externally from docker-compose so it can connect multiple docker-compose.yml files
	docker network inspect {{ cookiecutter.docker_compose_external_network }} >/dev/null 2>&1 || docker network create --driver bridge {{ cookiecutter.docker_compose_external_network }}
{%- endif %}
