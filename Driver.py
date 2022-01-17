# Kimberly Mazel 2502022250 L1BC
# Algorithm and Programming Final Project

from IncomeStatement import CreateIncomeStatement  # imports class that creates income statement
from PredictSalary import SalaryPrediction  # imports function that predicts salary
from SOFP import StatementOfFinancialPosition  # imports class that creates statement of financial position

def askUser():
    # input from user on what they want to choose
    statement = input("What would you like to choose? [A/B/C]: ").lower()

    # if statement to determine the actions that follow the user's choice
    # if user selects a (income statement)
    if statement == "a":
        # tells the user what they selected
        print("Income Statement has been selected. Program is starting...")
        # calls the function from another file to start the income statement process
        CreateIncomeStatement()

    # if the user selects b (statement of financial position)
    elif statement == "b":
        # tells the user what they selected
        print("Statement of Financial Position has been selected. Program is starting...")
        StatementOfFinancialPosition()

    # if the user selects c (salary prediction)
    elif statement == "c":
        # tells the user that they selected salary prediction
        print("Salary Prediction has been selected. Program is starting...")
        # calls the function from another file that predicts the salary based on years of experience
        SalaryPrediction()

    # if the user inputs anything else outside choices (validation)
    else:
        # tells the user to only input A, B or C
        print("Please only select from the options available. [A/B/C].")
        # calls the function again (repeat process)
        askUser()


# displays the available programs to the user
print("Here are the available statements that can be made:")
print("A: Income Statement")
print("B: Statement of Financial Position")
print("C: Salary Prediction")
askUser()  # calls the function that gets the input from the user
