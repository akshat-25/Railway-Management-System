from utils.id_generator import random_id_genrator

class TrainBusiness():
    def __init__(self,db):
        self.db = db
        
    def add_train(self,train_info: dict):
        train_id = random_id_genrator()
        self.db.write("INSERT INTO train VALUES(?,?,?,?,?,?,?)", (train_id,*tuple(train_info.values()),"ACTIVE"))
        
    def view_trains(self):
        train_list = self.db.read("SELECT * from train")
        return train_list
    
    def update_train_details(self,train_id,train_info: dict):
        
        update_option, new_field = train_info.values()
        
        match update_option:
            case 1: 
                self.db.write("UPDATE train SET name=? WHERE id=?",(new_field,train_id))
            case 2:
                self.db.write("UPDATE train SET capacity=? WHERE id=?",(new_field,train_id))
            case 3:
                self.db.write("UPDATE train SET general=? WHERE id=?",(new_field,train_id))
            case 4:
                self.db.write("UPDATE train SET sleeper=? WHERE id=?",(new_field,train_id))
            case 5:
                self.db.write("UPDATE train SET ac=? WHERE id=?",(new_field,train_id))
    
    def delete_train(self,train_id):
        is_train_exist = self.db.read("SELECT * from train WHERE id=?",(train_id,))
        
        if not is_train_exist:
            raise NameError("Invalid Id....")
        else:
            self.db.write("UPDATE train SET status=? WHERE id=?",("INACTIVE",train_id))
    
    
    def add_schedule(self,train_id,schedule: list):        
        for sub_schedule in schedule:
            schedule_id = random_id_genrator()
            self.db.write("INSERT into schedule VALUES(?,?,?,?,?,?,?)",(schedule_id,train_id,*sub_schedule))
            
    def search_train_by_id(self,train_id):
        train_route = self.db.read("SELECT s.station_id, st.name, s.arrival_time, s.departure_time, s.day, s.sequence_number FROM schedule s JOIN station st ON s.station_id = st.id WHERE s.train_id=?",(train_id,))
        return train_route
    
    def find_trains_by_location(self,start,destination):
        start_station_id = self.db.read("SELECT id from station where name=?",(start,))
        destination_station_id = self.db.read("SELECT id from station where name=?",(destination,))
        
        if start_station_id and destination_station_id:
            start_station_id = start_station_id[0][0]
            destination_station_id = destination_station_id[0][0]
        
        trains = self.db.read("SELECT s1.train_id, t.name, s1.arrival_time, s2.arrival_time FROM schedule s1 JOIN schedule s2 ON s1.train_id = s2.train_id JOIN train t ON s1.train_id = t.id WHERE s1.station_id = ? AND s2.station_id = ? AND s1.sequence_number < s2.sequence_number ",(start_station_id,destination_station_id))
        return trains