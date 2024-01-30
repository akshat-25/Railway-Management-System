from time import time
from prettytable import PrettyTable

menu_options = '''
 ---------ADMIN DASHBOARD---------\n
        Choose an option :\n
        1. Add new station
        2. Add new train
        3. View existing trains
        4. Update train details
        5. Delete train 
        6. Schedule a train
        7. View trains for booking
        8. Logout
'''

update_options = '''
  What do you want to update -> 
  1. Train Name
  2. Train Capacity
  3. General Coaches
  4. AC Coaches
  5. Sleeper Coaches

'''

search_options = '''
   Search options ->
   1. Search train by train number
   2. Search by location
'''

def time_input():
    alltimes = input("HH:MM\n").split()
    for time in alltimes:
        hour, min = [int(i) for i in time.split(":")]
        time = f"{hour}:{min}"
    return time

class AdminView():
    def __init__(self,train_controller,station_controller):
        self.train_controller = train_controller
        self.station_controller = station_controller
        
    def menu(self):
        while True:
            user_input = int(input(menu_options))
            match user_input:
                case 1:
                    station_name = input('Enter station name: ')
                    self.station_controller.add_station(station_name)
                case 2:
                    train_name = input('Enter train name: ')
                    capacity = int(input('Enter passenger capacity of train: '))
                    general_coaches = int(input('Enter number of General coaches: '))
                    ac_coaches = int(input('Enter number of AC coaches: '))
                    sleeper_coaches = int(input('Enter number of Sleeper coaches: '))

                    train_info = dict(name = train_name, capacity = capacity, general_coaches = general_coaches, ac_coaches = ac_coaches, sleeper_coaches = sleeper_coaches)
                    self.train_controller.add_train(train_info)
                case 3:
                    train_list = self.train_controller.view_trains()
                    print(train_list)
                case 4:
                    train_list = self.train_controller.view_trains()
                    print(train_list)
                    train_id = int(input('Enter Id of train to update :'))
                    update_field = int(input(update_options))
                    match update_field:
                        case 1:
                            new_name = input('Enter new name of the train: ')
                            train_info = dict(option=1,name=new_name)
                        case 2:
                            new_capacity = int(input('Enter new capacity of the train: '))
                            train_info = dict(option=2,capacity=new_capacity)
                        case 3:
                            new_general_coaches = int(input('Enter new number of general coaches: '))
                            train_info = dict(option=3,general_coaches=new_general_coaches)

                        case 4:
                            new_ac_coaches = int(input('Enter new number of AC coaches: '))
                            train_info = dict(option=4,ac_coaches=new_ac_coaches)
                        case 5:
                            new_sleeper_coaches = int(input('Enter new number of sleeper coaches: '))
                            train_info = dict(option=5,sleeper_coaches=new_sleeper_coaches)

                    self.train_controller.update_train_details(train_id,train_info)
                case 5:
                    train_list = self.train_controller.view_trains()
                    print(train_list)
                    train_id = int(input("Enter train Id to delete: "))
                    self.train_controller.delete_train(train_id)                    
                case 6:
                    train_list = self.train_controller.view_trains()
                    print(train_list)
                    train_id = int(input('Enter train Id to create a schedule: '))
                    station_list = self.station_controller.view_station_list()
                    print(station_list)
                    schedule = []
                    i = 1
                    while True:
                        station_id = int(input("Enter station id: "))
                        print("Enter arrival time: ")
                        arrival_time = time_input()
                        print("Enter departure time: ")
                        departure_time = time_input()
                        day = int(input("Enter day number: "))
                        sequence_number = i
                        i = i+1
                        sub_schedule = (station_id, arrival_time, departure_time, day, sequence_number)
                        schedule.append(sub_schedule)
                        user_input = input("Enter q to quit otherwise press any key: ")
                        if user_input == 'q':
                            break
                    
                    print(schedule)
                    self.train_controller.add_schedule(train_id,schedule)
                case 7:
                    search_option = int(input(search_options))
                    match search_option:
                        case 1:
                            train_number = int(input('Enter train number: '))
                            train_route = self.train_controller.search_train_by_id(train_number)
                            schedule_table = PrettyTable()
                            schedule_table.field_names = ["Station Name", "Arrival Time", "Departure Time", "Day"]                            
                            for schedule in train_route:
                                schedule_table.add_row(schedule[1:5])
                                
                            print(schedule_table)
                            
                        case 2:
                            start = input('Enter start station: ')
                            destination = input('Enter destination: ')
                            
                            fetch_trains = self.train_controller.find_trains_by_location(start,destination)
                            
                            trains = PrettyTable()
                            trains.field_names = ["Train Number", "Train Name", "Start Station Time", "Destination Station Time"]
                            
                            for train in fetch_trains:
                                trains.add_row(train)
                                
                            print(trains)
                            
                            
                    
                case 8:
                    exit()
