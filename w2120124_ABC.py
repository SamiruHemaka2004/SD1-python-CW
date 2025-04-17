#Author: D.Samiru Hemaka Wimalaransi
#Date: 09.12.2024
#Student ID: 20240795/ W2120124

# Task A:
def validate_date_input():
    #date in DD format
    while True:
        try:
            date = input("Please enter the day of the survey in the format DD: ")
            date_dig = int(date)#convert string to int 
            if 1 <= date_dig <= 31 and date.isdigit():#check conditions
                if len(date) == 2: #ensure day has two digits
                    print('')#for a space
                    break
                else:
                    print('enter two digits')
        
            else:
                print('enter a date whithin a calander')
        except ValueError:
            print('Integer required')
            
    #month in MM format
    while True:
        try:
            month = input('Please enter the month of the survey in the format MM: ')
            month_dig = int(month)
            if 1 <= month_dig <= 12 and month.isdigit():
                if len(month) == 2:
                    print('')
                    break
                else:
                    print('enter two digits')
                    
        
            else:
                print('enter a month whithin a calander')
        except ValueError:
            print('Integer required')

    #year in YYYY format
    while True:
        try:
            year = input('Please enter the year of the survey in the format YYYY: ')
            year_dig = int(year)
            if 2000 <= year_dig <= 2024 and year.isdigit():
                if len(year) == 4:
                    print('')
                    break
                else:
                    print('enter four digits')
        

            else:
                print('enter a valid year between 2000 to 2024.')
        except ValueError:
            print('Integer required')


    #check the year is a leap year
    is_leap_year = (year_dig % 4 == 0) #only consider 2000 to 2024

    #validate the day range for the month
    if month_dig in [4, 6, 9, 11]:  #months with 30 days
        if date_dig > 30:
            print(f"Invalid day:{month:02}only has 30 days.\n")
            return validate_date_input()  #restart the input process
    elif month_dig == 2:  #february
        if is_leap_year:
            if date_dig > 29:
                print("Invalid day: February in a leap year has only 29 days.\n")
                return validate_date_input()  #restart the input process
        else:
            if date_dig > 28:
                print("Invalid day: February in a non-leap year has only 28 days.\n")
                return validate_date_input()  
                
 #generate file path based on validated date inputs
    file_path = (f'traffic_data{date}{month}{year}.csv')
    
    print('********************************************')
    print(f'data file selected CSV file is: {file_path}')
    print('********************************************\n')


    date_for_histogram = (f'{date}/{month}/{year}')
    return file_path , date_for_histogram

#file_path , date_for_histogram = validate_date_input()


def validate_continue_input():
    while True:
        continue_input = input("Do you want to select another data file for a different date? Y/N: ").strip().upper()
        if continue_input in ['Y', 'N']:
            statement = continue_input
            break

        else:
            print("Invalid input. Please enter “Y” or “N”. ")
    return statement


