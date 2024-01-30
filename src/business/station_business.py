from utils.id_generator import random_id_genrator

class StationBusiness():
    def __init__(self,db):
        self.db = db
    
    def add_station(self,station_name):
        station_id = random_id_genrator()
        self.db.write("INSERT INTO station VALUES(?,?)",(station_id,station_name))
        
    def view_station_list(self):
        station_list = self.db.read("SELECT * from station")
        return station_list