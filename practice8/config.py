import psycopg2
from config import load_config


def connect():
    config = load_config()

    try:
        conn = psycopg2.connect(**config)
        print("Connected to the PostgreSQL server.")
        return conn

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return None