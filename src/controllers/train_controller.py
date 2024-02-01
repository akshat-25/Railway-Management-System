from utils.app_decorators import error_handler
import logging
from config.log_prompts.log_config import LogsConfig

logger = logging.getLogger("train_controller")

class TrainController:
    def __init__(self, business):
        self.business = business
        
    @error_handler
    def add_train(self, train_info: dict):
        self.business.add_train(train_info)
        logger.info(LogsConfig.LOG_TRAIN_ADDED)
        
    @error_handler
    def view_trains(self):
        train_list = self.business.view_trains()
        logger.info(LogsConfig.LOG_TRAIN_READ)
        return train_list

    @error_handler
    def update_train_details(self, train_id, train_info: dict):
        self.business.update_train_details(train_id, train_info)
        logger.info(LogsConfig.LOG_TRAIN_UPDATED)

    
    @error_handler
    def delete_train(self, train_id):
        self.business.delete_train(train_id)
        logger.info(LogsConfig.LOG_TRAIN_DELETED)
        
    @error_handler
    def scheduled_train(self,train_id):
       
        return self.business.scheduled_train(train_id)
    
    @error_handler
    def add_schedule(self, train_id, schedule: list):
        self.business.add_schedule(train_id, schedule)
        logger.info(LogsConfig.LOG_SCHEDULE_ADDED)

    @error_handler
    def search_train_by_id(self, train_id):
        train_route = self.business.search_train_by_id(train_id)
        logger.info(LogsConfig.LOG_TRAIN_READ)
        return train_route

    @error_handler
    def find_trains_by_location(self, start, destination):
        train_list = self.business.find_trains_by_location(start, destination)
        logger.info(LogsConfig.LOG_TRAIN_READ)
        return train_list
