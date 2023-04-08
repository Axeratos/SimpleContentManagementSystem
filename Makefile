.PHONY: run-project
run-project:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
  COMPOSE_PROFILES=full_run \
  docker-compose up --build


.PHONY: run-local
run-local:
		@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
  COMPOSE_PROFILES=local_dev \
  docker-compose up --build


.PHONY: docker-purge
docker-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
  docker-compose \
  down --volumes --remove-orphans --rmi local --timeout 0
