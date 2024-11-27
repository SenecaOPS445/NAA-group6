#!usr/bin/env/python3
# Name: Pulkit Nayyar
# SID: 152096210

import os
import subprocess
import pwd

def userexist(username):
    userslist = pwd.getpwall()
    for user in userslist:
        if user.pw_name == username:
            return True
    return False

def changepermission():
    user = input("Enter the user to escalate permissions: ").strip()
    if not user:
        print("Error: Please provide a user.")
        return

    if userexist(user):
        try:
            os.system(f"sudo usermod -aG sudo {user}")
            print(f"{user} has been added to the sudoers.")
        except Exception:
            print(f"Error: Cannot add '{user}' to the sudoers.")
            print(Exception)
    else:
        print(f"{user} does not exist")

def updatepasswd():
    user = input("Enter the user to change the password: ").strip()

    if not user:
        print("Error: no user provided.")
        return

    if userexist(user):
        try:
            print(f"Changing password for user '{user}'.")
            subprocess.run(["sudo", "passwd", user], check=True)
            print(f"Password for user '{user}' updated")
        except subprocess.CalledProcessError:
            print(f"Error: Cannot change password for user '{user}'.")
            print(subprocess.CalledProcessError)
    else:
        print(f"user: {user} does not exist.")

def updateusername():
    oldusrname = input("Enter the current username: ").strip()

    if not oldusrname:
        print("Error: no username provided.")
        return

    if userexist(oldusrname):
        newusrname = input("Enter the new username: ").strip()
        if not newusrname:
            print("Error: No new username provided.")
            return

        try:
            os.system(f"sudo usermod -l {newusrname} {oldusrname}")
            print(f"Username updated from '{oldusrname}' to '{newusrname}'.")
        except Exception:
            print(f"Error: Could not update username.")
            print(Exception)
    else:
        print(f"Username: {oldusrname} does not exist.")

def update_user():
    """
    This function will update user permissions,(if possible username, and password.)
    """
    print("Please choose an option:")
    print("1. Change a user password")
    print("2. Update username for an account")
    print("3. Make a user sudoer")
    print("4. exit")
    
    try:
        opt = int(input("Enter your option: ").strip())
    except ValueError:
        print("Invalid option")
        return

    if opt == 1:
        updatepasswd()
    elif opt == 2:
        updateusername()
    elif opt == 3:
        changepermission()
    elif opt == 4:
        print("----------Exiting----------.")
        return
    else:
        print("Invalid option")
