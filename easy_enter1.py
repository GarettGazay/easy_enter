import pandas as pd

# INPUT DATA
patient_fname = input("First Name: ")
patient_lname = input("Last Name:  ")
patient_phone = input("Phone: ")
start_address = input("Start Address: ")
end_address = input("End Address: ")
day_code = input("Day code: ") #day code is pickup_date
customer_email = ""

pickup_time_weekday1 = input("Pickup Time WeekDay 1: ") # add to same cell as pickup_date, append to [0] of first date
return_time_weekday1 = input("Return Time WeekDay 1: ")
pickup_time_weekday2 = input("Pickup Time WeekDay 2: ") # add to same cell as pickup_date, append to [1] of first date
return_time_weekday2 = input("Return Time WeekDay 2: ")
pickup_time_weekday3 = input("Pickup Time WeekDay 3: ") # add to same cell as pickup_date, append to [2] of first date
return_time_weekday3 = input("Return Time WeekDay 3: ")
#
#return_date = input("Return date: ")
service_type = input("Service Type: ")
account_id = input("Account ID: ")
passengersNum = input("Number of Passengers: ")
# driver_notes = ""
dispatcher_notes = input("Dispatcher Notes: ")
# customer_notes = ""
driver_name = ""
# driver_email = ""

# July dates, for each element in day, add ~n~ new rows with all data populated
mon_pickup = "2018-7-2 " + pickup_time_weekday1,"2018-7-9 " + pickup_time_weekday1,"2018-7-16 " + pickup_time_weekday1,"2018-7-23 " + pickup_time_weekday1,"2018-7-30 " + pickup_time_weekday1
mon_return = "2018-7-2 " + return_time_weekday1,"2018-7-9 " + return_time_weekday1,"2018-7-16 " + return_time_weekday1,"2018-7-23 " + return_time_weekday1,"2018-7-30 " + return_time_weekday1

tues_pickup = "2018-7-3 " + pickup_time_weekday1,"2018-7-10 " + pickup_time_weekday1,"2018-7-10 " + pickup_time_weekday1,"2018-7-17 " + pickup_time_weekday1,"2018-7-24","2018-7-31 " + pickup_time_weekday1
tues_return = "2018-7-3 " + return_time_weekday1,"2018-7-10 " + return_time_weekday1,"2018-7-10 " + return_time_weekday1,"2018-7-17 " +  return_time_weekday1,"2018-7-24","2018-7-31 " + return_time_weekday1

wed_pickup = "2018-7-4 " + pickup_time_weekday2,"2018-7-11 "  + pickup_time_weekday2,"2018-7-18 "  + pickup_time_weekday2,"2018-7-25 "  + pickup_time_weekday2
wed_return = "2018-7-4 " + return_time_weekday2,"2018-7-11 " + return_time_weekday2,"2018-7-18 "  + return_time_weekday2,"2018-7-25 "  + return_time_weekday2

thurs_pickup = "2018-7-5 " + pickup_time_weekday2,"2018-7-12 " + pickup_time_weekday2,"2018-7-19 " + pickup_time_weekday2,"2018-7-26 " + pickup_time_weekday2
thurs_return = "2018-7-5 " + return_time_weekday2,"2018-7-12 " + return_time_weekday2,"2018-7-19 " + return_time_weekday2,"2018-7-26 " + return_time_weekday2

fri_pickup = "2018-7-6 " + pickup_time_weekday3,"2018-7-13 " + pickup_time_weekday3,"2018-7-20 " + pickup_time_weekday3,"2018-7-27 " + pickup_time_weekday3
fri_return =  "2018-7-6 " + return_time_weekday3,"2018-7-13 " + return_time_weekday3,"2018-7-20 " + return_time_weekday3,"2018-7-27 " + return_time_weekday3

sat_pickup = "2018-7-7 " + pickup_time_weekday3,"2018-7-14 " + pickup_time_weekday3,"2018-7-21 " + pickup_time_weekday3,"2018-7-28 " + pickup_time_weekday3
sat_return = "2018-7-7 " + return_time_weekday3,"2018-7-14 " + return_time_weekday3,"2018-7-21 " + return_time_weekday3,"2018-7-28 " + return_time_weekday3

sun = "2018-7-1","2018-7-8","2018-7-15","2018-7-22","2018-7-29"

mwf_start = mon_pickup + wed_pickup + fri_pickup
mwf_end = mon_return + wed_return + fri_return
tthsat_start = tues_pickup + thurs_pickup + sat_pickup
tthsat_end = tues_return + thurs_return + sat_return

pickup_count = []
return_count = []
total_count  = []
pickup_sched = []
startNum = []
endNum = []

