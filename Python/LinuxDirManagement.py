#!/usr/bin/python
import os
from os import path as P
from tabulate import tabulate


# This method takes in two parameters: Directory Name and the number of files that are needed to create.
def createFiles(dName, fNumber):
    # Uses a loop to create the files in user's specified directory and the number of files
    for i in range(1, fNumber + 1):
        os.open(dName + "/file_" + str(i) + ".txt", 755)


# This methods creates sub-directories using two parameters: Directory Name and the number of subdirectories needed.
def createSubDirectories(dName, sdNumber):
    # Uses a loop to create the subdirectories
    for i in range(1, sdNumber + 1):
        os.mkdir(dName + "/dir_" + str(i))


# This method is used to get the name and the type of item that is in the directory.
def getInodeType(inode):
    # This adds the item to the list if its a directory
    if os.path.isdir(inode) and not inode.startswith("."):
        fileNames.append([str(inode), "Directory"])
    # This adds the item to the list if its a file
    if os.path.isfile(inode):
        fileNames.append([str(inode), "File"])


# This method uses the list created in the getInodeType method to print it to the console.
def listEntries(directory):
    for g in os.listdir(directory):
        getInodeType(g)
    # The system will use tabulate to print out the table using the specified headers and list
    print(tabulate(fileNames, headers=["Name", "Type"]))


# This method is used to rename the extension of the file to create it to whatever is specified by the user using
# the directory name, the current extension type of the file, and the new extension that is to be added.
def renameFiles(dName, cExt, nExt):
    for c in os.listdir(dName):
        a, b = os.path.splitext(c)
        if str(b) == str(cExt):
            os.renames(str(a) + str(cExt), str(a) + str(nExt))


# Prints the current working directory to the console.
print(os.getcwd())
# This creates the directory "Lab3" in the current working directory.
os.mkdir(str(os.getcwd()) + "/Lab3")
# Changes the directory to the one created above
os.chdir(str(os.getcwd()) + "/Lab3/")
# Prints current working directory to the console.
print(os.getcwd())

# Prompts user for amount of files wished to create
M = int(input("How many files would you like to create? "))

# Validates the input
if M > 0:
    # Uses the input for the method if it meets the validation requirements.
    createFiles(os.getcwd(), M)

# Prompts user for amount of directories wished to create
N = int(input("How many directories would you like to create? "))

# Validates the input
if N > 0:
    # Uses the input for the method if it meets the validation requirements.
    createSubDirectories(os.getcwd(), N)

# Creates the list where the data will be stored.
fileNames = []
# Calls the method using the current working directory
listEntries(os.getcwd())
# Calls the method using the current working directory, current file extension, and the desired new file extension.
renameFiles((os.getcwd()), ".txt", ".dat")
# Clears the list for the new entries to be listed after renaming
fileNames.clear()
# Calls method to print to console once more.
listEntries(os.getcwd())
