class StationController():
    def __init__(self,business):
        self.business = business
        
    def add_station(self,station_name):
        self.business.add_station(station_name)
        
    def view_station_list(self):
        station_list = self.business.view_station_list()
        return station_list