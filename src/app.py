from views.options_enum.start_menu_enum import Options
from database.database_sqlite import DatabaseAccess
from business.auth_business import AuthBusiness
from controllers.auth_controller import AuthController
from views.auth_view import AuthView
from utils.initializer import Initializer

db = DatabaseAccess()
business = AuthBusiness(db)
controller = AuthController(business)

def start_menu():
    db.create_tables()
    initialize_app = Initializer(db)
    initialize_app.create_super_admin()
    print('---------- Railway Management System ----------\n')
    while True:
        print('Choose an option :')
        print('1. Login')
        print('2. Exit')
        user_input = int(input())

        if(user_input == Options.Login.value):
            auth = AuthView(controller)
            auth.login()
        else:
            exit()

start_menu()