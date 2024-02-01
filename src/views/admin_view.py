from prettytable import PrettyTable
from config.prompts import PromptConfig
from views.enums.admin_dashboard_enum import AdminDashboard
from views.enums.admin_update_enum import AdminUpdate
from views.enums.admin_search_enum import AdminSearch
from utils.validations import InputValidations

def get_train_details_input():
    train_name = InputValidations.input_name(PromptConfig.TRAIN_NAME_PROMPT)
    capacity = InputValidations.input_number(PromptConfig.PASSENGER_CAPACITY_PROMPT)
    general_coaches = InputValidations.input_number(PromptConfig.GENERAL_COACH_PROMPT)
    ac_coaches = InputValidations.input_number(PromptConfig.AC_COACH_PROMPT)
    sleeper_coaches = InputValidations.input_number(PromptConfig.SLEEPER_COACH_PROMPT)
    return dict(
        name=train_name,
        capacity=capacity,
        general_coaches=general_coaches,
        ac_coaches=ac_coaches,
        sleeper_coaches=sleeper_coaches,
    )


def view_train(train_list):
    if train_list:
        train_table = PrettyTable()
        train_table.field_names = [
            "Train id",
            "Train Name",
            "Passenger Capacity",
            "General Coaches",
            "Sleeper Coaches",
            "AC Coaches",
        ]
        for train in train_list:
            train_table.add_row(train[:6])
        print(train_table)


def time_input():
    alltimes = InputValidations.input_time().split()
    for time in alltimes:
        hour, minute = [int(i) for i in time.split(":")]
        time_detail = f"{hour}:{minute}"
    return time_detail


