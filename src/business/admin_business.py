from utils.password_hasher import hash_password
from utils.id_generator import random_id_genrator


class AdminBusiness:
    def __init__(self,db):
        self.db = db
    
    def add_new_admin(self,user_info: dict):
        name, username, password = user_info.values()
        is_username_exist = self.db.read("SELECT * from user WHERE username= ?",(username,))
        if not is_username_exist:
            password = hash_password(password)
            user_id = random_id_genrator()
            self.db.write("INSERT INTO user VALUES(?,?,?,?,?)",(user_id,name,username,"ADMIN","ACTIVE"))
            self.db.write("INSERT INTO credential VALUES(?,?)",(user_id,password))
        else:
            print('Username already exists...')
    
    def delete_admin(self,admin_id):
        user_info = self.db.read("SELECT * from user WHERE id= ?",(admin_id,))
        self.db.write("INSERT OR REPLACE INTO user VALUES(?,?,?,?,?)",(admin_id,user_info[0][1],user_info[0][2],user_info[0][3],"INACTIVE"))
        self.db.write("DELETE from credential where user_id= ?",(admin_id,))
    
    def update_admin_details(self,user_info):
        admin_id , update_field, new_field = user_info.values()
        
        old_user_info = self.db.read("SELECT * from user WHERE id= ?",(admin_id,))
        if update_field == 1:
            self.db.write("UPDATE user SET status =? WHERE id=?",(admin_id,new_field,old_user_info[0][2],old_user_info[0][3],old_user_info[0][4]))
        else:
            self.db.write("INSERT OR REPLACE INTO user VALUES(?,?,?,?,?)",(admin_id,old_user_info[0][1],new_field,old_user_info[0][3],old_user_info[0][4]))
    
    def fetch_admin_details(self):
        admin_list = self.db.read('SELECT * FROM user WHERE role=?',('ADMIN',))
        return admin_list