run:
	@docker compose up

run_d:
	@docker compose up -d

run_dev:
	@python api/flask/run.py

build:
	@docker compose build --no-cache

stop:
	@docker compose down

logs:
	@docker compose logs

logs_f:
	@docker compose logs -f
