#!/usr/bin/python3
import csv as e
import ipaddress as i
import re
from tabulate import tabulate

# Imports the data into an object
employeeFile = "empdata-2.csv"
# Initiates the list that will be used
empCompL = []
empWPL = []
updatedEL = []
# Sets the reserved IP addresses that cannot be assigned to end-users
r1 = i.ip_address('250.30.8.0')
r2 = i.ip_address('250.30.8.255')
# Sets the subnet mask for the IP Addresses
mask = i.ip_network('250.30.8.0/24')


# This function displays the menu system
def displayMenu():
    print("Select one of the following employee management options:")
    print("*" * 50)
    print("\n 1. Print the information regarding the compromised computers.")
    print("\n 2. Print the information of users with weak passwords.")
    print("\n 3. Create an updated file and print names of employees with updated department.")
    print("\n 4. Quit")


# This function manages the user's input
def selectOption():
    selectOption = -1
    while selectOption not in range(1, 5):
        displayMenu()
        selectOption = int(input("Enter one of the options above: "))
    return selectOption


# This function handles all the csv reading and writing
def employeeFR(fileN):
    # Opens a new file for the new updated department
    file1 = open("empdata-new" + ".csv", "w")
    # Sets the column names
    file1F = ["first_name", "last_name", "email", "ipaddress", "department", "username", "Password"]
    # Reads the file provided by the function parameter
    with open(fileN, 'r') as csvfile:
        updatedL = []
        csvfile = e.reader(csvfile, delimiter=",")
        next(csvfile)
        # Reads excel rows and assigns them to their corresponding variable
        for row in csvfile:
            firstN = str(row[0])
            lastN = str(row[1])
            email = str(row[2])
            ipAddr = str(row[3])
            dept = str(row[4])
            user = str(row[5])
            password = str(row[6])
            updatedDept = str("Financing")
            # Checks if ipaddress is within the subnet and also doesn't include the reserved IPs.
            if i.ip_address(ipAddr) in mask and i.ip_address(ipAddr) != r1 and i.ip_address(ipAddr) != r2:
                empCompL.append([firstN, lastN, email, ipAddr, dept, user, password])
            # Checks if the password meets the requirements (over 10 characters but not more than 12)
            # Checks all instances where it also meets the criteria and excludes them from the weak password list.
            if len(password) < 10 or len(password) > 12 and not re.findall(r'[A-Z][a-z][\d][\W]]', password):
                empWPL.append([firstN, lastN, password])
            # If the department is accounting it will change it to the updated name (financing)
            if dept == "Accounting":
                updatedL.append([firstN, lastN, email, ipAddr, updatedDept, user, password])
                updatedEL.append([firstN, lastN, updatedDept])
            # Else if it does not include the department provided then it will ignore it but still add to updated file.
            elif dept != "Accounting":
                updatedL.append([firstN, lastN, email, ipAddr, dept, user, password])
        # Writes the new data to the file.
        File1W = e.writer(file1)
        File1W.writerow(file1F)
        File1W.writerows(updatedL)
    return


# This is the main function that handles the user's input and goes through the function calling.
def main():
    employeeFR(employeeFile)
    manageOption = -1
    while manageOption != 4:
        manageOption = selectOption()
        # Each option will clear the list so that it does not repeat the information after the print.
        if manageOption == 1:
            print(tabulate(empCompL, headers=["First Name", "Last Name", "Email", "IP Address", "Department",
                                              "Username", "Password"]))
            empCompL.clear()
        elif manageOption == 2:
            print(tabulate(empWPL, headers=["First Name", "Last Name", "Password"]))
            empWPL.clear()
        elif manageOption == 3:
            print(tabulate(updatedEL, headers=["First Name", "Last Name", "Department"]))
            updatedEL.clear()
        else:
            exit(-1)


main()
