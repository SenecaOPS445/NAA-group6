#!usr/bin/env/python3

import os

def add_user():
    """
    This function will add a user to the system.
    """

    # Get the username from the user
    username = input("Eneter the username for the new user: ").strip()
    if not username:
        print("Error: Username cannot be empty.")
        return
    
    # Check if the user already exists
    # users id command to check if the username already exists
    # we use os.popen() to run the command and read the output
    # we use 2>/dev/null to redirect the error output to /dev/null
    # so that when it errors, we do not save the message to the variable to get empty string
    user_check = os.popen(f"id -u {username} 2>/dev/null").read().strip()
    if user_check:
        print(f"Error: User '{username}' already exists.")
        return

 # Run the 'useradd' command to add the user, using sudo for admin privileges
    # "-m" makes sure a home directotry is created for the new user
    # os.popen() runs the command
    # we run the try block to catch any errors
    try:
        os.system(f"sudo useradd -m {username}")
    except:
        print("Error: Failed to add user. Check your permission or input")
        return
    return