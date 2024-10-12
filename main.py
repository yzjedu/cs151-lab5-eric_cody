
# Programmers: Cody and Eric
# Course: CS151, Professor Zee
# Due Date: October 16th, 2024
# Lab Assignment: Lab 05
# Problem Statement: Build a simulation of an ATM where users can view balance, deposit money, or withdraw money
# Data In:
# Data Out:
# Credits:


#Purpose of the lab
print('This is an working virtual ATM which you can use to view your balance, deposit money, or withdraw money')

#Set Initial Balance to $1000
initial_value = 1000

#Set Total Balance to $1000
total_value = 1000

#Prompt user to select deposit, withdraw, view balance or to exit
decision = input('Please enter D for deposit, W, for withdraw, V for viewing balance, or E to exit: ')
decision = decision.upper()

#While loop for decision
while decision != "E":

    if decision == "D":
            deposit_value = input('Enter value you wise to deposit: ')
            deposit_value =float(deposit_value)
            if deposit_value < 0:
                print('Please enter a positive value')
            elif deposit_value >= 0:
                total_value = total_value + deposit_value
                total_value = float(total_value)
                print('Balance: ', total_value)
                if total_value < 0:
                    print('WARNING: You will be charged 5% interest of your balance is under $0')
    elif decision == "W":
            withdraw_value = input('Enter value you wise to withdraw: ')
            withdraw_value = float(withdraw_value)
            if withdraw_value < 0:
                print('Please enter a positive value')
            elif withdraw_value >= 0:
                total_value = total_value - withdraw_value
                total_value = float(total_value)
                print('Balance: ', total_value)
                if total_value < 0:
                    print('WARNING: You will be charged 5% interest of your balance is under $0')
    elif decision == "V":
            print('Balance: ', total_value)
    else:
            print('Enter a valid interaction')

    decision = input('Please enter D for deposit, W, for withdraw, V for viewing balance, or E to exit: ')
    decision = decision.upper()