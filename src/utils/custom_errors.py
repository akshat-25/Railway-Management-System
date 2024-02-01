class DataNotFoundError(Exception):
    def __init__(self,message):
        super().__init__(f'{message}')
        
class AlreadyExistError(Exception):
    def __init__(self,message):
        super().__init__(f'{message}')
        
class GeneralError(Exception):
    def __init__(self,message):
        super().__init__(f'{message}')
        
class InvalidInputError(Exception):
    def __init__(self,message):
        super().__init__(f'{message}')