#!/usr/bin/python3
import csv_zip_rsync as rsync
import subprocess, os, shutil
import datetime
from datetime import timedelta
import zipfile, tarfile
import lzma

# This method is the menu for the action selection
def textM(userA):
    # If input is backup it runs through the file backup method
    if str(userA).lower() == "backup":
        # Take user Directory and destination Directory
        uD = str(input("Folder Name to Backup: "))
        dD = str(input("Folder Name of Backup: "))
        fileB(uD, dD)
    # if input is archive it runs the directory archive method
    elif str(userA).lower() == "archive":
        # Take user archive folder and desired archive type
        uA = str(input("Folder Name to Archive: "))
        dA = str(input("Archive type: "))
        dirArch(uA, dA)
    # if the input is mod it runs the modification check method
    elif str(userA).lower() == "mod":
        # takes user folder to check
        uM = str(input("Folder Name of Modification Check: "))
        twoW(uM)
    # if input is zip it runs the zip file size checker
    elif str(userA).lower() == "zip":
        # Takes the user zip file and kilobyte threshold
        uZ = str(input("Zip file to check: "))
        uT = int(input("Kilobyte threshold: "))
        largeZ(uZ, uT)
    # If they misspell or don't choose action correct it prints and ends
    else:
        print("Incorrect Selection")


# This method makes a folder backup of the directory the user inputs
def fileB(userDir, destDir):
    # Validates that the folder exist
    if os.path.exists(userDir):
        subprocess.run(['rsync', '-a', str(userDir), str(destDir)])
    # If directory doesn't exist it lets the user know
    else:
        print("Provided Directory Does Not Exist")

# This method creates an archive using the directory and the type
def dirArch(userD, typeA):
    # Checks if directory exists
    if os.path.exists(userD):
        # Checks which type of archive and creates it
        if str(typeA).lower() == "zip":
            shutil.make_archive(userD, 'zip', userD)
        elif str(typeA).lower() == "gztar":
            shutil.make_archive(userD, 'gztar', userD)
        elif str(typeA).lower() == "tar":
            shutil.make_archive(userD, 'tar', userD)
        elif str(typeA).lower() == "bztar":
            shutil.make_archive(userD, 'bztar', userD)
        elif str(typeA).lower() == "xztar":
            shutil.make_archive(userD, 'xztar', userD)
        else:
            print("Incorrect Archive Format")
    else:
        print("Folder Does not Exist")


# This method checks the zip contents for items above threshold specified
def largeZ(usrZ, sizeT):
    # Converts threshold of kilobytes to bytes
    sizeT = sizeT * 1024
    # Checks through the contents of zip
    with zipfile.ZipFile(usrZ) as zf:
        for data in zf.infolist():
            if data.compress_size > sizeT:
                # Prints file name and size
                print(data.filename, "File size: " + str(data.compress_size))
                # Checks which OS it uses
                if data.create_system == 0:
                    system = 'Windows'
                elif data.create_system == 3:
                    system = 'Linux'
                else:
                    system = 'Unknown'
                print("OS of File: " + system)


# This method is for checking which files have been modified in between 2 weeks from today
def twoW(userDir):
    # Checks if directory exists, if not sets it to current working directory
    if not os.path.exists(userDir):
        userDir = os.getcwd()
    else:
        os.chdir(os.getcwd() + "/" + str(userDir))
    print("Files modified in the last 2 weeks: ")
    # Starts to list out all the files that have been modified
    twoWeeks = datetime.datetime.utcnow() - timedelta(days=14)
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(item):
            if datetime.datetime.utcfromtimestamp(os.path.getmtime(item)) > twoWeeks:
                print(item)


def main():
    # Shows user the options and information about them.
    print("Action Selection: Backup, Archive, Mod, Zip")
    print("  -Backup: Creates back up folder")
    print("  -Archive: Archives your given folder with given format")
    print("  -Mod: Print files modified within the last 2 weeks")
    print("  -Zip: Displays compressed items over given threshold size")
    # Runs the menu method once user inputs his action
    userAction = str(input("What would you like to do :"))
    textM(userAction)


main()
