#!/usr/bin/python
# Imports tabulate to create table at the end
from tabulate import tabulate


# Creates customer class
class Customer:
    # Creates customer constructor with name and opening balance
    def __init__(self, name, openingBalance):
        self.customerType = None
        self.name = name
        self.openingBalance = openingBalance

    # A method to calculate the closing balance for the customer using opening balance and the customer interest
    def calculateClosingBalance(self):
        openingBalance = self.openingBalance
        customerInterest = 0.125
        self.customerInterestAmount = (openingBalance * customerInterest)
        self.closingB = openingBalance + self.customerInterestAmount
        return self.closingB

    # A method to determine the type of customer based on closing balance.
    def determineCustomerType(self):
        if self.closingB >= 150000:
            self.customerType = "Diamond"
        elif 150000 > self.closingB >= 100000:
            self.customerType = "Gold"
        elif 100000 > self.closingB >= 90000:
            self.customerType = "Silver"
        elif self.closingB < 90000:
            self.customerType = "Bronze"
        return self.customerType

    # Returns all the customers information to be used by the table
    def displayInfo(self):
        return self.name, self.customerType, self.openingBalance, self.customerInterestAmount, self.closingB


# The main method to run the entire code given the sequence.
def main():
    # Asks the user to input the number of customers at the bank.
    customerNum = int(input("Enter the number of customers you have in this bank? "))
    # Initializes the dictionary for the temporary customer class creation
    cDict = {}
    # A loop to validate the input per customer
    while 1:
        for i in range(1, customerNum + 1):
            # Two lines asking the user for customer name and opening balance.
            name = str(input("Enter customer " + str(i) + "'s name: "))
            openingBalance = float(input("Enter customer " + str(i) + "'s opening balance: "))
            # Validates the opening balance to make sure minimum deposit is met.
            while openingBalance < 50:
                print("Invalid Input: Minimum of $50 Opening Balance. ")
                openingBalance = float(input("Enter customer " + str(i) + "'s opening balance: "))
            else:
                cDict["customer{0}".format(i)] = Customer(name, openingBalance)
        break
    # Creates a table to store the object in
    customerTable = []
    # This loop calls the methods for calculation purposes and adds the information to the customer table
    for j in range(1, customerNum + 1):
        cDict["customer{0}".format(j)].calculateClosingBalance()
        cDict["customer{0}".format(j)].determineCustomerType()
        customerTable.append(cDict["customer{0}".format(j)].displayInfo())
    # Uses the customer table to make the table as well as formatting it with the given headers and decimal points.
    print(tabulate(customerTable, headers=["Name", "Customer Type", "Opening Balance($)", "Interest($)", "Closing($)"],
                   floatfmt=".2f"))


main()
