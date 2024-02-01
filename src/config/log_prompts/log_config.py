import yaml
from config.app_config import AppConfig

class LogsConfig:
    
    LOG_INVALID_INPUT = None
    LOG_APPLICATION_STARTING = None
    LOG_SUPERADMIN_LOGIN = None
    LOG_ADMIN_LOGIN = None
    LOG_ADMIN_LOGOUT = None
    PROVIDE_ROLE_BASED_ACCESS = None
    LOG_ADMIN_ADDED: None
    LOG_ADMIN_DELETED: None
    LOG_ADMIN_UPDATE: None
    LOG_ADMIN_READ:   None
    LOG_TRAIN_ADDED:  None
    LOG_TRAIN_DELETED: None
    LOG_TRAIN_READ:   None
    LOG_TRAIN_UPDATED: None
    LOG_STATION_ADDED: None       
    LOG_STATION_LIST_FETCHED: None
    LOG_SCHEDULE_ADDED = None
    LOG_SCHEDULE_ALREADY_EXIST = None 
    LOG_APPLICATION_EXITING = None
    
    @classmethod
    def load(cls):
        with open(AppConfig.LOG_FILE_LOCATION,"r") as file:
            data = yaml.safe_load(file)
            
            cls.LOG_INVALID_INPUT = data["LOG_INVALID_INPUT"]
            cls.LOG_APPLICATION_STARTING = data["LOG_APPLICATION_STARTING"]
            cls.LOG_SUPERADMIN_LOGIN = data["LOG_SUPERADMIN_LOGIN"]
            cls.LOG_ADMIN_LOGIN = data["LOG_ADMIN_LOGIN"]
            cls.LOG_ADMIN_LOGOUT = data["LOG_ADMIN_LOGOUT"]
            cls.PROVIDE_ROLE_BASED_ACCESS = data["PROVIDE_ROLE_BASED_ACCESS"]
            cls.LOG_ADMIN_ADDED = data["LOG_ADMIN_ADDED"]
            cls.LOG_ADMIN_DELETED = data["LOG_ADMIN_DELETED"]
            cls.LOG_ADMIN_UPDATE = data["LOG_ADMIN_UPDATE"]
            cls.LOG_ADMIN_READ =   data["LOG_ADMIN_READ"]
            cls.LOG_TRAIN_ADDED =  data["LOG_TRAIN_ADDED"]
            cls.LOG_TRAIN_DELETED = data["LOG_TRAIN_DELETED"]
            cls.LOG_TRAIN_READ =   data["LOG_TRAIN_READ"]
            cls.LOG_TRAIN_UPDATED = data["LOG_TRAIN_UPDATED"]
            cls.LOG_STATION_ADDED = data["LOG_STATION_ADDED"]       
            cls.LOG_STATION_LIST_FETCHED: data["LOG_STATION_LIST_FETCHED"]
            cls.LOG_SCHEDULE_ADDED = data["LOG_SCHEDULE_ADDED"]
            cls.LOG_SCHEDULE_ALREADY_EXIST = data["LOG_SCHEDULE_ALREADY_EXIST"]
            cls.LOG_APPLICATION_EXITING = data["LOG_APPLICATION_EXITING"]
            
            