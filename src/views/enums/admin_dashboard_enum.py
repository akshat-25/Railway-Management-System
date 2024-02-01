from enum import Enum

class AdminDashboard(Enum):
    Add_new_station = '1'   
    Add_new_train= '2'
    View_existing_trains= '3'
    Update_train_details= '4'
    Delete_train = '5'
    Schedule_a_train= '6'
    View_trains_for_booking= '7'
    Logout= '8'
    