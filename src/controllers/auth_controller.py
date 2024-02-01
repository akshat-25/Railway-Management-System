from utils.app_decorators import error_handler
import logging
from config.log_prompts.log_config import LogsConfig

logger = logging.getLogger("auth_controller")

class AuthController:
    def __init__(self, business):
        self.business = business

    def login(self, credentials: dict):
        user = self.business.login_user(credentials)
        logger.info(LogsConfig.LOG_ADMIN_LOGIN)
        return user
