import sqlite3
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

class DatabaseCreator:
    def __init__(self, data_path: Path, db_dirpath: Path, database_filename:str):
        self.data_path = data_path
        self.db_dirpath = db_dirpath
        self.db_dirpath.mkdir(parents=True, exist_ok=True)
        self.database_file_path = self.db_dirpath / database_filename
        self.engine = create_engine(f'sqlite:///{self.database_file_path.as_posix()}')

        # Create an empty SQLite database if it does not exist
        if not self.database_file_path.exists():
            conn = sqlite3.connect(self.database_file_path)
            conn.close()

    def create_database_from_csv(self):
        for csv_file in self.data_path.glob("*.csv"):
            table_name = csv_file.stem
            df = pd.read_csv(csv_file)
            df.to_sql(
                table_name,
                con=self.engine,
                if_exists='replace',
                index=False
            )

        message = f"Empty SQLite database successfully crated at {self.database_file_path.as_posix()}"

        return message