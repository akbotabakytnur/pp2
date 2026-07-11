import psycopg2
from config import load_config

def connect():
    try:
        config = load_config()

        conn = psycopg2.connect(
            dbname=config["DB_NAME"],
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            host=config["DB_HOST"],
            port=config["DB_PORT"]
        )

        return conn

    except Exception as e:
        print(e)
        return None