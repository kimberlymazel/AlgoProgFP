# Kimberly Mazel 2502022250 L1BC
# Algorithm and Programming Final Project

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot

# watched some videos on machine learning and used the article below for reference
# https://towardsdatascience.com/machine-learning-simple-linear-regression-with-python-f04ecfdadc13

def SalaryPrediction():
    experience = eval(input("Please enter your years of experience: "))
    user_input = np.array(experience).reshape(-1, 1)

    # importing the dataset (csv file from kaggle for salary and years of experience)
    data = pd.read_csv("Salary_Data.csv")
    x = data.iloc[:, :1].values  # dataset dropping the last column (years of experience only)
    y = data.iloc[:, 1:].values  # dataset in the last column (salary)

    # training the data
    # test_size = 0.2, 20% of the data is used for testing
    # remaining 0.8 of the data is used for training
    # random_state = seed for random number generator to test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # because of the positive correlation, we use linear regression to predict
    # regression = modelling target value based on independent processors
    linreg = LinearRegression()
    linreg.fit(x_train, y_train)  # predicts based on x_train and y_train variables
    predict = int(linreg.predict(user_input))  # gives the output of y (salary) based on x (user's years of experience)

    # graph to see the train data
    plot.scatter(x_train, y_train, color="blue")  # scatter graph for the salary values
    plot.plot(x_train, linreg.predict(x_train), color='black')  # line to show the trained data correlation
    plot.xlabel("Years of Experience")  # label for x value
    plot.ylabel("Salary Amount")  # label for y value
    plot.title("Training Data")  # title of graph

    # graph to see the test data
    plot.scatter(x_test, y_test, color="red")  # scatter graph for test salary values (not trained)
    plot.plot(x_train, linreg.predict(x_train), color='black')  # trained data line (see how close the test values are)
    plot.xlabel("Years of Experience")  # x values label
    plot.ylabel("Salary Amount")  # y values label
    plot.title("Test Data")  # title of graph

    # the graphs were just for me to see if the trained data was valid, thus plot.show() was deleted (doesnt show user)

    # prints the summary data and predicted salary in dollars
    print("You have " + str(experience) + " years of experience.")
    print("Based on researched data, your predicted salary is around $" + str(predict))
