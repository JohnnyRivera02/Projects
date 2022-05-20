#!/usr/bin/python3
import getpass, paramiko
import os


# This function is used as the menu display runner.
def menuStart():
    print("Select one of the following options:")
    print("*" * 50)
    print("\n 1. Create files in home directory.")
    print("\n 2. Copy all files from home directory to ssh_dir.")
    print("\n 3. Delete all files with a specified extension in ssh_dir.")
    print("\n 4. Display DNS server for VM.")
    print("\n 5. Display top 5 CPU consuming processes.")
    print("\n 6. Test Network Connectivity for VM given a specified URL.")
    print("\n 7. Display the VM's disk usage.")
    print("\n 8. Quit")


# This function handles the users input for the menu system.
def selectOption():
    selectOption = -1
    while selectOption not in range(1, 9):
        menuStart()
        selectOption = int(input("Enter one of the options above: "))
    return selectOption


# This function is used to initiate the ssh session once called upon.
def sshConnection():
    HOSTNAME = '10.2.57.7'
    PORT = 22
    username = "sshuser"
    # prompts the user for the password everytime just in-case it got left out without supervision.
    password = getpass.getpass(prompt="Enter " + str(username) + "'s password: ")
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connects to the server given the password specified and the predetermined system information.
    ssh_client.connect(HOSTNAME, PORT, username, password)
    return ssh_client


# This function creates 4 test files in the ssh server.
def fileCreate():
    connection = sshConnection()
    FILE_PATH = '/home/sshuser/'
    command = "touch file1.txt file2.txt file3.dat file4.dat"
    connection.exec_command("cwd " + FILE_PATH)
    stdin, stdout, stderr = connection.exec_command(command)
    output = stdout.read().decode('utf-8').splitlines()

    for i in output:
        print("File " + str(i) + " was created.")
    connection.close()
    return


# This function takes the testing files and transfers them using ssh commands.
def fileCopy():
    connection = sshConnection()
    # connection.exec_command("cd /home/sshuser/")
    stdin, stdout, stderr = connection.exec_command('ls')
    output = stdout.read().decode('utf-8').splitlines()

    # Takes the ls output and uses it for a loop to copy files that and not directories/hidden files.
    for files in output:
        if not os.path.isdir(files) and not files.startswith("."):
            connection.exec_command("cp " + files + " /home/sshuser/ssh_dir/")
    connection.close()
    return


# This function deletes the files that are in the ssh_dir given the specified extension.
def fileDelete():
    connection = sshConnection()
    fileX = str(input("Enter the type of extension you wish to delete: "))
    stdin, stdout, stderr = connection.exec_command('ls /home/sshuser/ssh_dir/ ')
    output = stdout.read().decode('utf-8').splitlines()

    # Takes the ls command for that directory and uses it for a loop.
    for files in output:
        a, b = os.path.splitext(files)
        if str(b) == str("." + fileX) or str(b) == str(fileX):
            # deletes the files with the forced option
            connection.exec_command("rm -f " + "/home/sshuser/ssh_dir/" + str(a + b))
    connection.close()
    return


# This function returns the VM's configured DNS server using the network manager.
def dnsServer():
    connection = sshConnection()
    # Calls a command to use the network manager and gets the 4 lines after DNS mention.
    stdin, stdout, stderr = connection.exec_command('nmcli | grep -A4 DNS')
    output = stdout.read().decode('utf-8').splitlines()

    # Prints out the output to the console.
    for i in output:
        print(i)
    connection.close()
    return


# This function returns the top 5 cpu demanding processes without much filtering.
def topFive():
    connection = sshConnection()
    # This executes the ps command to show the cpu usage processes.
    stdin, stdout, stderr = connection.exec_command("ps --sort=-pcpu | head -n 6")
    output = stdout.read().decode('utf-8').splitlines()

    # Prints the output to the console.
    for i in output:
        print(i)
    connection.close()
    return


# This function test the network on the VM using ping and a specified website.
def testNetwork():
    connection = sshConnection()
    # This variable prompts the user for a URL to pring to.
    URL = str(input("Enter the URL of the website you want to test connectivity for: "))
    stdin, stdout, stderr = connection.exec_command("ping " + URL + " -c 5")
    output = stdout.read().decode('utf-8').splitlines()

    # Prints the output to the console.
    for i in output:
        print(i)
    connection.close()


# This function is to show the disk usage on the system, it will show the system types as well.
def diskUsage():
    connection = sshConnection()
    stdin, stdout, stderr = connection.exec_command("df")
    output = stdout.read().decode('utf-8').splitlines()

    for i in output:
        print(i)
    connection.close()
    return


# This function initiates the system and calls upon functions given the user's input.
def main():
    manageOption = -1
    while manageOption != 8:
        manageOption = selectOption()
        if manageOption == 1:
            fileCreate()
        elif manageOption == 2:
            fileCopy()
        elif manageOption == 3:
            fileDelete()
        elif manageOption == 4:
            dnsServer()
        elif manageOption == 5:
            topFive()
        elif manageOption == 6:
            testNetwork()
        elif manageOption == 7:
            diskUsage()
        else:
            exit(-1)


main()