# Task B: 
def process_csv_data(file_path):
    # initialize an empty dictionary to store outcomes
    outcomes = {}
    try:
        filepath = open(file_path,'r') #open file and set to read mode
        data = filepath.readlines() #read line by line 
        filepath.close() #file close
        
        for i in range(len(data)):
            data[i] = data[i].strip() #remove whitespace in csv file
            data[i] = data[i].split(',') #split ',' in csv file and update variable data
            
        total_vehicals = len(data)-1 #-1 to remove header 
        
        #Initialize variables
        truck = 0
        electric = 0
        two_wheel = 0
        busses_leaving = 0
        without_turn = 0
        bike = 0
        speed_limit = 0
        only_Elm_Avenue=0
        only_Hanley_Highway = 0
        scooter = 0
        rain_hours_set = set()
        peak_hour =[0]*24
        hours_dic_Elm={}
        hours_dic_Hanley={}
        
        #j is row
        for j in data:
            if j[8] == 'Truck':  #trucks
                truck += 1
                
            if j[9] == 'True':  #electric vehicles
                electric += 1
                
            if j[8] == 'Bicycle' or j[8] == 'Scooter' or j[8] == 'Motorcycle':    #two-wheel vehicles
                two_wheel += 1
                
            if j[0] == 'Elm Avenue/Rabbit Road' and j[4] == 'N' and j[8] == 'Buss':    #buses leaving Elm Avenue
                busses_leaving += 1
                
            if j[3] == j[4]:  #vehicles without turns
                without_turn += 1
                
            if j[8] == 'Bicycle':
                bike += 1
                
            try:
                if int(j[6]) < int(j[7]): #compare actual speed to speed limit
                    speed_limit += 1
            except ValueError: #don't consider the header 
                continue
            
            if j[0] == 'Elm Avenue/Rabbit Road':
                only_Elm_Avenue += 1
                
            if j[0] == 'Hanley Highway/Westway':
                only_Hanley_Highway += 1
                
            if j[0] == 'Elm Avenue/Rabbit Road'and j[8] == 'Scooter':
                scooter+=1
                
            if j[0] == "Hanley Highway/Westway":
                hour = int(j[2][:2]) #in 3rd row slice data from : and take only the hour
                peak_hour[hour] += 1

            if j[5] == 'Heavy Rain'or j[5]=='Light Rain':
                rain_hours = j[2][:2]
                rain_hours_set.add(rain_hours) #a set is used for not repeate hours

            if j[0] == "Elm Avenue/Rabbit Road":
                hour_by_hour_Elm = j[2][:2]
                if hour_by_hour_Elm not in hours_dic_Elm:
                    hours_dic_Elm[hour_by_hour_Elm] = 0
                hours_dic_Elm [hour_by_hour_Elm] += 1
            elif j[0] == "Hanley Highway/Westway":
                hour_by_hour_Hanley = j[2][:2]
                if hour_by_hour_Hanley not in hours_dic_Hanley:
                    hours_dic_Hanley[hour_by_hour_Hanley] = 0
                hours_dic_Hanley [hour_by_hour_Hanley] += 1


        total_hours_of_rain = len(rain_hours_set)
        peak_hour_vehicles = max(peak_hour)   
        max_index = peak_hour.index(peak_hour_vehicles)
        peak_hour_traffic_startat = max_index
        int(peak_hour_traffic_startat)
        peak_hour_traffic_endat = (peak_hour_traffic_startat)+1
        elm_vehicles = list(hours_dic_Elm.values())
        Hanley_vehicles = list(hours_dic_Hanley.values())
        final_hour_list = [elm_vehicles,Hanley_vehicles]


        try:
            percentage = round((truck / total_vehicals) * 100)
            avrg = round(bike/24)
            percentage_scooter = int((scooter / only_Elm_Avenue) * 100)
        except ZeroDivisionError:
            print('can not integer divide by 0')

        #use a dectionary for we can call a value from calling it's key
        outcomes={
            'file_path':file_path,
            'total_vehicals':total_vehicals,
            'truck': truck,
            'electric': electric,
            'two_wheel': two_wheel,
            'busses_leaving': busses_leaving,
            'without_turn': without_turn,
            'percentage': percentage,
            'avrg': avrg,
            'speed_limit': speed_limit,
            'only_Elm_Avenue': only_Elm_Avenue,
            'only_Hanley_Highway': only_Hanley_Highway,
            'percentage_scooter': percentage_scooter,
            'peak_hour_vehicles':peak_hour_vehicles,
            'peak_hour_traffic_startat':peak_hour_traffic_startat,
            'peak_hour_traffic_endat':peak_hour_traffic_endat,
            'total_hours_of_rain':total_hours_of_rain
        }
        

    except FileNotFoundError:
        print(f"File {file_path} not found.\n")
        outcomes = {}      
    except NameError:
        print(f"File {file_path} is not defined.\n")
        outcomes = {}      
    except IndexError:
        print(f"File {file_path} is empty.\n")
        outcomes = {}     
    return outcomes , final_hour_list


    