def pickupTimes(day_code):
    global pickup_sched
    global pickup_count
    global startNum

    # Day code identifier
    if day_code == "mwf":
        pickup_sched = mon_pickup, wed_pickup, fri_pickup
    elif day_code == "tthsat":
        pickup_sched = tues_pickup, thurs_pickup, sat_pickup
    # Count number of rides
    for i in pickup_sched:
        for j in i:
            # print(j)
            pickup_count += [j]
    startNum = len(pickup_count)
    # print("StartNum: ",startNum)
    # print("Pickups: ",pickup_sched)

def returnTimes(day_code):
    global return_sched
    global return_count
    global endNum

    # Day code identifier
    if day_code == "mwf":
        return_sched = mon_return, wed_return, fri_return
    elif day_code == "tthsat":
        return_sched = tues_return, thurs_return, sat_return
    # Count number of rides
    for i in return_sched:
        for j in i:
            # print(j)
            return_count += [j]
    endNum = len(return_count)
    # print("endNum: ",endNum)
    # print("Returns: ",return_sched)

def createCSV(fname,lname,phone,start_addy,end_addy,passNum,day_code,sertype,accID,dispnotes):
    global mwf_start
    global startNum
    global endNum
    global mwf_end
    global tthsat_start
    global tthsat_end

    # Total rides to be used to multiply each attribute
    total_rides = startNum + endNum

    # Concat names
    patient_name = fname + " " + lname

   # Create dataframe with all data except dates
    df_create = pd.DataFrame({
        'customer_name' : [patient_name] * total_rides,
        'customer_phone' : [phone] * total_rides,
        'customer_email' : [''] * total_rides,
        'start_address' : [start_addy] * startNum + [end_addy] * endNum,
        'end_address' : [end_addy] * endNum + [start_addy] * startNum,
        'pickup_date' : [''] * total_rides,
        'return_date' : [''] * total_rides,
        'account_id': [accID] * total_rides,
        'service_type' : [sertype] * total_rides,
        'passengers' : [passNum] * total_rides,
        'driver_notes' : [''] * total_rides,
        'dispatcher_notes' : [dispnotes] * total_rides,
        'customer_notes' : [''] * total_rides,
        'driver_email' : [''] * total_rides,
    })

    'passengers','driver_notes','customer_notes','driver_email'

    # Loop through the dates and merge dataframes


    # Pick Ups
    df_start_dates = pd.DataFrame({})
    df_start_dates1 = pd.DataFrame({})

    if day_code == "mwf":
        for i in mwf_start:
            df_start_dates = df_start_dates.append(pd.DataFrame({'pickup_date' : i}, index=[0]), ignore_index=False)
        # print("MWF Pick up dates: ",df_start_dates)
    elif day_code == "tthsat":
        for i in tthsat_start:
            # print("tthsat_start: ",tthsat_start)
            df_start_dates1 = df_start_dates1.append(pd.DataFrame({'pickup_date' : i}, index=[0]), ignore_index=False)
        # print("TTHSAT Pick up dates: ",df_start_dates1)


    # Returns
    df_end_dates = pd.DataFrame({})
    df_end_dates1 = pd.DataFrame({})

    if day_code == "mwf":
        for i in mwf_end:
            df_end_dates = df_end_dates.append(pd.DataFrame({'pickup_date' : i}, index=[0]), ignore_index=False)
        # print("Return dates: ",df_end_dates)
    elif day_code == "tthsat":
        for i in tthsat_end:
            df_end_dates1 = df_end_dates1.append(pd.DataFrame({'pickup_date' : i}, index=[0]), ignore_index=False)
        # print("TTHSAT Return dates: ",df_end_dates1)


    # Append All DataFrames

    allDates = df_start_dates.append(df_end_dates)
    allDates1 = df_start_dates1.append(df_end_dates1)


    if day_code == "mwf":
        concat = pd.concat([df_create,allDates])
        concat.to_csv('scfhp-july.csv', index=False, columns = ['customer_name','customer_phone','customer_email','start_address','end_address','pickup_date','return_date','account_id','service_type','passengers','driver_notes','dispatcher_notes','customer_notes','driver_email'])
        print("")
        print("Your MWF schedule for",patient_name, "for the Month of July has been created...")
    elif day_code == "tthsat":
        concat = pd.concat([df_create,allDates1])
        concat.to_csv('scfhp-july.csv', index=False, columns = ['customer_name','customer_phone','customer_email','start_address','end_address','pickup_date','return_date','account_id','service_type','passengers','driver_notes','dispatcher_notes','customer_notes','driver_email'])
        print("")
        print("Your TTHSAT schedule for",patient_name, "for the Month of July has been created...")

pickupTimes(day_code)
returnTimes(day_code)
createCSV(patient_fname,
                patient_lname,
                patient_phone,
                start_address,
                end_address,
                passengersNum,
                day_code,
                service_type,
                account_id,
                dispatcher_notes)
