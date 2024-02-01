from utils.password_hasher import hash_password
from utils.id_generator import random_id_genrator
from config.queries import Queries

class AdminBusiness:
    def __init__(self, db):
        self.db = db

    def add_new_admin(self, user_info: dict):
        name, username, password = user_info.values()
        is_username_exist = self.db.read(Queries.FETCH_USER, (username,))
        if not is_username_exist:
            password = hash_password(password)
            user_id = random_id_genrator()
            self.db.write(
                Queries.ADD_USER, (user_id, name, username, "ADMIN", "ACTIVE")
            )
            self.db.write(Queries.ADD_CREDENTIALS, (user_id, password))
        else:
            print("Username already exists...")

    def delete_admin(self, admin_id):
        user_info = self.db.read(Queries.FETCH_USER_FROM_ID, (admin_id,))
        self.db.write(
            Queries.DELETE_USER,
            (admin_id, user_info[0][1], user_info[0][2], user_info[0][3], "INACTIVE"),
        )
        self.db.write(Queries.DELETE_CREDENTIALS, (admin_id,))

    def update_admin_details(self, user_info: dict):
        field_mapping = {1: "name", 2: "username"}

        admin_id, update_field, new_field = user_info.values()

        field_name = field_mapping.get(update_field)

        if field_name:
            query = f"UPDATE user SET f{field_name}= ? where id=?"
            params = (new_field, admin_id)
            self.db.write(query, params)

    def fetch_admin_details(self):
        admin_list = self.db.read(Queries.FETCH_ADMIN_LIST, ("ADMIN",))
        return admin_list