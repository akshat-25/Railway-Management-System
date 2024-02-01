from database.database_context.database_connection import DatabaseConnection
from typing import List,Tuple
from config.queries import Queries


db_file = "src/database/data.db"

class DatabaseAccess:
    def create_tables(self) -> None:
        with DatabaseConnection(db_file) as connection:
            cursor = connection.cursor()
            cursor.executescript(Queries.CREATE_ALL_TABLES)
            
    def write(self,query: str,data: Tuple) -> None:
        with DatabaseConnection(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(query,data)
    
    
    def read(self, query: str,data: Tuple|None = None) -> List[Tuple]:
        with DatabaseConnection(db_file) as connection:
            cursor = connection.cursor()
            if not data:
                cursor.execute(query)
            else:
                cursor.execute(query,data)
            return cursor.fetchall()
        

        

