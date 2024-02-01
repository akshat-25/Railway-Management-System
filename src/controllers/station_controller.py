from utils.app_decorators import error_handler
import logging
from config.log_prompts.log_config import LogsConfig

logger = logging.getLogger("station_controller")

class StationController:
    def __init__(self, business):
        self.business = business

    def add_station(self, station_name):
        self.business.add_station(station_name)
        logger.info(LogsConfig.LOG_STATION_ADDED)

    def view_station_list(self):
        station_list = self.business.view_station_list()
        logger.info(LogsConfig.LOG_STATION_LIST_FETCHED)
        return station_list
