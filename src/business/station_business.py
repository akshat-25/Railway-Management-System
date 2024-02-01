from utils.id_generator import random_id_genrator
from config.queries import Queries


class StationBusiness:
    def __init__(self, db):
        self.db = db

    def add_station(self, station_name):
        station_id = random_id_genrator()
        self.db.write(Queries.ADD_STATION, (station_id, station_name))

    def view_station_list(self):
        station_list = self.db.read(Queries.FETCH_STATION)
        return station_list
