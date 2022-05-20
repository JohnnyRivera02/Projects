#!/usr/bin/python3
import argparse, logging, os
# When running this on windows as I did, make sure to use: "pip install tabulate" in cmd to obtain module
from tabulate import tabulate

# Creates a logger handler with a logfile and a given format to show different messages.
logger = logging.getLogger()
logging.basicConfig(filename="logfile.log", format='%(levelname)s:%(message)s', level=logging.DEBUG)


# This method uses the list created in the getInodeType method to print it to the console.
def listEntries(Directory):
    for g in os.listdir(Directory):
        if not g.startswith(".") or not g.startswith(".."):
            if os.path.isdir(g):
                fileNames.append([str(g), "Directory"])
            else:
                fileNames.append([str(g), "File"])
    # The system will use tabulate to print out the table using the specified headers and list
    return print(Directory), print(tabulate(fileNames, headers=["Names", "Type"]))


# Creates a parser object that gives the description and adds the help option.
parser = argparse.ArgumentParser(description="List content of given directory.", add_help=True)

# Creates the user defined arguments and makes the directory required when running.
parser.add_argument('-d', action="store", default="", dest="userDirectory", help="A directory must be "
                                                                                 "provided", required=True)
parser.add_argument('-l', action="store_true", default=False, dest="booleanVar",
                    help="if -l is present, then output will be sent to the log file with the specified name.")

# Obtains the values from the parse and sets it to variables for use.
results = parser.parse_args()
directory = str(results.userDirectory)
LogPrint = bool(results.booleanVar)

# Creates an empty list to display the directory content.
fileNames = []
# If -l option is given then it will print the logfile that is used.
if LogPrint:
    print("Logger: logfile.log")

# Validates the path with the exception handling
try:
    listEntries(directory)
    # If the option was given it will add the output to the logfile.
    if LogPrint:
        logger.info(str(fileNames))
except FileNotFoundError:
    # Catch invalid input exception
    print("The given directory does not exist")
    # If the option was given it will add the error to the logfile.
    if LogPrint:
        logger.error("This directory does not exist")
    # Exits the program
    exit(1)
