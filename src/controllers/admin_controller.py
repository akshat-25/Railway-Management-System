
class AdminController:
    def __init__(self,business):
        self.business = business
    
    def add_new_admin(self,user_info: dict):
        self.business.add_new_admin(user_info)
        
    def delete_admin(self,admin_id):
        self.business.delete_admin(admin_id)
    
    def update_admin_details(self,user_info):
        self.business.update_admin_details(user_info)
    
    def fetch_admin_details(self):
        admin_list = self.business.fetch_admin_details()
        return admin_list   