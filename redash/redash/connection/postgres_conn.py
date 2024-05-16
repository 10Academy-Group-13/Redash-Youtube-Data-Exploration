import psycopg2
from sqlalchemy import create_engine

class ConnectToPostgres:
    def __init__(self):
        db_params = {
            'host': 'localhost',
            'user': 'postgres',
            'port': '15432',
            'database': 'youtube_datas'
        }

        try:
            # Create a PostgreSQL database engine
            self.engine = create_engine(f"postgresql+psycopg2://{db_params['user']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")
        except Exception as error:
            raise Exception("Cannot connect to the database. Please check your connection details.")

    def get_engine(self):
        return self.engine