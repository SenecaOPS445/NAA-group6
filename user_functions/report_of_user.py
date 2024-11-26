#!usr/bin/env/python3

# Author: Jaekyun Kim
# StudentID: jkim681
# Last revised: 2024-11-24

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
        # After doing some research, modern linux distros generally uses uid greater th1an 1000 for regular users
        # root pw_uid is 0 so we should capture this as well
	    # in certain distro nobody system user has uid greater then 1000 and we do not want to include it.
        if (user.pw_uid >= 1000 or user.pw_uid == 0) and user.pw_name != "nobody":
            # we only want the username and the user home directory
            regular_users.append((user.pw_name,user.pw_dir))
    
    return regular_users

def get_last_login(user):
    """
    This function will return the detailed information about last login of given user.
    """
    # The os.popen will run the command and return the output as file object
    # We want to get the history of the login of the provided user
    last_login_command = os.popen(f"last {user}")
    # Since it is file object we need to read the file
    last_login_data = last_login_command.read()
    # when there is time i should try to clean the data
    return last_login_data

def is_sudoer(user):
    """
    This function will return True if the user is a sudoer, False otherwise.
    """
    # may need to check user group as well if the user is in sudo group
    # may need to add which folder the user has sudo access to
    # this problem is solved by running sudo -l -U command
    user_privileges_raw = os.popen(f"sudo -l -U {user}").read()
    # In some cases, the above command outputed more information then required. 
    # This code will filter out exccessive information by starting from the word "User"
    start_index = user_privileges_raw.find("User")
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
        return f"Unable to get disk usage for the user:{user_info[0]} This could be because user is system user \n"
    
    # Read the file
    disk_usage_data = disk_usage_command.read()
    return disk_usage_data

def user_report():
    """
    This function will create a user report as text file in the provided location for all users including the user's name, disk usage, when logged in and permissions. 
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
        # need to check disk usage
        report_file.write(f"Disk Usage: \n")
        report_file.write(get_user_disk_usage(user))
        # need to check last login 
        report_file.write(f"Login History: \n")            
        report_file.write(get_last_login(user[0]))
        report_file.write("\n")
    
    report_file.close()
    print("User report has been created successfully. AT {report_location}/user_report.txt \n")
    return