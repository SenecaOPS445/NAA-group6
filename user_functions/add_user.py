#!usr/bin/env/python3

import os

def add_user():
    """
    This function will add a user to the system.
    """

    # Get the username from the user
    username = input("Enter the username for the new user: ").strip() 
    # .strip gets rid of trailing empty spaces to reduce confusion when interjecting
    if not username: # this is a shortcut to username  ==, the statement evaluates the true when username is empty string
        print("Error: Username cannot be empty.")
        return
    
    # Check if the user already exists
    # users id command to check if the username already exists
    # we use os.popen() to run the command and read the output
    # os.popen does not print the output to the terminal, it stores the output in an object
    # we use 2>/dev/null to redirect the error output to /dev/null
    # so that when it errors, we do not save the message to the variable to get empty string
    # -u is a flag to indicate username
    # .read reads the data from the object that os.popen returns
    user_check = os.popen(f"id -u {username} 2>/dev/null").read().strip() # this will return the user id if the user exists
    if user_check: # checks if it is empty string or not
        print(f"Error: User '{username}' already exists.") # if it is not an empty string, that means the user already exists
        return

 # Run the 'useradd' command to add the user, using sudo for admin privileges
    # "-m" makes sure a home directotry is created for the new user
    # os.system() runs the command
    # we run the try block to catch any errors
    # os.system prints the output to the terminal
    try:
        os.system(f"sudo useradd -m {username}") # creating the user, -m creates the home directory and assigns it to the user
    except: # in case the command errors out, ex: something wrong with the system
        print("Error: Failed to add user. Check your permission or input")
        return
    return # return nothing due to the function not expecting anything to return