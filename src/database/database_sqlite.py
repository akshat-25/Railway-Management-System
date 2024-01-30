from database.database_context.database_connection import DatabaseConnection
from typing import List,Tuple

create_tables_sql = '''
CREATE TABLE IF NOT EXISTS train (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    capacity INTEGER,
    general INTEGER,
    sleeper INTEGER,
    ac INTEGER,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS station (
    id INTEGER PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY,
    train_id INTEGER,
    station_id INTEGER,
    arrival_time VARCHAR,
    departure_time VARCHAR,
    day INTEGER,
    sequence_number INTEGER,
    FOREIGN KEY (train_id) REFERENCES train(id),
    FOREIGN KEY (station_id) REFERENCES station(id)
);

CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    username VARCHAR,
    role VARCHAR,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS credential (
    user_id INTEGER PRIMARY KEY,
    hashed_password VARCHAR,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

'''
db_file = "src/database/data.db"

class DatabaseAccess:
    def create_tables(self) -> None:
        with DatabaseConnection(db_file) as connection:
            cursor = connection.cursor()
            cursor.executescript(create_tables_sql)
            
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
        

        

