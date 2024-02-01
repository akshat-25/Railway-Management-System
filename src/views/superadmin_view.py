from config.prompts import PromptConfig
from utils.validations import InputValidations

class SuperAdminView:
    def __init__(self,controller):
        self.controller = controller
        
        
    def menu(self):
       user_input = int(input(PromptConfig.SUPERADMIN_PROMPT))
       match user_input:
           case 1:
               name = input(PromptConfig.ADMIN_NAME)
               username = InputValidations.input_username()
               password = InputValidations.input_password()
               user_info = dict(name = name, username = username, password = password)
               self.controller.add_new_admin(user_info)  
           case 2:
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
           case 3:
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
               admin_id = InputValidations.input_number(PromptConfig.SELECT_ADMIN)
               print(PromptConfig.SUPERADMIN_UPDATE_PROMPT)
               update_option = int(input())
               if update_option == 1:
                   new_name = InputValidations.input_name(PromptConfig.ADMIN_NEW_NAME)
                   user_info = dict(id = admin_id,field = 1, name = new_name)
               elif update_option == 2:
                   new_username = InputValidations.input_username()
                   user_info = dict(id = admin_id,field = 2,username = new_username)
                   
               self.controller.update_admin_details(user_info)
           case 4: 
               admin_list = self.controller.fetch_admin_details()
               print(admin_list)
               admin_id = InputValidations.input_number(PromptConfig.ADMIN_ID_TO_DELETE)
               self.controller.delete_admin(admin_id)
                    