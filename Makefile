# Variables
FLASK = python -m flask	--app main
POSTMAN = python -m flask2postman
# APP_ENTRY_POINT = main.py

# Targets
.PHONY: init migrate import_data run upgrade downgrade
# the default command to run with the make command
default: import_data run
# command to run the app
run:
	$(FLASK) run --debug
# command to download the dependencies
init:
	pip install flask flask_sqlalchemy flask_migrate psycopg2-binary flask2postman pandas WTForms
# command to create the database
migrate:
	$(FLASK) db migrate
# command to upgrade the database
upgrade:
	$(FLASK) db upgrade
# command to downgrade the database
downgrade:
	$(FLASK) db downgrade
# command to import the data
import_data:
	$(FLASK) import_data
postman:
	$(POSTMAN) main.app > sp-postman.json