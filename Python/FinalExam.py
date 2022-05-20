#!/usr/bin/python3
# Final Exam
# Johnny Rivera
# CIT 383-001 Fall 2021
# 12/14/21
import re

from tabulate import tabulate


def getFileData():
    file = "passwd.txt"
    # This regular expression uses group capturing to get all the data within the passwd file.
    reg_ex = r'(?P<user>.*?)\:(?P<passwd>.*?)\:(?P<userid>.*?)\:(?P<groupid>.*?)\:(?P<comment>.*?)\:(?P<home>.*?)\:(' \
             r'?P<sbin>.*?)'
    with open(file) as f:
        content = f.read()
        # Adds all the lines found in the log file to a list to be used later.
        alldata = re.findall(reg_ex, content)
    return alldata


# This function gets the groupID and the returned list from the previous function.
def findData(groupID, returnList):
    # Initiates a new list and count for later use.
    groupList = []
    count = 0
    # Goes through each of the users and finds the groupID to compare with the user's requested ID.
    for i in range(0, len(returnList)):
        if returnList[i][3] == str(groupID):
            groupList.append((returnList[i][0], returnList[i][4], returnList[i][3]))
            count += 1
    # Formats the output print using tabulate and a separate line for showing count, while entries exists.
    if count > 0:
        print(tabulate(groupList, headers=["Username", "Name", "GroupID"]))
        print("\nTotal number of users in group " + str(groupID) + " = " + str(count))
    # If no entries found then user will be informed it does not exist.
    if count == 0:
        print("\nInvalid/Non-Existing GroupID")
        exit(-1)


# This function initiates the entire code which includes getting the user's input and calling the previous functions.
def main():
    # Gets the user's input as integer
    uInput = int(input("Enter the group ID of the user: "))
    # sets the call so it calls it once.
    call = getFileData()
    findData(uInput, call)


main()
