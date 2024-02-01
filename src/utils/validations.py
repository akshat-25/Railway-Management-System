import logging
import re
from config.log_prompts.log_config import LogsConfig
from utils.app_decorators import loop
from config.prompts import PromptConfig
from config.app_config import AppConfig
import maskpass
logger = logging.getLogger("validations")


class InputValidations:
   
    @staticmethod
    @loop
    def input_username() -> str:
        username = input(PromptConfig.USERNAME_PROMPT).strip().lower()
        if re.match(AppConfig.REGEX_USERNAME, username):
            return username
        print("Invalid input...")
        logger.info(LogsConfig.LOG_INVALID_INPUT)
        
    @staticmethod
    @loop
    def input_password() -> str:
        password = maskpass.askpass(PromptConfig.PASSWORD_PROMPT).strip()
        if re.match(AppConfig.REGEX_PASSWORD, password):
            return password
        print("Invalid input...")
        logger.info(LogsConfig.LOG_INVALID_INPUT)
        
    @staticmethod
    @loop
    def input_name(name_prompt) -> str:
        name = input(name_prompt)
        if re.match(AppConfig.REGEX_NAME, name):
            return name
        print("Invalid Input..")
        logger.info(LogsConfig.LOG_INVALID_INPUT)
        
    @staticmethod
    @loop
    def input_number(number_prompt) -> str:
        number = input(number_prompt)
        if re.match(AppConfig.REGEX_NUMBER, number):
            return number
        print("Invalid Input..")
        logger.info(LogsConfig.LOG_INVALID_INPUT)
        
        
    @staticmethod
    @loop
    def input_time() -> str:
        time = input(PromptConfig.TIME_PROMPT)
        if re.match(AppConfig.REGEX_TIME, time):
            return time
        print("Invalid Input..")
        logger.info(LogsConfig.LOG_INVALID_INPUT)
