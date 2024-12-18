#!usr/bin/env/python3

# Author: Jaekyun Kim
# StudentID: jkim681
# Last revised: 2024-11-26

import os
import pwd

def get_regular_users():
    """
    This function will return a list of regular users on the system.
    """
    # the pwd library provides access to /etc/passwd file without us manually opening the file manually
    # getpwall() will return a list of all users on the system as user object
    all_users = pwd.getpwall()
    
    # Get the regular users
    regular_users = []
    for user in all_users:
        # Since getpwall fetchese all users, including system users. we need to filter out these.
        # After doing some research, modern linux distros generally uses uid greater than 1000 for regular users
        # root pw_uid is 0 so we should capture this as well
	    # in certain distro nobody system user has uid greater then 1000 and we do not want to include it.
        if (user.pw_uid >= 1000 or user.pw_uid == 0) and user.pw_name != "nobody":
            # we only want the username and the user home directory
            # we also do not have to worry about empty list being returned as there will always be a root user
            regular_users.append((user.pw_name,user.pw_dir))
    
    return regular_users

def get_last_login(user):
    """
    This function will return the detailed information about login history of given user.
    """
    # The os.popen will run the command and return the output as file object
    # We want to get the history of the login of the provided user
    try: # we want to do some error catching in case the command fails
        last_login_command = os.popen(f"last {user}")
    except:
        # we want to notify the user right away and create the report with the error
        # in case other command works as intended
        print(f"Unable to get login history for the user:{user} \n")
        return f"Unable to get login history for the user:{user} \n"
    # Since it is file object we need to read the file
    last_login_data = last_login_command.read()
    # when there is time i should try to clean the data
    return last_login_data

def is_sudoer(user):
    """
    This function will return a string indicating if the user has sudo access. 
    It will also check what commands the user can run a sudo.
    """
    # may need to check user group as well if the user is in sudo group
    # may need to add which folder the user has sudo access to
    # this problem is solved by running sudo -l -U command
    try:
        user_privileges_raw = os.popen(f"sudo -l -U {user}").read()
    except:
        # we want to notify the user right away and create the report with the error
        # in case other command works as intendedo catch possible unexpected error that might occur when running the linix command
        print(f"Unexpected Error: Unable to get user privileges for the user:{user} \n")
        return f"Unexpected Error: Unable to get user privileges for the user:{user} \n"
    # In some cases, the above command outputed more information then required. 
    # This code will filter out exccessive information by starting from the word "User"
    start_index = user_privileges_raw.find("User") # finds the index that of the word "User"
    user_privileges = user_privileges_raw[start_index:]
    # if have time should try to clean the data
    return user_privileges

def get_user_disk_usage(user_info):
    """
    This function will return the disk usage of the user.
    """
    # This will run the command and return the output as file object
    # we want to get the disk usage by looking at the home directory of the user
    # This is provided by the user_info[1]
    try:
        disk_usage_command = os.popen(f"du -sh {user_info[1]}")
    except:
        # we want to notify the user right away and create the report with the error
        # in case other command works as intended
        print(f"Unable to get disk usage for the user:{user_info[0]} This could be because user is system user \n")
        return f"Unable to get disk usage for the user:{user_info[0]} This could be because user is system user \n"
    # Read the file
    disk_usage_data = disk_usage_command.read()
    return disk_usage_data

def get_recent(user):
    """
    This function will return the recent activity of the user.
    """
    # This will run the command and return the output as file object
    # we want to get the recent activity of the user
    try:
        recent_command = os.popen(f"w {user}")
    except:
        # we want to notify the user right away and create the report with the error
        # in case other command works as intended
        print(f"Unable to get recent activity for the user:{user} \n")
        return f"Unable to get recent activity for the user:{user} \n"
    # Read the file
    recent_data = recent_command.read()
    return recent_data

def user_report():
    """
    This function will create a user report as text file in the provided location 
    for all users including the user's name, disk usage, when logged in and permissions.
    This function does not return anything.
    """
    # Prompt the user for the location to save the report
    report_location = input("Please enter the location to save the user report: ")

    # We need to check if the filepath is valid
    if not os.path.exists(report_location):
        print("The location you have provided does not exist. \n")
        return
    # We need to create and write to text file in the file loaction
    report_file = open(report_location + "/user_report.txt", "w")

    # This calls the function to get the list of regular users
    users = get_regular_users()

    # need to use the list of users to get information about regualr users
    for user in users:
        report_file.write("-------------------------\n")
        report_file.write(f"User: {user[0]}\n")
        # need to check if the user is sudoer or not
        report_file.write(f"Permissions: \n")
        report_file.write(is_sudoer(user[0]))
        report_file.write("\n")
        # need to check disk usage
        report_file.write(f"Disk Usage: \n")
        report_file.write(get_user_disk_usage(user))
        report_file.write("\n")
        # need to check history of login 
        report_file.write(f"Login History: \n")    
        report_file.write(get_last_login(user[0]))
        report_file.write("\n")
        # Addition feature: looking at recent user activity  + cpu usage
        report_file.write(f"Recent User Activity: \n")
        report_file.write(get_recent(user[0]))
        report_file.write("\n")
    
    report_file.close() # make sure we close the file after writing to it
    # we want to notify if the report has been created successfully or not
    print(f"User report has been created successfully. AT {report_location}/user_report.txt \n")
    return # We do not return anything as the function does not expect any return value in the main code