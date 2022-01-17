# Kimberly Mazel 2502022250 L1BC
# Algorithm and Programming Final Project

import csv  # module to export to csv
import sys  # to end the program (sys.exit)

class StatementOfFinancialPosition:
    def __init__(self):
        self.assets = 0  # total assets
        self.nonCurrentAssets = 0  # total of non-current assets
        self.currentAssets = 0  # total of current assets

        self.equityLiability = 0  # total equity and liabilities
        self.equity = 0  # total equity
        self.liability = 0  # total liabilities

        self.ncAssetNames = []  # names of non-current assets
        self.ncAssetValues = []  # values of non-current assets

        self.cAssetNames = []  # names of current assets
        self.cAssetValues = []  # values of current assets

        self.equityNames = []  # names of equity
        self.equityValues = []  # values of equity
        self.liabilityNames = []  # names of liabilities
        self.liabilityValues = []  # values of liabilities

        self.input_ncAssets()

    # input methods
    def add_ncAsset(self):
        ncAsset_added = input("Would you like to input a non-current asset? [Y/N]: ").lower()
        return ncAsset_added  # returns the user's response for non-current asset (yes or no)

    def add_cAsset(self):
        cAsset_added = input("Would you like to input a current asset? [Y/N]: ").lower()
        return cAsset_added  # returns the user's response for current asset (yes or no)

    def add_equity(self):
        equity_added = input("Would you like to input an equity? [Y/N]: ").lower()
        return equity_added  # returns the user's response for equity

    def add_liability(self):
        liability_added = input("Would you like to input an liability? [Y/N]: ").lower()
        return liability_added  # returns the user's response for liability

    # function to calculate sum of assets and (equity and liability)
    def sum_assets(self):
        self.nonCurrentAssets = sum(self.ncAssetValues)
        self.currentAssets = sum(self.cAssetValues)
        self.assets = self.nonCurrentAssets + self.currentAssets

    def sum_equityLiability(self):
        self.equity = sum(self.equityValues)
        self.liability = sum(self.liabilityValues)
        self.equityLiability = self.equity + self.liability


    # functions to check if assets, equity and liability has been entered
    def check_ncAssets(self):
        if not bool(self.ncAssetValues):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input non-current asset
            print("No non-current asset has been inputted. Please input at least non-current asset.")
            self.input_ncAssets()
        else:  # if true (list is not empty) return
            return

    def check_cAssets(self):
        if not bool(self.cAssetValues):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input current asset
            print("No current asset has been inputted. Please input at least one current asset.")
            self.input_cAssets()
        else:  # if true (list is not empty) return
            return

    def check_equity(self):
        if not bool(self.equityValues):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input equity
            print("No equity has been inputted. Please input at least one equity.")
            self.input_equity()
        else:  # if true (list is not empty) return
            return

    def check_liability(self):
        if not bool(self.liabilityValues):
            # if a list is empty, the boolean value is false
            # if not true = if list is empty, asks the user to input liability
            print("No liability has been inputted. Please input at least one liability.")
            self.input_liability()
        else:  # if true (list is not empty) return
            return


    # function to input the non-current asset
    def input_ncAssets(self):
        addValue = True
        # while loop that asks the user to input non-current asset until "n" is inputted in add_ncAsset
        while addValue:
            answer = self.add_ncAsset()
            if answer == "y":
                # if the user inputs y (yes) in add_ncAsset
                newncAssetName = str(input("Please enter the name of the source of the non-current asset: "))
                self.ncAssetNames.append(newncAssetName)  # appends the inputted name
                newncAssetAmount = eval(input("Please enter the value of the non-current asset inputted: "))
                self.ncAssetValues.append(newncAssetAmount)  # appends the inputted value
            elif answer == "n":  # user inputs n (no) in add_ncAsset
                self.check_ncAssets()  # calls function that checks if the non-current asset list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        ncAssetName = [name for name in self.ncAssetNames]  # variable for each name in the ncAssetNames list
        ncAssetAmount = [value for value in self.ncAssetValues]  # variable for each amount in ncAssetValues list
        ncAssetDictionary = dict(zip(ncAssetName, ncAssetAmount))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for revenue
        # zip() conjoins ncAssetName and ncAssetValues, pairs respective items (first with first, second with second)

        # for loop to print each ncAsset name and respective value (shows the user a summary of the inputted ncAsset)
        for i in ncAssetDictionary:
            print(i + ": $" + str(ncAssetDictionary[i]))  # output example: Machinery: $1000

        self.input_cAssets()  # calls function for the user to input their current assets

    def input_cAssets(self):
        addValue = True
        # while loop that asks the user to input current asset until "n" is inputted in add_cAsset
        while addValue:
            answer = self.add_cAsset()
            if answer == "y":
                # if the user inputs y (yes) in add_cAsset
                newcAssetName = str(input("Please enter the name of the source of the current asset: "))
                self.cAssetNames.append(newcAssetName)  # appends the inputted name
                newcAssetAmount = eval(input("Please enter the value of the current asset inputted: "))
                self.cAssetValues.append(newcAssetAmount)  # appends the inputted value
            elif answer == "n":  # user inputs n (no) in add_cAsset
                self.check_cAssets()  # calls function that checks if the current asset list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        cAssetName = [name for name in self.cAssetNames]  # variable for each name in the cAssetNames list
        cAssetAmount = [value for value in self.cAssetValues]  # variable for each amount in cAssetValues list
        cAssetDictionary = dict(zip(cAssetName, cAssetAmount))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for revenue
        # zip() conjoins ncAssetName and ncAssetValues, pairs respective items (first with first, second with second)

        # for loop to print each cAsset name and respective value (shows the user a summary of the inputted cAsset)
        for i in cAssetDictionary:
            print(i + ": $" + str(cAssetDictionary[i]))  # output example: Inventories: $2000

        self.sum_assets()
        self.input_equity()  # calls function for the user to input their equity

    def input_equity(self):
        addValue = True
        # while loop that asks the user to input equity until "n" is inputted in add_equity
        while addValue:
            answer = self.add_equity()
            if answer == "y":
                # if the user inputs y (yes) in add_equity
                newEquityName = str(input("Please enter the name of the source of equity: "))
                self.equityNames.append(newEquityName)  # appends the inputted name
                newEquityAmount = eval(input("Please enter the value of the equity inputted: "))
                self.equityValues.append(newEquityAmount)  # appends the inputted value
            elif answer == "n":  # user inputs n (no) in add_equity
                self.check_ncAssets()  # calls function that checks if the equity list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        equityName = [name for name in self.equityNames]  # variable for each name in the ncAssetNames list
        equityAmount = [value for value in self.equityValues]  # variable for each amount in ncAssetValues list
        equityDictionary = dict(zip(equityName, equityAmount))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for revenue
        # zip() conjoins ncAssetName and ncAssetValues, pairs respective items (first with first, second with second)

        # for loop to print each equity name and respective value (shows the user a summary of the inputted equity)
        for i in equityDictionary:
            print(i + ": $" + str(equityDictionary[i]))  # output example: Retained Earnings: $400

        self.input_liability()  # calls function for the user to input their liability

    def input_liability(self):
        addValue = True
        # while loop that asks the user to input non-current asset until "n" is inputted in add_liability
        while addValue:
            answer = self.add_liability()
            if answer == "y":
                # if the user inputs y (yes) in add_ncAsset
                newLiabilityName = str(input("Please enter the name of the source of liability: "))
                self.liabilityNames.append(newLiabilityName)  # appends the inputted name
                newLiabilityAmount = eval(input("Please enter the value of the liability inputted: "))
                self.liabilityValues.append(newLiabilityAmount)  # appends the inputted value
            elif answer == "n":  # user inputs n (no) in add_liability
                self.check_liability()  # calls function that checks if the liability list is empty
                addValue = False  # addValue becomes false, while loop stops
            else:  # prevents user from entering any other answers (random words not allowed, only Y or N)
                print("Please only enter 'Y' or 'N' to decide.")

        liabilityName = [name for name in self.liabilityNames]  # variable for each name in the liabilityNames list
        liabilityAmount = [value for value in self.liabilityValues]  # variable for each amount in liabilityValues list
        liabilityDictionary = dict(zip(liabilityName, liabilityAmount))  # dictionary of each name and respective amount
        # dict() used to create a dictionary of the name and respective amount for liability
        # zip() conjoins liabilityNames and liabilityAmount, pairs respective items

        # for loop to print each ncAsset name and respective value (shows the user a summary of the inputted liability)
        for i in liabilityDictionary:
            print(i + ": $" + str(liabilityDictionary[i]))  # output example: Accrued Expense: $700

        self.sum_equityLiability()
        self.balanced()

    def balanced(self):
        print("The total inputted assets are: $" + str(self.assets))
        print("The total inputted equity and liabilities are: $" + str(self.equityLiability))

        if self.assets == self.equityLiability:
            print("The statement of financial position is balanced.")
        elif self.assets > self.equityLiability:
            print("The statement of financial position is unbalanced.")
            print("The total inputted assets is greater than the total inputted equity and liabilities.")
        elif self.assets < self.equityLiability:
            print("The statement of financial position is unbalanced.")
            print("The total inputted equity and liability is greater than the total inputted assets.")

        self.askexport()

    def askexport(self):  # function that asks the user if they want to export the data to a csv file
        csv_export = input("Do you want to export the data as a CSV file? [Y/N]: ").lower()

        if csv_export == "y":  # if user enters y (yes), they want to export the data to a csv file
            self.exportcsv()  # calls function that exports it to a csv file
        elif csv_export == "n":  # if user enters n (no), they do not want to export to a csv file
            self.newsofp()  # calls function that asks if they want to run another calculation
        else:  # ensures that user can only enter y or n (no random words)
            print("Please only enter 'Y' or 'N' to decide.")
            self.askexport()  # calls function again (asks the user again)

    def exportcsv(self):
        sofp = open("SOFPCSV.csv", "w")  # opening test file for csv, can be changed, write method
        writer = csv.writer(sofp)

        writer.writerow(["Statement of Financial Position"])
        writer.writerow("")
        writer.writerow(["ASSETS"])
        writer.writerow(["Non-current assets"])

        for i in range(len(self.ncAssetValues)):
            writer.writerow([self.ncAssetNames[i], self.ncAssetValues[i]])
        writer.writerow(["", self.nonCurrentAssets])

        writer.writerow(["Current assets"])

        for j in range(len(self.cAssetValues)):
            writer.writerow([self.cAssetNames[j], self.cAssetValues[j]])
        writer.writerow(["", self.currentAssets])

        writer.writerow(["Total assets", self.assets])
        writer.writerow("")
        writer.writerow(["EQUITY AND LIABILITIES"])
        writer.writerow(["Equity"])

        for k in range(len(self.equityValues)):
            writer.writerow([self.equityNames[k], self.equityValues[k]])
        writer.writerow(["", self.equity])

        writer.writerow("")
        writer.writerow(["Liabilities"])

        for l in range(len(self.liabilityValues)):
            writer.writerow([self.liabilityNames[l], self.liabilityValues[l]])
        writer.writerow(["", self.liability])

        writer.writerow("")
        writer.writerow(["Total equity and liabilities", self.equityLiability])

        sofp.close()
        self.newsofp()

    def newsofp(self):
        repeatprocess = input("Do you want to run another calculation? [Y/N]: ").lower()

        if repeatprocess == "y":
            self.programreset()  # if yes, calls function that resets the program and runs it again
        elif repeatprocess == "n":
            self.programclose()  # if no, calls function that ends the program
        else:  # ensures that user can only enter y or n (no random words)
            print("Please only enter 'Y' or 'N' to decide.")
            self.newsofp()  # calls function again (asks the user again)


    # function that resets the values and runs the program again
    def programreset(self):
        # resets variables to 0
        self.assets = 0
        self.nonCurrentAssets = 0
        self.currentAssets = 0
        self.equityLiability = 0
        self.equity = 0
        self.liability = 0

        # del used to delete objects in list, 0: deletes all objects
        del self.ncAssetNames[0:]
        del self.ncAssetValues[0:]
        del self.cAssetNames[0:]
        del self.cAssetValues[0:]
        del self.equityNames[0:]
        del self.equityValues[0:]
        del self.liabilityNames[0:]
        del self.liabilityValues[0:]

        print("Running the program again...")
        self.input_ncAssets()  # calls first function

    # function that closes the program
    def programclose(self):
        print("Now exiting the program. Thank you for using it.")  # closing message for user
        sys.exit(0)  # sys function that exits the program (0 = successful termination)
