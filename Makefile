PROJECT_CODE_PATH=/home/room_booking/room_booking
TEST_COMPOSE=docker-compose -f docker-compose.test.yaml -p tests
RUN_APP=run --rm app
COVERAGE_REPORT_PATH=room_booking/.coverage
COVERAGE_REPORT_FLAG=--data-file ${COVERAGE_REPORT_PATH}
COVERAGE_HTML_REPORT_PATH=${PROJECT_CODE_PATH}/htmlcov

.PHONY: build
build:
	docker-compose build

.PHONY: rebuild
rebuild:
	docker-compose down
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: up-app
up-app:
	docker-compose up -d app

.PHONY: up-db
up-db:
	docker-compose up -d db

.PHONY: db-bash
db-bash: up-db
	docker-compose exec db bash

.PHONY: db-shell
db-shell: up-db
	docker-compose exec db psql -U room_booking -d room_booking_db

.PHONY: app-bash
app-bash: up-app
	docker-compose exec app bash

.PHONY: format
format:
	docker-compose ${RUN_APP} sh -c "black ${PROJECT_CODE_PATH}"

.PHONY: format-check
format-check:
	docker-compose ${RUN_APP} sh -c "black --check ${PROJECT_CODE_PATH}"

.PHONY: import-check
import-check:
	docker-compose ${RUN_APP} sh -c "isort --check ${PROJECT_CODE_PATH}"

.PHONY: fix-imports
fix-imports:
	docker-compose ${RUN_APP} sh -c "autoflake -r --in-place --ignore-init-module-imports --remove-all-unused-imports ${PROJECT_CODE_PATH} && isort ${PROJECT_CODE_PATH}"

.PHONY: flake8
flake8:
	docker-compose ${RUN_APP} flake8 ${PROJECT_CODE_PATH}

.PHONY: migrate
migrate:
	docker-compose ${RUN_APP} alembic upgrade head

.PHONY: lint
lint: flake8 import-check format-check

.PHONY: format-all
format-all: format fix-imports

.PHONY: test-build
test-build:
	${TEST_COMPOSE} build

.PHONY: destroy-test
destroy-test:
	${TEST_COMPOSE} down -v

.PHONY: test-migrate
test-migrate:
	${TEST_COMPOSE} ${RUN_APP} alembic upgrade head

.PHONY: test-unit
test-unit:
	${TEST_COMPOSE} ${RUN_APP} coverage run -a ${COVERAGE_REPORT_FLAG} -m pytest tests/unit

.PHONY: test-integration
test-integration:
	${TEST_COMPOSE} ${RUN_APP} coverage run -a ${COVERAGE_REPORT_FLAG} -m pytest tests/integration

.PHONY: tests
tests: test-build test-unit test-integration

.PHONY: test-db-shell
test-db-shell:
	${TEST_COMPOSE} exec db psql -U test -d test_db

.PHONY: test-clean
test-clean:
	${TEST_COMPOSE} down -v

.PHONY: coverage-report
coverage-report:
	${TEST_COMPOSE} ${RUN_APP} coverage report ${COVERAGE_REPORT_FLAG} -m

.PHONY: coverage-report
generate-cov-report:
	${TEST_COMPOSE} ${RUN_APP} coverage html -d ${COVERAGE_HTML_REPORT_PATH} ${COVERAGE_REPORT_FLAG}
