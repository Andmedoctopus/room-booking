db-bash:
	docker-compose exec db bash

db-shell:
	docker-compose exec db psql -U room_booking -d room_booking_db
