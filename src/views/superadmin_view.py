menu_options = '''
 ---------SUPERADMIN DASHBOARD---------\n
        Choose an option :\n
        1. Add new admin
        2. View admin details
        3. Update admin details
        4. Delete admin
'''

class SuperAdminView:
    def __init__(self,controller):
        self.controller = controller
        
        
    def menu(self):
       user_input = int(input(menu_options))
       match user_input:
           case 1:
               name = input('Enter name of the admin: ')
               username = input('Enter username: ')
               password = input('Enter password: ')
               user_info = dict(name = name, username = username, password = password)
               self.controller.add_new_admin(user_info)  
           case 2:
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
           case 3:
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
               admin_id = int(input('Enter Id of admin from the above list :'))
               print('What do you want to update ?')
               print('1. Name')
               print('2. Username')
               update_option = int(input())
               if update_option == 1:
                   new_name = input('Enter new name of admin:')
                   user_info = dict(id = admin_id,field = 1, name = new_name)
               elif update_option == 2:
                   new_username = input('Enter new username of the admin: ')
                   user_info = dict(id = admin_id,field = 2,username = new_username)
                   
               self.controller.update_admin_details(user_info)
           case 4: 
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
               admin_id = int(input('Enter Id of admin to delete from the above list :'))
               self.controller.delete_admin(admin_id)
                
       
       
       