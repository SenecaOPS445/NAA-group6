#!/usr/bin/env python3
# Author ID: Mohammadullah

import os
import pwd

def check_user_exists(username):
    """This is a helper funtions that checks if username is valid."""
    all_user = pwd.getpwall() 
    for user in all_user:
        if user.pw_name == username:
            return True
    return False

    
def delete_user():
    """This function deletes user from the system.
     It will ask the user the username that they intended to delete then uses os.system() to run the commands. """
    
    # Step 1: Ask the user which username they wish to delete
    username = input("Enter the username you wish to delete: ")

    # Step 2: Check if the user has actually put in a valid username
    if not username: # If the user hits the enter key without entering anything.
        print("Error: No username provided.")
        return
    
    # Step 3: Confirm that they actually want to delete the user
    while True: # Starts a loop until the user inputs a valid username
        confirmation = input(f"Are you sure you want to delete the user '{username}'? (yes/no): ").strip().lower()
        if confirmation == "yes": # User assures he wants to delete the user
            break # The loop stops and proceeds with deletion
        elif confirmation == "no": # User cancels deletion
            print("User deletion canceled.")
            return
        else: # Invalid input
            print("invalid Input. Please enter 'yes' or 'no'.")
    
     # Step 4: OS command for deleting the user
    # userdel -r removes the user and user's home directory
    # the returned value of os.system is the key to decide whether the command in the string parameter is successfully executed or not. 
    if check_user_exists(username):

        result = os.system(f"sudo userdel -r {username}")
        print(f"User '{username}' successfully deleted.")


    # Step 5: Run the command to see what it returns
    if result == 0: # If the return value is 0 then it is showing that the task is successfully executed.
        
    else: # If the return value is not equal to zero, then the command failed
        # Reasons for failure may include:
        # - User does not exist
        # - Insufficient permissions
        # - Syntex issues with the command
        print(f"Error: could not delete the user '{username}'. Please check the username or your permissions.")