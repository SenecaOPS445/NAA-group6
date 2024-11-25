# Fall 2024 Assignment 2 Group 6
## Project: User Report and Management 
### Descriptions
When managing linux systems we add and remove users often and sometimes change permissions. Furthermore, system admins may require to pull reports of all users and provide meaningful information about the users to optimize the system configuration. All of these task can be executed using regular linux commands, however it is a hassle to edit sudoers file for permissions, and compile reports from different command outputs. **There are no easy one stop tool to configure and manage users.**

This project is trying to is to partially automate this process and provide an user friendly front end to provide easy one stop tool to configure and manage users.\
Some of the features include:
- add/delete user 
- update user permission by adding/removing from sudoers file 
- provide meaningful reports about users, such as: 
  - list of all users
  - disk usage 
  - permissions the user has 
  - how/when user accessesed system (SSH, RDP, etc.) 
- Possibly more!

### Overview

When running the command\
(NOTE. This script **needs to run as sudo** to work properly)
`sudo python3 ./assignment2.py`

This will prompt the menu with all the options. These options may look like the following:\
(NOTE. This is **not** final!) 

`` 1. add user`` \
``2. delete user``\
``3. change permission of user``\
``4. create report of users``\
``5. exit``\
``please enter the action you want to execute (1-5):``

once the user enters the action, it will be prompted with appropriate information, such as user name, password, path where the report will be generated in.

There will be error handling in the program and the program will continue to loop through the menu until the user explicitly exits out or enter and execute ctrl-c.
### Answers to Some Questions
1. How will your program gather require input?

    The program will gather required input using various python standard libraries, such as os, subporcess, shutil library. We will leverage these libraries to collect data, and execute linux commands using the os library. This will allow us to capture the required information needed to generate the reports. For other informations such as username, password, etc. the program will prompt the user to enter the required data.

2. How will your program accomplish its requirements?

    The program will be menu driven, when first executed the user will be provided with options they can take and when needed, will be prompted to enter require information. Then the program will execute the required linux commands using the os library in python. Furthermore, for the reports and permission changes, the program will be using file manipulation to create reports from various commands provided in python standard library and existing linux commands, and edit sudoers files when requested.

3. How will output be presented?

    The immediate output will be presented to the standard output (Command Console) to indicate errors and if program executed successfully. For the reports, it will be generated as text file in user provided location.

4. What arguments or options will be included?

    When the program first runs, it will prompt the menu that users can take. This will include all the features listed above in the description.\
    To reiterate:
    - add/delete user 
    - update user permission by adding/removing from sudoers file 
    - provide meaningful reports about users, such as: 
        - list of all users
        - disk usage 
        - permissions the user has 
        - how/when user accessesed system (SSH, RDP, etc.) 
    - And possibly more
5. What aspects of development do you think will present the most challenge?

    We expect that file manipulation will be most difficult, as we need to edit the sudoers file which can break easily. Furthermore, file manipulation is a must when creating the reports. Also, understanding and using the standard libraries, and finding ways to get and format the outputs into one report file may appose some challenge.