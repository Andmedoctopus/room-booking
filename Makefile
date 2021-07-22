PROJECT_CODE_PATH = /home/room_booking/room_booking
db-bash:
	docker-compose exec db bash

db-shell:
	docker-compose exec db psql -U room_booking -d room_booking_db

app-bash:
	docker-compose exec app bash

format:
	docker-compose run --rm app sh -c "black ${PROJECT_CODE_PATH} && isort ${PROJECT_CODE_PATH}"

format-check:
	docker-compose run --rm app sh -c "black --check ${PROJECT_CODE_PATH} && isort --check ${PROJECT_CODE_PATH}"

flake8:
	docker-compose run --rm app flake8 ${PROJECT_CODE_PATH}