class AdminView:
    def __init__(self, train_controller, station_controller):
        self.train_controller = train_controller
        self.station_controller = station_controller
    
    
    def menu(self):
        while True:
            user_input = input(PromptConfig.ADMIN_PROMPT)
            match user_input:
                case str(AdminDashboard.Add_new_station.value):
                    station_name = InputValidations.input_name(PromptConfig.STATION_NAME_PROMPT)
                    self.station_controller.add_station(station_name)
                case str(AdminDashboard.Add_new_train.value):
                    train_info = get_train_details_input()
                    self.train_controller.add_train(train_info)
                case str(AdminDashboard.View_existing_trains.value):
                    train_list = self.train_controller.view_trains()
                    view_train(train_list)
                case str(AdminDashboard.Update_train_details.value):
                    train_list = self.train_controller.view_trains()
                    if train_list:
                        print(train_list)
                        train_id = int(input(PromptConfig.TRAIN_NUMBER_PROMPT))
                        update_field = int(
                            input(PromptConfig.ADMIN_UPDATE_TRAIN_PROMPT)
                        )
                        match update_field:
                            case AdminUpdate.Train_Name.value:
                                new_name = input(PromptConfig.UPDATE_TRAIN_NAME_PROMPT)
                                train_info = dict(option=1, name=new_name)
                            case AdminUpdate.Train_Capacity.value:
                                new_capacity = int(
                                    input(PromptConfig.UPDATE_PASSENGER_CAPACITY_PROMPT)
                                )
                                train_info = dict(option=2, capacity=new_capacity)
                            case AdminUpdate.General_Coaches.value:
                                new_general_coaches = int(
                                    input(PromptConfig.UPDATE_GENERAL_COACH_PROMPT)
                                )
                                train_info = dict(
                                    option=3, general_coaches=new_general_coaches
                                )
                            case AdminUpdate.AC_Coaches.value:
                                new_ac_coaches = int(
                                    input(PromptConfig.UPDATE_AC_COACH_PROMPT)
                                )
                                train_info = dict(option=4, ac_coaches=new_ac_coaches)
                            case AdminUpdate.Sleeper_Coaches.value:
                                new_sleeper_coaches = int(
                                    input(PromptConfig.UPDATE_SLEEPER_COACH_PROMPT)
                                )
                                train_info = dict(
                                    option=5, sleeper_coaches=new_sleeper_coaches
                                )

                        self.train_controller.update_train_details(train_id, train_info)

                case str(AdminDashboard.Delete_train.value):
                    train_list = self.train_controller.view_trains()
                    view_train(train_list)
                    train_id = InputValidations.input_number(PromptConfig.TRAIN_NUMBER_PROMPT)

                    self.train_controller.delete_train(train_id)
                case str(AdminDashboard.Schedule_a_train.value):
                    train_list = self.train_controller.view_trains()
                    train_table = PrettyTable()
                    train_table.field_names = ["Train id", "Train Name"]

                    for train in train_list:
                        train_table.add_row(train[0:2])
                    print(train_table)
                    train_id = InputValidations.input_number(PromptConfig.TRAIN_NUMBER_PROMPT)
                    is_train_scheduled = self.train_controller.scheduled_train(train_id)

                    if is_train_scheduled:
                        station_table = PrettyTable()
                        station_table.field_names = PromptConfig.STATION_LIST_FIELDS
                        station_list = self.station_controller.view_station_list()
                        for station in station_list:
                            station_table.add_row(station)

                        print(station_table)
                        schedule = []
                        i = 1
                        while True:
                            station_id = InputValidations.input_number(PromptConfig.STATION_ID_PROMPT)
                            print(PromptConfig.ARRIVAL_TIME_PROMPT)
                            arrival_time = time_input()
                            print(PromptConfig.DEPARTURE_TIME_PROMPT)
                            departure_time = time_input()
                            day = int(input(PromptConfig.DAY_NUMBER_PROMPT))
                            sequence_number = i
                            i = i + 1
                            sub_schedule = (
                                station_id,
                                arrival_time,
                                departure_time,
                                day,
                                sequence_number,
                            )
                            schedule.append(sub_schedule)
                            user_input = input(PromptConfig.QUIT_OPTION)
                            if user_input == "q":
                                break
                            print(schedule)
                            self.train_controller.add_schedule(train_id, schedule)
                    else:
                        break
                case str(AdminDashboard.View_trains_for_booking.value):
                    search_option = InputValidations.input_number(PromptConfig.TRAIN_NUMBER_PROMPT)
                    match search_option:
                        case AdminSearch.Search_train_by_train_number.value:
                            train_number = InputValidations.input_number(PromptConfig.TRAIN_NUMBER_PROMPT)
                            train_route = self.train_controller.search_train_by_id(
                                train_number
                            )
                            if train_route != None:
                                schedule_table = PrettyTable()
                                schedule_table.field_names = (
                                    PromptConfig.SCHEDULE_TABLE_FIELDS
                                )
                                for schedule in train_route:
                                    schedule_table.add_row(schedule[1:5])

                                print(schedule_table)

                        case AdminSearch.Search_by_location.value:
                            start = input(PromptConfig.START_STATION_PROMPT)
                            destination = input(PromptConfig.END_STATION_PROMPT)
                            fetch_trains = (
                                self.train_controller.find_trains_by_location(
                                    start, destination
                                )
                            )

                            if fetch_trains:
                                trains = PrettyTable()
                                trains.field_names = PromptConfig.TRAIN_TABLE_FIELDS

                                for train in fetch_trains:
                                    trains.add_row(train)

                                print(trains)

                                train_number = InputValidations.input_number(PromptConfig.TRAIN_NUMBER_PROMPT)
                                train_route = self.train_controller.search_train_by_id(
                                    train_number
                                )
                                schedule_table = PrettyTable()
                                schedule_table.field_names = (
                                    PromptConfig.SCHEDULE_TABLE_FIELDS
                                )
                                for schedule in train_route:
                                    schedule_table.add_row(schedule[1:5])

                                print(schedule_table)
                case str(AdminDashboard.Logout):
                    exit()
