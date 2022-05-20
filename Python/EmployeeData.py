#!/usr/bin/python3
# Project 1
# Johnny Rivera
# CIT 383-001 Fall 2021
# 10/16/2021
from tabulate import tabulate
from collections import Counter


# This class creates employees and gets information based on what the administrator adds
class Employee:
    def __init__(self, eID, firstname, lastname, deptCode, superName, tempPass, server, linuxID):
        self.eID = eID
        self.firstname = firstname
        self.lastname = lastname
        self.deptCode = deptCode
        self.superName = superName
        self.tempPass = tempPass
        self.server = server
        self.linuxID = linuxID

# Each request function returns the employees information for use
    def reqName(self):
        return self.firstname + " " + self.lastname

    def reqID(self):
        return self.eID

    def reqDept(self):
        return self.deptCode

    def reqSup(self):
        return self.superName

    def reqUser(self):
        return self.linuxID

    def reqServer(self):
        return self.server


# This function is the initiation of the data collecting system
# Each try and exception statement validates the users input for incorrect values
def userRecords(eIDValid, eDict, dCL, sRL, eR):
    try:
        eID = int(input("Enter the user's employee id: "))
        eIDValid.append(eID)
        if eIDValid.count(eID) <= 1:
            eFN = str(input("Enter the user's first name: "))
            eLN = str(input("Enter the user's last name: "))
            try:
                eDN = int(input("Enter the user's department number: "))
                eS = str(input("Enter the user's supervisor (full name) :"))
                eLID = str(input("Enter the user's Linux account ID: "))
                eTP = str(input("Enter the user's Temporary Password: "))
                eSR = str(input("Enter the name of the server they've requested: "))
                sAdmin = Employee(eID, eFN, eLN, eDN, eS, eTP, eSR, eLID)
                eDict["Name"].append(str(sAdmin.reqName())), eDict["EmployeeID"].append(sAdmin.reqID()), \
                eDict["Department"].append(sAdmin.reqDept()), eDict["Supervisor Name"].append(sAdmin.reqSup()), \
 \
                eDict["Username"].append(sAdmin.reqUser())
                dCL.append(sAdmin.reqDept()), sRL.append(sAdmin.reqServer())
                # eDict.append({sAdmin.reqName(), sAdmin.reqID(), sAdmin.reqDept(), sAdmin.reqSup(),
                # sAdmin.reqUser()})
                try:
                    eUR = str(input("Would  you  like  to  create  another  record  (type  yes  or  Y  to continue)"))
                    if str(eUR).lower() == "y" or str(eUR).lower() == "yes":
                        eR = "y"
                    else:
                        eR = "n"
                except ValueError:
                    "No Input Recorded"
            except ValueError:
                eIDValid.remove(eID)
                print("Invalid Input: Input an integer")
        else:
            print("Employee ID already exists")
    except ValueError:
        print("Invalid Input: Input an Integer")
    return eR


# This functions calls for the printing of the users data
def printReport(eDict, sRL, dCL, eID):
    # This goes through the information and checks for information count: Server Requests and Department Codes
    tempSList = list((i, sRL.count(i)) for i in sRL)
    tempDList = list((i, dCL.count(i)) for i in dCL)
    print("Summary report of User Records")
    print("==============================")
    print(str(len(eID)) + " records created:")
    # Removes duplicates from count list and prints
    print(tabulate(list(set(tempDList)), headers=["Department Code", "Employee Count"]))
    print(tabulate(list(set(tempSList)), headers=["Server Requested", "Employee Count"]))
    return print(tabulate(eDict, headers="keys"))

# This function calls for all the previous classes and functions
def main():
    # Initiates the dictionary with keys for data collection
    eDict = {"Name": [], "EmployeeID": [], "Department": [], "Supervisor Name": [], "Username": []}
    # creates dummy list to start loop later on
    loopStart = []
    # dCl = department code list , sRL = server requested list
    dCL = []
    sRL = []
    eIDValid = []
    eR = ' '

    # Loops through the system based on what user inputs
    while str(eR).lower() == "y" or len(loopStart) == 0:
        eR = userRecords(eIDValid, eDict, dCL, sRL, eR)
        if str(eR).lower() == "n" and eR != "":
            loopStart.append("Stop")
        else:
            continue

    # Prints everything if the dictionary is not empty
    if eDict.keys():
        printReport(eDict, sRL, dCL, eIDValid)


main()
