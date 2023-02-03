PROJECT_CODE_PATH = /home/room_booking/room_booking


.PHONY: db-bash
db-bash:
	docker compose exec db bash

.PHONY: db-shell
db-shell:
	docker compose exec db psql -U room_booking -d room_booking_db

.PHONY: app-bash
app-bash:
	docker compose exec app bash

.PHONY: format
format:
	docker compose run --rm app sh -c "black ${PROJECT_CODE_PATH}"

.PHONY: format-check
format-check:
	docker compose run --rm app sh -c "black --check ${PROJECT_CODE_PATH}"

.PHONY: import-check
import-check:
	docker compose run --rm app sh -c "isort --check ${PROJECT_CODE_PATH}"

.PHONY: fix-imports
fix-imports:
	docker compose run --rm app sh -c "autoflake -r --in-place --ignore-init-module-imports --remove-all-unused-imports ${PROJECT_CODE_PATH} && isort ${PROJECT_CODE_PATH}"

.PHONY: flake8
flake8:
	docker-compose run --rm app flake8 ${PROJECT_CODE_PATH}

.PHONY: migrate
migrate:
	docker-compose run --rm app alembic upgrade head

.PHONY: lint
lint: flake8 import-check format-check

.PHONY: format-all
format-all: format fix-imports
