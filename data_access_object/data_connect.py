import psycopg2
import psycopg2.extras
from psycopg2 import Error
from load_db_config import load_config


def connect(load_config):
    try:
        global connection
        global cursor
        config = load_config()
        connection = psycopg2.connect(**config)
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print('Connected to the PostgreSQL server.')
        return cursor
    except (Exception, Error) as error:
        print(error)


def close_connect():
    if connection:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    config = load_config()
    connect(config)
