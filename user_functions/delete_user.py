#!/usr/bin/env python3
# Author ID: Mohammadullah

import os
import pwd

# Step 1: Check if the username provided by the user actually exists or not
def check_user_exists(username):
    """This is a helper funtions that checks if username is valid."""
    all_user = pwd.getpwall() # SHould return a list of all user system account details from file /etc/passwd
    # Go through the list of user entries.
    for user in all_user:
        # Check whether the username provided is matching or not with 'pw_name' attribute 
        if user.pw_name == username: 
            #If a match is found, return True to show the username exists
            return True
    # If the loop cannot find a match return False
    return False

    
def delete_user():
    """This function deletes user from the system.
     It will ask the user the username that they intended to delete then uses os.system() to run the commands. """
    
    # Step 2: Ask the user which username they wish to delete
    username = input("Enter the username you wish to delete: ")

    # Step 3: Check if the user has actually put in a valid username
    if not username: # If the user hits the enter key without entering anything.
        print("Error: No username provided.")
        return
    
    # checking if the user exists even before asking for confiramtion to delete the user
    if check_user_exists(username):
    # Step 4: Confirm that they actually want to delete the user
        while True: # Starts a loop until the user inputs a valid username
            confirmation = input(f"Are you sure you want to delete the user '{username}'? (yes/no): ").strip().lower() # the strip will remove any extra whitespaces and lower will make teh input in lower case.
            if confirmation == "yes": # User assures he wants to delete the user
                break # The loop stops and proceeds with deletion
            elif confirmation == "no": # User cancels deletion
                print("User deletion canceled.")
                return
            else: # Invalid input
                print("invalid Input. Please enter 'yes' or 'no'.")
    
    # Step 5: OS command for deleting the user
    # userdel -r removes the user and user's home directory
    # Try block tries to delete the user but gives error if the command executes unsuccsessfully

        try:
          # the code below runs the command that deletes the user from the system  
            result = os.system(f"sudo userdel -r {username}")
        except:
            # If we run into an error while deleting the user print a message saying user could not be deleted
            print(f"Error: could not delete the user '{username}'.")
            return 
        # If we do not run into error saying user deleted successfully
        print(f"User '{username}' successfully deleted.")
        return
    else:
        print(f"Username: {username} does not exist, please check again.") # show this message if the username provided is not in the system
        return 