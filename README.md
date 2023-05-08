# scheduller_project

This is a project based on python and flask framework.
The installation is simple just clone this repository and use this basic command.

# Requirement and installation

`pip install flask` => for download the flask framework, skip if you already install flask.

`pip install flask_sqlalchemy` => for download sql alchemy to do data model and migrations

`pip install flask_migrate` => for download migration via flask to database

`pip install psycopg2-binary` => only download if you are using postgres

# How to Run and early setup

`python -m flask db init` => for initiation database and will create migrations folder

`python -m flask db migrate` => for migration table to database automatically

`python -m flask db upgrade` => for upgrade if there is change on migrations script

`python -m flask db downgrade` => used downgrade for undo change on migration

`python -m flask run --debug` => for running the flask program and creating the local environment for developing.
