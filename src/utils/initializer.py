import os
from utils.id_generator import random_id_genrator
from utils.password_hasher import hash_password
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

class Initializer():
    def __init__(self,db):
        self.db = db
        
    def create_super_admin(self) -> None:
        is_superadmin_exists = self.db.read('SELECT * from user WHERE role= ?',("SUPERADMIN",))
        
        if not is_superadmin_exists :
            superadmin_id = random_id_genrator()
            superadmin_name = os.getenv('SUPER_ADMIN_NAME')
           
            superadmin_username = os.getenv('SUPER_ADMIN_USERNAME')
            password = os.getenv('SUPER_ADMIN_PASSWORD')
            superadmin_password = hash_password(password)
            
            self.db.write('INSERT INTO user VALUES(?,?,?,?,?)',(superadmin_id,superadmin_name,superadmin_username,"SUPERADMIN","ACTIVE"))
            self.db.write('INSERT INTO credential VALUES(?,?)', (superadmin_id, superadmin_password))