#!/usr/bin/python
# Imports table formatter
from tabulate import tabulate
# Initiates the code loop
while (1 == 1):
    # Ask the user the amount of students
    studentNum = int(input("How many students are there in the class?"))
    # Checks Validation
    if studentNum <= 0:
        print("Invalid Input")
        break
    else:
        # Ask user how many days it will be recording for.
        studentWN = int(input("How many days in the weekend?"))
        # Checks Validation
        if studentWN <= 0:
            print("Invalid Input")
            break
        else:
            # Initiates the empty list to collect student information
            studentStats = []
            # Creates 2 variables to store total scripting and math time.
            totalST = 0.0
            totalMT = 0.0
            # Ask information based on number of students
            for i in range(1, studentNum + 1):
                # Initiates local variable to collect math and scripting avg for the amount of days.
                studentMWNA = 0.0
                studentSWNA = 0.0
                # Ask for information per day and subject
                for j in range(1, studentWN + 1):
                    # Asks user the hours the student studied for math
                    studentMHr = float(input("How many hours (1-9) did you study math on day" + str(j) + "?"))
                    # Adds input to use later on in average calculation.
                    studentMWNA += studentMHr
                    # Checks input Validation
                    if studentMHr >= 10 or studentMHr <= 0:
                        print("Invalid input in math field")
                        break
                    else:
                        # Asks user the hours the student studied for scripting
                        studentSHr = float(input("How many hours (1-9) did you study scripting on day" + str(j) + "?"))
                        # Adds input to use later on in average calculation.
                        studentSWNA += studentSHr
                        # Checks Validation
                        if studentMHr >= 10 or studentMHr <= 0:
                            print("Invalid input in scripting field")
                            break
                # Calculates average using inputs from students per student
                studentMWNA = (studentMWNA/studentWN)
                studentSWNA = (studentSWNA/studentWN)
                # Adds average to total to use later in overall calculations
                totalMT += studentMWNA
                totalST += studentSWNA
                # Checks validation
                if studentSWNA > studentMWNA:
                    mostTS = "Scripting"
                elif studentMWNA > studentSWNA:
                    mostTS = "Math"
                else:
                    mostTS = "Same"
                # Adds information to list to be used by tabulate
                studentStats.append([i, studentSWNA, studentMWNA, mostTS])
    # Finds total average and stores it
    totalAvgST = (totalST / studentNum)
    totalAvgMT = (totalMT / studentNum)
    # Prints outcome for most time consuming subject
    if totalAvgMT > totalAvgST:
        mostTST = "Math"
    else:
        mostTST = "Scripting"
    # Prints table using the list and headers specified.
    print(tabulate(studentStats, headers=["Student", "Avg Scripting Time", "Avg Math Time", "Most Time Spent"]))
    # Adds final line to show overall information
    overallL = [["Overall", "{:.2f}".format(totalAvgST), "{:.2f}".format(totalAvgMT), mostTST]]
    print(tabulate(overallL))
    # Ends loop once table prints
    break
