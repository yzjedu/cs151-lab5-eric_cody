# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

# 1. Display Purpose: To make ATM that a user can deposit, withdraw, or view their balance
# 2. Set initial_value to 1000
# 3. Set total_value to 1000
# 4. Prompt user to select D: Deposit, W: Withdraw, V: View Balance, or E: Exit,store under decision
    a. use .upper() and .lower() so capitalization doesn't matter
# 5. Set the SENTINEL to E
# 6. While decision != E
    i. if decision == D:
        a. Prompt user to enter the amount they wish to deposit, deposit_value
            if deposit_value < 0
                display to user ("Enter a valid value to deposit")

    ii. Add deposit_value to initial_value, store under total_value
        
    iii. Display total_value to user
        a. if total_value < 0:
            display to user (WARNING: You will be charged 5% interest if your balance is under $0.")

    IV. otherwise if decision == W:
        a. Prompt user to enter the amount they wish to withdraw, withdraw_value
            if deposit_value < 0
                display to user ("Enter a valid value to deposit")

    V. Add withdraw_value to initial_value, store under total value

    VI. Display total_value to user
         if total_value < 0:
             display to user (WARNING: You will be charged 5% interest if your balance is under $0.")

    VII otherwise if decision == V
        a. Display to user total_value

    VII otherwise 
        a. Display to user ("Enter a valid interaction")
        
    