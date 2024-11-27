#!usr/bin/env/python3

import subprocess

def add_user():
    """
    This function will add a user to the system.
    """

# Get the username from the user
    username = input("Enter the username for the new user: ").strip()
    if not username:
        print("Error: Username cannot be empty.")
        return

# Check if the user already exists
    if subprocess.run(["id", username], stdout=subprocess.DEVNULL).returncode == 0:
        print(f"Error: User '{username}' already exists.")
        return



