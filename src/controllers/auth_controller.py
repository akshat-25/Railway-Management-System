class AuthController:
    
    def __init__(self,business):
        self.business = business
        
    def login(self,credentials: dict):
        user = self.business.login_user(credentials)
        return user
    
    
   