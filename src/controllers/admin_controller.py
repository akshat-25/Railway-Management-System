import logging
from config.log_prompts.log_config import LogsConfig

logger = logging.getLogger("admin_controller")


class AdminController:
    def __init__(self, business):
        self.business = business

    def add_new_admin(self, user_info: dict):
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)
        self.business.add_new_admin(user_info)
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)

    def delete_admin(self, admin_id):
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)

        self.business.delete_admin(admin_id)
        logger.info(LogsConfig.LOG_ADMIN_DELETED)

    def update_admin_details(self, user_info):
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)

        self.business.update_admin_details(user_info)
        logger.info(LogsConfig.LOG_ADMIN_UPDATE)

    def fetch_admin_details(self):
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)

        admin_list = self.business.fetch_admin_details()
        logger.info(LogsConfig.LOG_ADMIN_READ)

        return admin_list
