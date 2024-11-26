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
    if check_user_exists(username):
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
    # Try block truies to delete the user but gives error if the command executes unsuccsessfully

        try:

            result = os.system(f"sudo userdel -r {username}")
        except:
            print(f"Error: could not delete the user '{username}'.")
            return 
        print(f"User '{username}' successfully deleted.")
        return
    else:
        print(f"Username: {username} does not exist, please check again.")
        return 