class Queries:
    CREATE_ALL_TABLES = '''
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

# Train Queries
    ADD_TRAIN = "INSERT INTO train VALUES(?,?,?,?,?,?,?)"
    SELECT_FROM_TRAIN = "SELECT * from train"
    SELECT_TRAIN = "SELECT * from train WHERE id=?"
    DELETE_TRAIN = "UPDATE train SET status=? WHERE id=?"
    SEARCH_TRAIN_BY_ID = "SELECT s.station_id, st.name, s.arrival_time, s.departure_time, s.day, s.sequence_number FROM schedule s JOIN station st ON s.station_id = st.id WHERE s.train_id=?"
    SEARCH_TRAIN_BY_LOCATION = "SELECT s1.train_id, t.name, s1.arrival_time, s2.arrival_time FROM schedule s1 JOIN schedule s2 ON s1.train_id = s2.train_id JOIN train t ON s1.train_id = t.id WHERE s1.station_id = ? AND s2.station_id = ? AND s1.sequence_number < s2.sequence_number"
    
# Schedule Queries
    ADD_SCHEDULE = "INSERT into schedule VALUES(?,?,?,?,?,?,?)"
    
    
# Station Queries
    STATION_ID = "SELECT id from station where name=?"
    ADD_STATION = "INSERT INTO station VALUES(?,?)"
    FETCH_STATION = "SELECT * from station"
    
# Admin Queries
    FETCH_USER = "SELECT * from user WHERE username= ?"
    ADD_USER = "INSERT INTO user VALUES(?,?,?,?,?)"
    FETCH_USER_FROM_ID = "SELECT * from user WHERE id= ?"
    DELETE_USER = "INSERT OR REPLACE INTO user VALUES(?,?,?,?,?)"
    FETCH_ADMIN_LIST = 'SELECT * FROM user WHERE role=?'
    
# Credentials Queries
    ADD_CREDENTIALS = "INSERT INTO credential VALUES(?,?)"
    DELETE_CREDENTIALS = "DELETE from credential where user_id= ?"
    FETCH_PASSWORD = "SELECT hashed_password from credential WHERE user_id= ?"