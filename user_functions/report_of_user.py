#!usr/bin/env/python3
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
        if user.pw_uid >= 1000:
            # we only want the username (this may change)
            regular_users.append(user.pw_name)
    
    return regular_users

def user_report():
    """
    This function will create a user report as text file in the provided location for all users including the user's name, disk usage, when logged in and permissions. 
    """
    # Prompt the user for the location to save the report
    report_location = input("Please enter the location to save the user report: ")

    # We need to check if the filepath is valid
    if not os.path.exists(report_location):
        print("The location you provided does not exist.")
        return
    
    # This calls the function to get the list of regular users
    users = get_regular_users()

    # need to user the list of users to get information about regualr users
    # need to check if the user is sudoer or not
    # need to check last login
    # need to check disk usage
    # need to check how the user connected to the system
    
    return