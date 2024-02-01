from utils.password_hasher import hash_password
from models.user import User
from config.queries import Queries
from utils.custom_errors import DataNotFoundError

class AuthBusiness:
    def __init__(self, db):
        self.db = db

    def login_user(self, credentials: dict):
        username, password = credentials.values()
        password = hash_password(password)
        
        user_data = self.db.read(Queries.FETCH_USER, (username,))
        if not user_data:
            raise DataNotFoundError("Incorrrect username or password.")
        
        user_id = user_data[0][0]
        user_status = user_data[0][4]
        user_password = self.db.read(Queries.FETCH_PASSWORD, (user_id,))

        if (not user_data and not user_password) or user_status == "INACTIVE":
            raise DataNotFoundError("Incorrrect username or password.")

        user = User(user_data[0][1], user_data[0][2], user_data[0][3])
        return user
