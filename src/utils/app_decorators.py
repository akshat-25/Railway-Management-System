import functools
from utils.custom_errors import DataNotFoundError, AlreadyExistError, GeneralError, InvalidInputError
import logging

logger = logging.getLogger("errors")


def loop(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        while True:
            result = func(*args, **kwargs)
            if result:
                return result

    return wrapper


def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DataNotFoundError as e:
            logger.exception(e)
            print(e)
        except AlreadyExistError as e:
            logger.exception(e)
            print(e)
        except GeneralError as e:
            logger.exception(e)
            print(e)
        except InvalidInputError as e:
            logger.exception(e)
            print(e)

    return wrapper
