#!/usr/bin/python3
# These lines import all the modules that are used in this lab.
import ftplib
import http.client
from ftplib import FTP
import os


# This function is used as the menu display runner.
def menuStart():
    print("Select one of the following options:")
    print("*" * 50)
    print("\n 1. Transfer a specified file.")
    print("\n 2. Download all specified file type to current directory.")
    print("\n 3. Obtain information of webpage with specified URL.")
    print("\n 4. Quit")


# This function handles the users input for the menu system.
def selectOption():
    selectOption = -1
    while selectOption not in range(1, 5):
        menuStart()
        selectOption = int(input("Enter one of the options above: "))
    return selectOption


# This function takes in a user-specified file extension type to download
def allX():
    # Initiates the FTP host.
    ftp = FTP(#PLACE IP ADDRESS OF HOST)
    # Lets the user know what option was selected as well as ask for file type.
    print("Option 2 Selected.")
    fileX = str(input("Enter the type of extension the file is: "))
    # Validates that the file type exists.
    try:
        with ftp:
            try:
                # Validates that the login credentials works
                ftp.login('ftpuser', 'student')
            except ftplib.error_reply:
                print("Incorrect username or password.")
                exit(-1)
            # Changes directory to where files will be downloaded from.
            ftp.cwd('cit383')
            # Goes through the file list in the directory for all the ones that fit the criteria.
            for c in ftp.nlst():
                a, b = os.path.splitext(c)
                # If it finds one it will download it to the requesting machine.
                if str(b) == str("." + fileX) or str(b) == str(fileX):
                    ftp.retrbinary("RETR " + (a + b), open((a + b), 'wb').write)
            ftp.close()
    except:
        print("This file type either is incorrect or does not exists in the current directory.")
        exit(-1)


# This function asks the user for a file name that will be transferred using FTP.
def specFile():
    # Initiates the FTP host.
    ftp = FTP(#PLACE IP ADDRESS OF HOST)
    # Lets the user know what option was selected as well as ask for file name to transfer.
    print("Option 1 Selected.")
    fileN = input("Enter the name of the file to be transfered: ")
    # Validates that the file exists.
    try:
        fileT = open(fileN, 'rb')
        with ftp:
            # Validates that the login credential works.
            try:
                ftp.login('ftpuser', 'student')
            except:
                print("Incorrect username or password.")
                exit(-1)
            # changes directory to place of transfer
            ftp.cwd('cit383Labs')
            # Sends the specified file to the directory mentioned before.
            ftp.storbinary('STOR ' + str(fileN), fileT)
        ftp.close()
    except FileNotFoundError:
        print("The file name either is incorrect or does not exists in the current directory.")
        exit(-1)


# This function uses a user-specified URL and gets information from it.
def webINFO():
    # Asks the user for a valid URL
    URL = str(input("Enter the URL of the website you want to retrieve information from: "))
    try:
        # Initiates the connection to the website
        hp = http.client
        content = hp.HTTPSConnection(str(URL))
        content.request("GET", "/")
        # Sets the website responses to object to call on later.
        resp = content.getresponse()
        # Calls upon the response object and validates that the information exists for that website.
        try:
            print("Website Status: " + str(resp.status))
        except:
            print("No Website Status Found: POSSIBLE INVALID URL")
        try:
            print("HTTP Version: " + str(resp.version))
        except:
            print("No HTTP Version Found: POSSIBLE INVALID URL")
        try:
            print("Content length: " + "{:.2f}".format((resp.length) / 1024) + "MB")
        except:
            print("No Length Found")
        try:
            print("Last Modification: " + str(resp.headers["last-modified"]))
        except:
            print("No Modification Date Found.")
        # Closes the connection.
        content.close()
        print("\n")
    except:
        print("Invalid URL")
        exit(-1)


# This function starts up the menu system and calls functions depending on the user input.
def main():
    manageOption = -1
    while manageOption != 4:
        manageOption = selectOption()
        if manageOption == 1:
            specFile()
        elif manageOption == 2:
            allX()
        elif manageOption == 3:
            webINFO()
        else:
            exit(-1)


main()
