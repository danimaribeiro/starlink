

run-migrations:
	docker compose run web alembic upgrade head


download-data:
	docker compose run web python main.py download-starlink-file


import-data:
	docker compose run web python main.py import-starlink-data