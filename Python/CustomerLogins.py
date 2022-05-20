#!/usr/bin/python3
import csv as e
import os
import os.path
from tabulate import tabulate

# This line initializes the use of the Excel file
employeeFile = "employee-logins.csv"
# This creates a new directory to store the text files which will be created.
os.mkdir(os.getcwd() + "\\eFolder")
# Assigns a variable to the new directory
cFolder = os.getcwd() + "\\eFolder\\"
# Creates an empty list to add employee's to
empList = []


# This methods takes in one excel file and checks login attempts
def employeeFR(fileN):
    with open(fileN, 'r') as csvfile:
        csvfile = e.reader(csvfile, delimiter=";")
        next(csvfile)
        # Reads excel rows and assigns them to their corresponding variable
        for row in csvfile:
            firstN = str(row[0])
            lastN = str(row[1])
            tLogin = int(row[2])
            ipAddr = str(row[3])
            # If login attempt count is over 200 it will add the employee to list.
            if tLogin > 200:
                empList.append([firstN, lastN, tLogin, ipAddr])
    return


# This method creates a file using the list of employees that have suspicious activity
def employeeFC(eList):
    # Initializes the suspicious count
    susCount = 0
    # Changes directory to create new files in the new directory
    os.chdir(cFolder)
    # Creates the files for every suspicious employee and adds info of employee as well.
    for i in range(len(eList)):
        file1 = open("Employee_" + str(i) + ".txt", "w")
        file1.write(str(empList[i]))
        susCount += 1
    # Creates and prints the table that was created using tabulate
    print(tabulate(eList, headers=["First Name", "Last Name", "Total Login Attempts", "IP Address"]))
    # Prints stored number of suspicious accounts
    print("The total number of employees with suspicious login attempts: " + str(susCount))
    return


# These two lines initializes the two methods using their respective parameter.
employeeFR(employeeFile)
employeeFC(empList)
