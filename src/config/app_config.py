class AppConfig:
    LOG_FILE_LOCATION = r"src\config\log_prompts\log_config.yaml"
    LOG_LOCATION = r"logs.log"


# regex patterns
    REGEX_USERNAME = r"^([A-Za-z0-9]{3,20}.\s*)"
    REGEX_PASSWORD = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"
    REGEX_NAME = r"([A-Za-z])"
    REGEX_NUMBER = r"^([0-9])"
    REGEX_TIME = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"