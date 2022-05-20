#!/usr/bin/python3
# Project 3
# Johnny Rivera
# CIT 383-001 Fall 2021
# 12/3/21
import getpass
import logging
import os
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import paramiko


# This function is used as the menu display runner.
def menuStart():
    print("Select one of the following options:")
    print("*" * 50)
    print("\n 1. Identify all the files in the home directory of a specified User.")
    print("\n 2. Download compromised files.")
    print("\n 3. Email CTO list of compromised files.")
    print("\n 4. Quit")


# This function handles the users input for the menu system.
def selectOption():
    selectedOption = -1
    while selectedOption not in range(1, 5):
        menuStart()
        selectedOption = int(input("Enter one of the options above: "))
    return selectedOption


# This function starts the ssh session given the credentials.
def connectionStart(HOSTNAME, username, passwd):
    PORT = 22
    # prompts the user for the password everytime just in-case it got left out without supervision.
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connects to the server given the password specified and the predetermined system information.
    ssh_client.connect(str(HOSTNAME), PORT, str(username), str(passwd))
    return ssh_client


# This function gets all the files that were modified within 21 days in the user's home directory.
def accountInfo(HOSTNAME, username, passwd):
    compL = []
    start = connectionStart(HOSTNAME, username, passwd)
    # This section sends the command to the user's computer and gets the output.
    FILE_PATH = '/home/' + str(username) + "/"
    command = "cd " + str(FILE_PATH) + " | find -mtime -21 -type f -maxdepth 1 -exec basename {} .po \\;"
    stdin, stdout, stderr = start.exec_command(command)
    output = stdout.read().decode('utf-8').splitlines()
    # Given the output it will get details about the said modified files.
    for i in output:
        command2 = "cd " + str(FILE_PATH) + " | date -r " + str(i)
        stdin, stdout, stderr = start.exec_command(command2)
        secondOut = stdout.read().decode('utf-8').splitlines()
        for j in secondOut:
            j = "Last Modification Date: " + str(j)
            # Makes sure that the files are not hidden
            if not i.startswith(".") and not i.startswith("_"):
                # Adds to list for reporting.
                compL.append([i, j])
    start.close()
    return compL


# This function is for printing the data that was found in another function.
def printData(data):
    # Prints all files that were compromised and their last modification date.
    # This also adds the filenames to the logger.
    print("File Name: " + "  " + "Last Modification Date: ")
    logger = logging.getLogger()
    if os.path.exists(os.getcwd() + 'logfile.log'):
        with open('logfile.log', 'w+'):
            pass
    logging.basicConfig(filename="logfile.log", filemode='w', format='%(message)s', level=logging.INFO)
    fileL = []
    for j in range(0, len(data)):
        temp = data[j][0]
        fileL.append(temp)
    for i in fileL:
        logger.info(str(i))
    return [print(i) for i in data]


# This function is for downloading the files from the compromised computer to the local computer.
def downloadFTP(HOSTNAME, USERNAME, password, data):
    fileL = []
    port = 22
    for j in range(0, len(data)):
        temp = data[j][0]
        fileL.append(temp)
    # Asks the user for the directory to download to.
    askU = str(input("Enter the directory where files will be downloaded: "))
    if not askU.endswith("/"):
        askU = askU + "/"
        if not os.path.exists(askU):
            askU = "/home/student/"

    # Initializes the connection.
    start = paramiko.Transport((HOSTNAME, port))
    start.connect(username=USERNAME, password=password)
    sftps = paramiko.SFTPClient.from_transport(start)

    # Makes a logger with the files that were compromised.
    logger = logging.getLogger()
    if os.path.exists(os.getcwd()+'logfile.log'):
        with open('logfile.log', 'w+'):
            pass
    logging.basicConfig(filename="logfile.log", filemode='w', format='%(message)s', level=logging.INFO)
    for c in sftps.listdir("/home/" + str(USERNAME) + "/"):
        for i in fileL:
            if c == i:
                # Downloads the files
                sftps.get("/home/" + str(USERNAME) + "/" + str(i), askU + str(i))
                # Adds filenames to logger.
                logger.info(str(i))
    start.close()
    return


# This function sends mail to the CTO with the list of files/user that were compromised. It also attached one comp file.
def sendMail(user):
    # This section gets the senders credential and the recipient's email address.
    sender_email = str(input("Enter your email address: "))
    receiver_email = str(input("Enter the recipient's email address: "))
    password = getpass.getpass(prompt="Enter your email password: ")

    # This section fills in the parts of the email
    message = MIMEMultipart("alternative")
    message["Subject"] = "Compromised Files"
    message["From"] = sender_email
    message["To"] = receiver_email

    # This section is for reading the logfile with the names of the files.
    file = open('logfile.log', 'r')
    lines = file.read().splitlines()
    # This line sets the sample file which will be attached to the email.
    sampleFile = str(lines[0])

    # The following section is the text version of the email.
    text = ("""\
    Dear CTO,
    This email was sent to inform you of the compromised files that we have found
    on the computer. The data that is presented you will be in list form and will include the following:
     *Files that have been attacked
     *Names of the users who have been attacked.
    In addition to the a attached compromised file for you to further investigate.
    
    Files Compromised:
    """ + str(lines) + """
    Users attacked:
    """ + str(user) + """
    Look forward to your response,
    Johnny Rivera""")

    # This section is the HTML version of the email.
    html = """\
    <html>
      <body>
        <p>Dear <b>CTO</b>,<br>
           This email was sent to inform you of the compromised files that we have found on the computer.<br>
           The data that is presented you will be in list form and will include the following:<br>
                <ol>
                    <li>Files that have been attacked</li>
                    <li>Names of the users who have been attacked.</li>
                </ol>  
           In addition to the a attached compromised file for you to further investigate.<br>
           <br>Files Compromised:<br>
           <b>{lines}</b><br>
           <br>Users Compromised:<br> 
           <b>{user}</b><br>      
            <br><i>Look forward to your response,<br>
            <b>Johnny Rivera</b></i><br>
        </p>
      </body>
    </html>
    """.format(lines=lines, user=user)

    # This last section adds all the pieces to the email that will sent
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    part3 = MIMEApplication(file.read(), filename=sampleFile)
    part3['Content-Disposition'] = 'attachment; filename="%s"' % sampleFile
    message.attach(part3)
    context = ssl.create_default_context()

    # Initialises the server connection to send the email.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()
        file.close()
    return


# This function initializes the code with the credentials and menu system handler.
def main():
    HOSTNAME = str(input("Enter the IP address of the target computer: "))
    username = str(input("Enter the username of the target computer: "))
    password = getpass.getpass(prompt="Enter " + str(username) + "'s password: ")

    # This section handles the user input for the menu system and runs different functions.
    manageOption = -1
    while manageOption != 4:
        manageOption = selectOption()
        if manageOption == 1:
            printData(accountInfo(HOSTNAME, username, password))
        elif manageOption == 2:
            downloadFTP(HOSTNAME, username, password, accountInfo(HOSTNAME, username, password))
        elif manageOption == 3:
            sendMail(username)
        else:
            exit(-1)


main()
