# Variables
FLASK = python -m flask	--app main
# APP_ENTRY_POINT = main.py

# Targets
.PHONY: init migrate import_data run upgrade downgrade

default: import_data run

run:
	$(FLASK) run --debug

init:
	pip install flask flask_sqlalchemy flask_migrate psycopg2-binary

migrate:
	$(FLASK) db init
	$(FLASK) db migrate

upgrade:
	$(FLASK) db upgrade

downgrade:
	$(FLASK) db downgrade

import_data:
	$(FLASK) import_data
