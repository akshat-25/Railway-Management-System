from getpass import getpass
from views.superadmin_view import SuperAdminView
from views.admin_view import AdminView
from controllers.admin_controller import AdminController
from business.admin_business import AdminBusiness
from database.database_sqlite import DatabaseAccess
from controllers.admin_controller import AdminController
from controllers.station_controller import StationController
from controllers.train_controller import TrainController
from business.train_business import TrainBusiness
from business.station_business import StationBusiness
from config.prompts import PromptConfig


db = DatabaseAccess()
admin_business = AdminBusiness(db)
admin_controller = AdminController(admin_business)
train_business = TrainBusiness(db)
train_controller = TrainController(train_business)
station_business = StationBusiness(db)
station_controller = StationController(station_business)

class AuthView():
    def __init__(self,controller):
        self.controller = controller
        
    def login(self):
        username = input(PromptConfig.USERNAME_PROMPT)
        password = getpass(PromptConfig.PASSWORD_PROMPT)
        credentials = dict(username = username ,password = password)
        user = self.controller.login(credentials)
        if user.role == PromptConfig.SUPERADMIN_ROLE_PROMPT:
            print(PromptConfig.WELCOME_SUPERADMIN_PROMPT)
            superadmin_dashboard = SuperAdminView(admin_controller) 
            superadmin_dashboard.menu()
        else:
            print(PromptConfig.WELCOME_ADMIN_PROMPT)
            admin_dashboard = AdminView(train_controller,station_controller)
            admin_dashboard.menu()