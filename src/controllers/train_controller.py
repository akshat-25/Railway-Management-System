class TrainController():
    def __init__(self,business):
        self.business = business
        
    def add_train(self,train_info: dict):
        self.business.add_train(train_info)
        
    def view_trains(self):
        train_list = self.business.view_trains()
        return train_list
    
    def update_train_details(self,train_id,train_info: dict):
        self.business.update_train_details(train_id,train_info)
        
    def delete_train(self,train_id):
        self.business.delete_train(train_id)
        
    def add_schedule(self,train_id,schedule: list):
        self.business.add_schedule(train_id,schedule)
        
    def search_train_by_id(self,train_id):
        train_route = self.business.search_train_by_id(train_id)
        return train_route
    
    def find_trains_by_location(self,start,destination):
        train_list = self.business.find_trains_by_location(start,destination)
        return train_list