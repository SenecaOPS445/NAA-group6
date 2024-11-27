#!usr/bin/env/python3
import sys
import os

# Importing the functions from the user_functions folder
from user_functions.add_user import add_user
from user_functions.delete_user import delete_user
from user_functions.update_user import update_user
from user_functions.report_of_user import user_report

# This is the main function that runs through all the options and calls the appropriate function

def usage():
    """
    This function will print the usage of the script.
    """
    # Prints some user friendly information about how to run the script
    # To guide the user on how to run the script
    print("Usage: sudo python3 Assignment2.py")
    print("This script does not take in any command line arguments.")
    # Exits the script with a status code of 1 to indicate code did not run properly
    sys.exit(1)

def main():
    """
    This function provides the menu and captures the inputs from user. 
    If the user provides an invalid input, it will prompt the user to provide a valid input.
    this function returns false then the loop in main will call this function again.
    """
    print("Please choose between the following options")
    print("1. add user")
    print("2. delete user")
    print("3. update user ")
    print("4. create user report")
    print("5. exit")
    try:
        # This will try to convert the user input to an integer
        # Incase the user enters invalid input
        command = int(input("Please enter a command: "))
    except:
        # We do not know what the user will enter and we do not want the code to error out
        # This will catch all non-interger value inputs and prompt the user to enter a valid input
        print("Invalid command")
        print("Please enter a number beteween 1 and 5")
        return True
    if command == 1:
        # Menu option 1 is to add user
        add_user()
    elif command == 2:
        # Menu option 2 is to delete user
        delete_user()
    elif command == 3:
        # Menu option 3 is to update user
        update_user()
    elif command == 4:
        # Menu option 4 is to create user report
        user_report()
    elif command == 5:
        # This catches the exit command and will exit the program by exiting out of the loop
        print("Exiting the program")
        return False
    # this will catch all case where the user provides non-exit commands and will loop again
    return True



if __name__ == "__main__":
    loop_init = True # Setting this value will alow us to run the intitial loop
    # Since the script runs many terminal commands that requires prevlieged accesses
    # We need to make sure the user is running the script as sudo
    # To ensure that script runs as intended. The os.geteuid function will allow us
    # to check if the script is running with previleged access
    if os.geteuid() != 0:
        # This will check if the user is running the script as root (the 0 represents root)
        print("Insufficent Permission: This script needs to be run as sudo")
        usage()
    # Checks if the user has provided correct number of arguments (This script does not take in any command line input)
    if len(sys.argv) == 1: 
        # This will run the main function in a loop until the user exits the program
        while loop_init:
            # This will run the main function and set the loop value to either true or false based on how the user interacted with the function
            loop_init = main() 
    else:
        # If the user provided more command line arguments than expected, this will prmopt the correct user usage.
        print("Invalid command line arguments")
        usage()
    # This will exit the script with status code 0 to indicate the script ran successfully
    sys.exit(0)
