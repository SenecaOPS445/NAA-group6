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

# Add the new user
    if subprocess.run(["sudo", "useradd", "-m", username]).returncode == 0:
        print(f"User '{username}' has been successfully added.")
    else:
        print("Error: Failed to add user. Check your permissions or input.")

