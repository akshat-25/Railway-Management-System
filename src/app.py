from views.enums.start_menu_enum import Options
from database.database_sqlite import DatabaseAccess
from business.auth_business import AuthBusiness
from controllers.auth_controller import AuthController
from views.auth_view import AuthView
from utils.initializer import Initializer
from config.app_config import AppConfig
from config.prompts import PromptConfig
from config.log_prompts.log_config import LogsConfig
from utils.custom_errors import InvalidInputError
from utils.app_decorators import (
    error_handler,
    loop
)
import logging

db = DatabaseAccess()
business = AuthBusiness(db)
controller = AuthController(business)

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename=AppConfig.LOG_LOCATION,
)

logger = logging.getLogger("main")

@loop
@error_handler
def user_input_handler():
    print(PromptConfig.AUTH_PROMPT)
    user_input = input()
       
    if user_input == str(Options.Login.value):
        auth = AuthView(controller)
        auth.login()
    elif user_input == str(Options.Exit.value):
        logger.info(LogsConfig.LOG_APPLICATION_EXITING)
        exit()
    else:
        raise InvalidInputError("Invalid input...")

def start_menu():
    db.create_tables()
    PromptConfig.load()
    LogsConfig.load()
    initialize_app = Initializer(db)
    initialize_app.create_super_admin()
    print(PromptConfig.STARTING_APPLICATION)
    logger.info(LogsConfig.LOG_APPLICATION_STARTING)
    user_input_handler()

start_menu()