import click
from flask.cli import with_appcontext
from flask import current_app
import psycopg2

@click.command('import_data')
@with_appcontext
def import_data_command():
    # Assuming you have a connection string to your PostgreSQL database
    db_conn_str = current_app.config['SQLALCHEMY_DATABASE_URI']
    try:
        conn = psycopg2.connect(db_conn_str)
        cursor = conn.cursor()

        # Read SQL file and execute each statement
        with open('db_matkul.sql', 'r') as sql_file:
            cursor.execute(sql_file.read())

        conn.commit()
        cursor.close()
        conn.close()

        click.echo('Data import completed successfully.')
    except Exception as e:
        click.echo('Data import failed.')
        click.echo(str(e))
