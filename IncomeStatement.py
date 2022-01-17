# Kimberly Mazel 2502022250 L1BC
# Algorithm and Programming Final Project

import csv  # used to export the data to a csv file
import sys  # used for sys.exit
import matplotlib.pyplot as plot  # for displaying bar graph

class CreateIncomeStatement:
    def __init__(self):
        self.revenue = 0  # amount of total revenue that the user has (default set to 0)
        self.expense = 0  # amount of total expenses that the user has (default set to 0)

        self.revenueNames = []  # empty list for the names of each revenue the user will input
        self.revenueAmount = []  # empty list for the amount of each revenue the user will input

        self.expenseNames = []  # empty list for the names of each expense the user will input
        self.expenseAmount = []  # empty list for the amount of each expense the user will input

        self.difference = 0  # difference between the revenue and expenses (determines profit/loss)
        self.status = "n/a"  # status of the difference (profit / loss / broken even)

        self.input_revenue()  # starts the calculation process
        # starts from input_revenue() to input_expense() to profitloss()
        # input_revenue() calls input_expense() which calls profitloss()

    # input methods
    def add_revenue(self):  # asks the user if they want to input an revenue
        revenue_added = input("Would you like to input a revenue? [Y/N]: ").lower()
        return revenue_added  # returns the user's response for revenue (yes or no)

    def add_expense(self):  # asks the user if they want to input an expense
        expense_added = input("Would you like to input an expense? [Y/N]: ").lower()
        return expense_added  # returns the user's response for expenses (yes or no)

    # functions to calculate the sum of the revenue and expenses
    def sum_revenue(self):
        self.revenue = sum(self.revenueAmount)  # updates self.revenue with the sum of the inputted revenues

    def sum_expense(self):
        self.expense = sum(self.expenseAmount)  # updates self.expense with the sum of the inputted expenses

    # functions to check that both revenue and expenses are inputted
    def check_revenue(self):
        if not bool(self.revenueAmount):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input revenue if revenueAmount is empty
            print("No revenue has been inputted. Please input at least one revenue.")
            self.input_revenue()
        else:  # if true (list is not empty) return
            return

    def check_expense(self):
        if not bool(self.expenseAmount):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input expense if expenseAmount is empty
            print("No expense has been inputted. Please input at least one expense.")
            self.input_expense()
        else:  # if true (list is not empty) return
            return

    # function to input the revenue
    def input_revenue(self):
        addValue = True
        # while loop to continue asking the user to input name and value of revenue until user inputs "n" in add_revenue
        while addValue:
            answer = self.add_revenue()
            if answer == "y":
                # if the user inputs y (yes) in add_revenue (asks the user if they want to add revenue)
                newrevenueName = str(input("Please enter the name of the source of revenue: "))
                self.revenueNames.append(newrevenueName)  # appends the inputted name to the list of revenue names
                newrevenueAmount = eval(input("Please enter the value of the revenue inputted: "))
                self.revenueAmount.append(newrevenueAmount)  # appends the inputted value to the list of revenue amounts
            elif answer == "n":  # user inputs n (no) in add_revenue (asks the user if they want to input revenue)
                self.check_revenue()  # calls function that checks if the revenue list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        revenueName = [name for name in self.revenueNames]  # variable for each name in the revenueNames list
        revenueValue = [value for value in self.revenueAmount]  # variable for each amount in revenueAmount list
        revenueDictionary = dict(zip(revenueName, revenueValue))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for revenue
        # zip() conjoins revenueName and revenueValue, pairs respective items (first with first, second with second)

        # for loop to print each revenue name and respective value (shows the user a summary of the inputted revenue)
        for i in revenueDictionary:
            print(i + ": $" + str(revenueDictionary[i]))  # output example: Labour: $1000

        self.sum_revenue()  # calls function to calculate the sum of the revenue inputted
        print("The total inputted revenue is: $" + str(self.revenue))  # prints the total revenue for the user to see
        self.input_expense()  # calls function for the user to input their expense

    # function for the user to input their expense
    def input_expense(self):
        addValue = True
        # while loop to continue asking the user to input name and value of expense until user inputs "n" in add_expense
        while addValue:
            answer = self.add_expense()
            if answer == "y":
                # if the user inputs y (yes) in add_expense (asks the user if they want to add expense)
                newExpenseName = str(input("Please enter the name of the source of expense: "))
                self.expenseNames.append(newExpenseName)  # appends the inputted name to the list of expense names
                newExpenseAmount = eval(input("Please enter the value of the expense inputted: "))
                self.expenseAmount.append(newExpenseAmount)  # appends the inputted value to the list of expense amounts
            elif answer == "n":  # user inputs n (no) in add_expense (asks the user if they want to input expense)
                self.check_expense()  # calls function that checks if the expense list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        expenseName = [name for name in self.expenseNames]  # variable for each name in the expenseNames list
        expenseValue = [value for value in self.expenseAmount]  # variable for each amount in expenseAmount list
        expenseDictionary = dict(zip(expenseName, expenseValue))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for expense
        # zip() conjoins expenseName and expenseValue, pairs respective items (first with first, second with second)

        # for loop to print each expense name and respective value (shows the user a summary of the inputted expense)
        for i in expenseDictionary:
            print(i + ": $" + str(expenseDictionary[i]))  # output example: Employee Wages: $700

        self.sum_expense()  # calls function to calculate the sum of the expense inputted
        print("The total inputted expense is: $" + str(self.expense))  # prints the total expense for the user to see
        self.profitloss()  # calls function to calculate the profit or loss

    def profitloss(self):  # function to determine the difference and if it's a profit or loss (or broken even)
        self.difference = self.revenue - self.expense

        # summary of revenue and expense displayed to user
        print("Total revenue: $" + str(self.revenue))
        print("Total expense: $" + str(self.expense))

        if self.difference > 0:
            print("You have a profit of $" + str(self.difference))
            self.status = "Profit"  # changes the status to profit
        elif self.difference < 0:
            print("You have a loss of $" + str(abs(self.difference)))
            # abs() makes the difference absolute so when printed the number isn't negative
            self.status = "Loss"  # changes the status to loss
        else:
            print("There is no difference between your revenue and expense. You have a broken even.")
            self.status = "Broken Even"  # changes the status to broken even

        self.askexport()  # calls function for csv file export confirmation

    def askexport(self):  # function that asks the user if they want to export the data to a csv file
        csv_export = input("Do you want to export the data as a CSV file? [Y/N]: ").lower()

        if csv_export == "y":  # if user enters y (yes), they want to export the data to a csv file
            self.exportcsv()  # calls function that exports it to a csv file
        elif csv_export == "n":  # if user enters n (no), they do not want to export to a csv file
            self.createchart()  # calls function that asks if they want to run another calculation
        else:  # ensures that user can only enter y or n (no random words)
            print("Please only enter 'Y' or 'N' to decide.")
            self.askexport()  # calls function again (asks the user again)

    def exportcsv(self):
        headerrevenue = ["Revenue Name", "Revenue Value"]  # header for the revenue section in csv file
        headerExpense = ["Expense Name", "Expense Value"]  # header for the expense section in csv file
        totalrevenue = ["Total Revenue", self.revenue]
        totalExpense = ["Total Expense", self.expense]
        profitLoss = [self.status, abs(self.difference)]  # profit/loss and the value
        # output example: Profit 700

        namerevenue = self.revenueNames  # list for revenue names
        valuerevenue = self.revenueAmount  # list for revenue values
        nameExpense = self.expenseNames  # list for expense names
        valueExpense = self.expenseAmount  # list for expense values

        file = open("IncomeCSV.csv", "w")  # opening test file for csv, can be changed, write method
        writer = csv.writer(file)

        revenueLength = len(namerevenue)  # length of revenue list (number of revenue inputted)
        expenseLength = len(nameExpense)  # length of expense list (number of expense inputted)

        writer.writerow(headerrevenue)  # writes revenue header

        # for loop that writes the name and respective value for each revenue by row
        # output example:
        # Wages 1000
        # Sales 200
        for i in range(revenueLength):  # for length of revenue (loops until all revenue is written)
            writer.writerow([namerevenue[i], valuerevenue[i]])
            # writes the name and the respective value of each revenue

        writer.writerow(totalrevenue) # writes total revenue
        writer.writerow("")  # row break to separate revenue and expense

        writer.writerow(headerExpense)  # writes expense header

        # for loop that writes the name and respective value for each expense by row
        # output example:
        # Rent 700
        # Electricity 150
        for j in range(expenseLength):  # for length of expense (loops until all expenses are written)
            writer.writerow([nameExpense[j], valueExpense[j]])  # writes the name and the respective value of expense

        writer.writerow(totalExpense)  # writes total expense
        writer.writerow("")  # row break to separate expense and profit/loss

        writer.writerow(profitLoss)  # writes the status (profit/loss/broken even) and the value (revenue - expense)

        file.close()  # closes the file
        self.createchart()  # calls the function that asks the user if they want to create a chart

    def createchart(self):
        makechart = input("Do you want to compare your revenue and expense through a bar chart? [Y/N]: ").lower()

        if makechart == "y":
            self.revenueExpenseChart()  # if yes, calls function that creates and shows chart
        elif makechart == "n":
            self.newbudget()  # if no, calls function asks the user if they want to run the program again
        else:  # ensures that user can only enter y or n (no random words)
            print("Please only enter 'Y' or 'N' to decide.")
            self.createchart()  # calls function again (asks the user again)

    def newbudget(self):  # function that asks the user if they want to do another calculation
        repeatprocess = input("Do you want to run another calculation? [Y/N]: ").lower()

        if repeatprocess == "y":
            self.programreset()  # if yes, calls function that resets the program and runs it again
        elif repeatprocess == "n":
            self.programclose()  # if no, calls function that ends the program
        else:  # ensures that user can only enter y or n (no random words)
            print("Please only enter 'Y' or 'N' to decide.")
            self.newbudget()  # calls function again (asks the user again)

    # function that creates and shows a chart comparing the user's revenue and expenses
    def revenueExpenseChart(self):
        dataset = {"Revenue": self.revenue, "Expenses": self.expense}  # dictionary of total revenue and expenses
        xvalue = list(dataset.keys())  # list containing keys of dictionary (x values)
        yvalue = list(dataset.values())  # list containing values of dictionary (y values)

        plot.bar(xvalue, yvalue, width=0.5)
        # plots the revenue/expenses with their respective values
        # width of each bar is 0.5

        plot.ylabel("Amount of Money")  # label for y value
        plot.title("Comparison of Revenue and Expenses")  # title of chart

        plot.show()  # shows chart

        self.newbudget()  # calls function that asks if user wants to run the program again

    # function that resets the values and runs the program again
    def programreset(self):
        self.revenue = 0  # resets total revenue to 0
        self.expense = 0  # resets total expense to 0

        # del used to delete objects in list, 0: deletes all objects
        del self.revenueNames[0:]  # deletes all revenue names inputted
        del self.revenueAmount[0:]  # deletes all revenue values inputted
        del self.expenseNames[0:]  # deletes all expense names inputted
        del self.expenseAmount[0:]  # deletes all expense values inputted

        print("Running the program again...")
        self.input_revenue()  # calls function that asks the user if they want to input an revenue (starts process)

    # function that closes the program
    def programclose(self):
        print("Now exiting the program. Thank you for using it.")  # closing message for user
        sys.exit(0)  # sys function that exits the program (0 = successful termination)
