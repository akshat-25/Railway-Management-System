from utils.id_generator import random_id_genrator
from config.queries import Queries
import sqlite3
from utils.custom_errors import (
    DataNotFoundError,
    AlreadyExistError,
    GeneralError
)


class TrainBusiness:
    def __init__(self, db):
        self.db = db

    def add_train(self, train_info: dict):
        train_id = random_id_genrator()
        train_name = train_info.get("train_name")
        is_name_same = self.db.read('SELECT * from train WHERE name= ?',(train_name,))
        
        if not is_name_same:
            raise AlreadyExistError("Train name already exist!")
        
        try:
            self.db.write(
                Queries.ADD_TRAIN, (train_id, *tuple(train_info.values()), "ACTIVE")
                )
        except sqlite3.IntegrityError as e:
            raise AlreadyExistError(e)
        
       
    def view_trains(self):
        try:
            train_list = self.db.read(Queries.SELECT_FROM_TRAIN)
        except Exception as e:
            raise GeneralError("An error has occured...")
        else:
            return train_list

    def update_train_details(self, train_id, train_info: dict):
        field_mapping = {1: "name", 2: "capacity", 3: "general", 4: "sleeper", 5: "ac"}

        update_option, new_field = train_info.values()

        field_name = field_mapping.get(update_option)

        if field_name:
            query = f"UPDATE train SET {field_name}= ? WHERE id=?"
            params = (new_field, train_id)
            self.db.write(query, params)
        else:
            raise DataNotFoundError("Field not found")

    def delete_train(self, train_id):
        is_train_exist = self.db.read(Queries.SELECT_TRAIN, (train_id,))

        if not is_train_exist:
            raise DataNotFoundError("Train not found")
        try:
            self.db.write(Queries.DELETE_TRAIN, ("INACTIVE", train_id))
        except:
            raise GeneralError("An error has occured...")

    def scheduled_train(self,train_id):
        is_train_exist = self.db.read("SELECT * from schedule where train_id =?",(train_id,))
        
        if is_train_exist:
            raise AlreadyExistError("Schedule already exist!")
        else:
            return False
      
        
    def add_schedule(self, train_id, schedule: list):
        is_train_exist = self.db.read("SELECT * from schedule where train_id =?",(train_id,))
        
        if not is_train_exist:
            raise AlreadyExistError("Schedule already exist!")

        for sub_schedule in schedule:
            schedule_id = random_id_genrator()
            self.db.write(Queries.ADD_SCHEDULE, (schedule_id, train_id, *sub_schedule))

    def search_train_by_id(self, train_id):
        
        train_route = self.db.read(Queries.SEARCH_TRAIN_BY_ID, (train_id,))
        
        if not train_route:
            raise DataNotFoundError("No train found.")
              
        sorted_data = sorted(train_route, key=lambda x: x[-1])

        return sorted_data

    def find_trains_by_location(self, start, destination): 
        start_station_id = self.db.read(Queries.STATION_ID, (start,))
        destination_station_id = self.db.read(Queries.STATION_ID, (destination,))
        if start_station_id and destination_station_id:
            start_station_id = start_station_id[0][0]
            destination_station_id = destination_station_id[0][0]
            trains = self.db.read(
                Queries.SEARCH_TRAIN_BY_LOCATION, (start_station_id, destination_station_id)
                )
            return trains
        else:
            raise DataNotFoundError("No trains available")
        
            
    
            