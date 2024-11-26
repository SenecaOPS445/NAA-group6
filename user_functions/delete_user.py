#!/usr/bin/env python3
# Author ID: Mohammadullah

import os

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
    