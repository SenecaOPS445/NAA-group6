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

def makesudoer():
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

def removesudoer():
    user = input("Enter the user to remove sudo access").strip()
    if not user:
        print("Error: Please provide a user.")
        return

    if userexist(user): 
        try:
            os.system(f"sudo deluser {user} sudo")
            print(f"{user} has been removed from the sudoers.")
        except Exception:
            print(f"Error: Cannot remove '{user}' from the sudoers.")
            print(Exception)
    else:
        print(f"{user} does not exist")
    
def update_user():
    """
    This function will update user permissions,(if possible username, and password.)
    """
    print("Please choose an option:")
    print("1. Change a user password")
    print("2. Make a user sudoer")
    print("3. Remove sudo access from a user ")
    print("4. exit")
    
    try:
        opt = int(input("Enter your option: ").strip())
    except ValueError:
        print("Invalid option")
        return

    if opt == 1:
        updatepasswd()
    elif opt == 2:
        makesudoer()
    elif opt == 3:
        removesudoer()
    elif opt == 4:
        print("----------Exiting----------.")
        return
    else:
        print("Invalid option")
