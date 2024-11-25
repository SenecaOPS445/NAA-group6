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

def get_last_login(user):
    """
    This function will return the detailed information about last login of given user.
    """
    # The os.popen will run the command and return the output as file object
    # Do I use last or lastlog cmd? need to some research here
    last_login_command = os.popen(f"last {user}")
    # Since it is file object we need to read the file
    last_login_data = last_login_command.read()
    return last_login_data

def is_sudoer(user):
    """
    This function will return True if the user is a sudoer, False otherwise.
    """
    # The sudoers file is located in /etc/sudoers
    sudoers_file = open("/etc/sudoers", "r")
    # Read the file
    sudoers_data = sudoers_file.read()
    # Check if the user is in the sudoers file
    sudoers_file.close()
    # may need to check user group as well if the user is in sudo group
    if user in sudoers_data:
        return "User is a sudoer."
    return "User is not a sudoer."

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
    # We need to create and write to text file in the file loaction
    report_file = open(report_location + "/user_report.txt", "w")

    # This calls the function to get the list of regular users
    users = get_regular_users()

    # need to use the list of users to get information about regualr users
    for user in users:
        report_file.write("-------------------------\n")
        report_file.write(f"User: {user}\n")
        # need to check disk usage
        report_file.write(f"Disk Usage: \n")
        # need to check last login 
        report_file.write(f"Last Login: \n")            
        report_file.write(get_last_login(user))
        # need to check if the user is sudoer or not
        report_file.write(f"Permissions: \n")
        report_file.write(is_sudoer(user))
        report_file.write("\n")
    
    report_file.close()
    print("User report has been created successfully.")
    return