#outcomes , final_list = process_csv_data(file_path)


def display_outcomes(outcomes):
    try:
    
        print(f'The total number of vehicles recorded for this date is {outcomes['total_vehicals']}')        
        print(f'The total number of trucks recorded for this date is {outcomes['truck']}')        
        print(f'The total number of electric vehicles for this date is {outcomes['electric']}')
        print(f'The total number of two wheel vehicles for this date is {outcomes['two_wheel']}')
        print(f'The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes['busses_leaving']}')
        print(f'The total number of vehicles through both junctions not turning left or right is {outcomes['without_turn']}')
        print(f'The percentage of total vehicles recorded that are trucks for this date is {outcomes['percentage']}%.')
        print(f'The average number of bikes per hour for this date is {outcomes['avrg']}\n ')
        print(f'The total number of vehicles recorded as over the speed limit for this date is {outcomes['speed_limit']}')
        print(f'The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['only_Elm_Avenue']}')
        print(f'The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['only_Hanley_Highway']}')
        print(f'{outcomes['percentage_scooter']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n')
        print(f'The highest number of vehicles in an hour on Henley Highway/Westway is {outcomes['peak_hour_vehicles']}')
        print(f'The most vehicles through Henley/Westway were recorded between {outcomes['peak_hour_traffic_startat']}:00 and {outcomes['peak_hour_traffic_endat']}:00. ')
        print(f'The number of hours of rain for this day is {outcomes['total_hours_of_rain']}')

    except KeyError:
        #earlier function we defined outcomes ={} so in this function it will occur an error called KeyEroor so it will return without anything happen.
        return


#display_outcomes(outcomes)


# Task C
def save_results_to_file(outcomes, file_name="results.txt"):
    if not outcomes:
        return
    
    file_save = open(file_name,'a')
    file_save.write(f'data file selected CSV file is: {outcomes['file_path']}\n')
    file_save.write(f'The total number of vehicles recorded for this date is {outcomes['total_vehicals']}.\n')
    file_save.write(f'The total number of trucks recorded for this date is {outcomes['truck']}.\n')
    file_save.write(f'The total number of electric vehicles for this date is {outcomes['electric']}.\n')
    file_save.write(f'The total number of two wheel vehicles for this date is {outcomes['two_wheel']}.\n')
    file_save.write(f'The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes['busses_leaving']}.\n')
    file_save.write(f'The total number of vehicles through both junctions not turning left or right is {outcomes['without_turn']}.\n')
    file_save.write(f'The percentage of total vehicles recorded that are trucks for this date is {outcomes['percentage']}%.\n')
    file_save.write(f'The average number of bikes per hour for this date is {outcomes['avrg']}.\n ')
    file_save.write(f'The total number of vehicles recorded as over the speed limit for this date is {outcomes['speed_limit']}.\n')
    file_save.write(f'The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['only_Elm_Avenue']}.\n')
    file_save.write(f'The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['only_Hanley_Highway']}.\n')
    file_save.write(f'{outcomes['percentage_scooter']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n')
    file_save.write(f'The highest number of vehicles in an hour on Henley Highway/Westway is {outcomes['peak_hour_vehicles']}.\n')
    file_save.write(f'The most vehicles through Henley/Westway were recorded between {outcomes['peak_hour_traffic_startat']}:00 and {outcomes['peak_hour_traffic_endat']}:00.\n')
    file_save.write(f'The number of hours of rain for this day is {outcomes['total_hours_of_rain']}.\n\n')
    file_save.write(f'*****************************************************************************\n\n')
 
    file_save.close()
    print(f"\nAll Outcomes saved to {file_name}.\n")

#save_results_to_file(outcomes, file_name="results.txt")

#validate_continue_input()#y or n for repeat this prosess or terminate


























