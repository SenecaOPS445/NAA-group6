#!usr/bin/env/python3
import sys

# Importing the functions from the user_functions folder
from user_functions.add_user import add_user
from user_functions.delete_user import delete_user
from user_functions.update_user import update_user
from user_functions.report_of_user import user_report

# This is the main function that runs through all the options and calls the appropriate function

def main():
    """
    This function provides the menu and captures the inputs from user. 
    If the user provides an invalid input, it will prompt the user to provide a valid input.
    this function returns false and which calls this function again.
    """
    print("Please choose between the following options")
    print("1. add user")
    print("2. delete user")
    print("3. update user permissions")
    print("4. Create user report")
    print("5. exit")
    command = input("Please enter a command: ")
    if command == "1":
        add_user()
        return True
    elif command == "2":
        delete_user()
        return True
    elif command == "3":
        update_user()
        return True
    elif command == "4":
        user_report()
        return True
    elif command == "5":
        return True
    else:
        print("Invalid command")
        return False



if __name__ == "__main__":
    loop_init = True
    if len(sys.argv) == 1:
        while loop_init:
            loop_init = main()
    else:
        print("Invalid command line arguments")
        sys.exit(1)
    sys.exit(0)
