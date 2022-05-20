#!/usr/bin/python3
import re
from tabulate import tabulate


# This function is used to find all the lines on the apache log file and the information.
def getFileData(file):
    # LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""
    # This regular expression uses group capturing to get all the data within the file.
    reg_ex = r'(?P<ip>.*?) (?P<remote_log_name>.*?) (?P<userid>.*?) \[(?P<date>.*?)(?= ) (?P<timezone>.*?)\] \"(' \
             r'?P<request_method>.*?) (?P<path>.*?)(?P<request_version> HTTP\/.*)?\" (?P<status>.*?) (?P<length>.*?) ' \
             r'\"(?P<referrer>.*?)\" \"(?P<user_agent>.*?)'
    with open(file) as f:
        content = f.read()
        # Adds all the lines found in the log file to a list to be used later.
        alldata = re.findall(reg_ex, content)
    return alldata


# This function is used to get the IP addresses from the list obtained before.
def getClientIP(returnList):
    freqList = {}
    # Goes through the list and adds the IP address as the key and frequency of the IP address as the value to the
    # dictionary.
    for i in range(0, len(returnList)):
        currentIP = returnList[i][0]
        # Makes sure that the key is not already in place so it does not overwrite it everytime.
        if not currentIP in freqList.keys():
            freqList[currentIP] = ("*" * sum(x.count(str(currentIP)) for x in returnList))
    return freqList


# This function is used to get the status codes from the list obtained before.
def getStatusCode(returnList):
    SfreqList = {}
    # Goes through the list and adds the status codes as the key and frequency of the status codes as the value to the
    # dictionary in percentage form.
    for i in range(0, len(returnList)):
        currentIP = returnList[i][8]
        # Validates that the key has not already been added and formats the inputs.
        if not currentIP in SfreqList.keys() and not currentIP == '-':
            SfreqList[currentIP] = "{:.2f}".format(((sum(x.count(str(currentIP))
                                                         for x in returnList)) / len(returnList) * 100)) + "%"
    return SfreqList


# This function is used to print out the information that was obtained from the log file.
def printReport(IPlist, statusList, logfile):
    print("-" * 50)
    print("Statistics for the Apache log file: " + str(logfile))
    print("-" * 50)
    print("\n")
    headers1 = ["Client IP Address", "Frequency"]
    headers2 = ["HTTPS Status Code", "Percent Frequency"]
    # These two tables are formatted and in a loop so that the keys are also counted in the table instead of headers.
    print(tabulate([(k, v) for k, v in IPlist.items()], headers=headers1, tablefmt='fancy_grid'))
    print("\n")
    print(tabulate([(k, v) for k, v in statusList.items()], headers=headers2, stralign="center", tablefmt='fancy_grid'))
    return


# This function calls all the previous functions using the user's input for the logfile.
def main():
    # Takes in the log file that will be used and validates if it exists.
    userI = str(input("Enter the name of the log file to parse: "))
    try:
        listOut = getFileData(str(userI))
        printReport(getClientIP(listOut), getStatusCode(listOut), userI)
    except:
        print("File Does Not Exists")
        exit(-1)


main()
