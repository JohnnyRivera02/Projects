#!/usr/bin/python3
# Project 2
# Johnny Rivera
# CIT 383-001 Fall 2021
# 11/06/2021
import subprocess as sp
import sys, pwd, random, string, crypt, csv as c
import grp, getpass, os

# Imports the csv file that will be used
employeeFile = "employee-1.csv"
# Creates two empty list to reference later
empL = []
empNL = []


# This function is for checking if the user already exists in the system.
def userDup(userN):
    try:
        pwd.getpwnam(userN)
        return True
    except:
        return False


# This function is for creating usernames and checking if a suffix is needed.
def username(firstN, lastN):
    username = str.lower(lastN) + str.lower(firstN[0])
    count = 1
    while userDup(username):
        username1 = (username + str(count))
        if userDup(username1):
            count += 1
        else:
            username = username1
            break
    if not userDup(username):
        empNL.append([firstN, lastN, username])
    return username


# This function is for checking if a group exists already.
def groupDup(group):
    try:
        grp.getgrnam(group)
        return True
    except:
        return False


# This function is for user creation, it uses a random password generator to at least provide some security.
def userCreation(userN, firstN, lastN):
    password = (''.join(random.choice(string.ascii_letters) for i in range(7)))
    name = firstN + " " + lastN
    try:
        # Encrypts the password to add and uses useradd with the name as the comment.
        encpassword = crypt.crypt(password)
        # Uses useradd to add the name for comment, encrypted password and the username.
        sp.run(['useradd', '-c', name, '-p', encpassword,  userN])
    except:
        print("The account could not be created.")
        exit(-1)
    # Prints that it worked to let the administrator know
    print(str(userN) + "'s user created successfully.")


# This function is for group creation and assignment.
def groupCreation(userN, group):
    # Checks if the group exists, if not then it will create it.
    if not groupDup(group):
        sp.run(['groupadd', group])

    # Uses usermod to append a user to a group.
    try:
        # uses usermod to change the real name associated
        sp.run(['usermod', '-a', '-G', group, userN])
    except:
        print("The user could not be added to the group.")
        exit(-1)
    return


# This function is for extracting the csv data so it is readable for the program.
def extractData(fileN):
    with open(fileN, 'r') as csvfile:
        csvfile = c.reader(csvfile, delimiter=",")
        next(csvfile)
        # Reads excel rows and assigns them to their corresponding variable
        for row in csvfile:
            firstN = str(row[0])
            lastN = str(row[1])
            userG = str(row[2])
            empL.append([firstN, lastN, userG])
    return


# This function is for generating a csv file with the data after the usernames are created.
def generateData(eList):
    file1 = open("useraccounts" + ".csv", "w")
    file1F = ["first_name", "last_name", "username"]
    File1W = c.writer(file1)
    File1W.writerow(file1F)
    File1W.writerows(eList)


# This function is for initiating everything and allowing the admin to create accounts using a csv file.
def main():
    extractData(employeeFile)
    # For the length of the employee list it will create the users.
    for i in range(0, len(empL)):
        # This takes in the values of the multi-dimensional array and adds them to the loop variables.
        lFirstName = empL[i][0]
        lLastName = empL[i][1]
        lGroup = empL[i][2]
        # Calls the functions so that the accounts can be created using the information.
        lUsername = username(lFirstName, lLastName)
        userCreation(lUsername, lFirstName, lLastName)
        groupCreation(lUsername, lGroup)
    # Generates the csv file after all the usernames and accounts are created.
    generateData(empNL)


main()
