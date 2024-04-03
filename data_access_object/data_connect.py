import psycopg2
import psycopg2.extras
from psycopg2 import Error
from load_db_config import load_db_config

global connection
global cursor


def connect(load_db_config):
    try:
        db_config = load_db_config
        db_connection = psycopg2.connect(**db_config)
        db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return db_cursor
    except (Exception, Error) as error:
        print(error)


def close_connect():
    if connection:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    config = load_db_config()
    connect(config)
