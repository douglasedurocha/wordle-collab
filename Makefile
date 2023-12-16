.PHONY: install
install:
	poetry install --no-root

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: fmt
fmt:
	poetry run ruff --fix

.PHONY: runserver
runserver:
	poetry run python wordle-collab/manage.py runserver

.PHONY: migrate
migrate:
	poetry run python wordle-collab/manage.py migrate

.PHONY: migrations
migrations:
	poetry run python wordle-collab/manage.py makemigrations

.PHONY: superuser
superuser:
	poetry run python wordle-collab/manage.py createsuperuser

.PHONY: test
test:
	poetry run pytest

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit;
