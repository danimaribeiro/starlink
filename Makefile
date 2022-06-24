

run-migrations:
	docker compose run web alembic upgrade head


download-data:
	docker compose run web python main.py download-starlink-file


import-data:
	docker compose run web python main.py import-starlink-data


clear-data:
	docker compose run web python main.py clear-data


fetch-satellite-position:
	docker compose run web python main.py fetch-position -s 5eed770f096e590006985610 -t 2021-01-26T02:30:01


closest-satellite:
	docker compose run web python main.py closest-satellite -la -27.686170 -lo -48.499287 -t 2022-06-24T02:30:01
