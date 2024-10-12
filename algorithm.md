# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

# 1. Display Purpose: To make ATM that a user can deposit, withdraw, or view their balance
# 2. Set initial_value to 1000
# 3. Set total_value to 1000
# 4. Prompt user to select D: Deposit, W: Withdraw, V: View Balance, or E: Exit,store under decision
    a. use .upper() so capitalization doesn't matter
# 5. Set the SENTINEL to E
# 6. While decision != E
    i. if decision == D:
        a. Prompt user to enter the amount they wish to deposit, deposit_value
            i. convert deposit_value to float
            ii. if deposit value < 0
                    output to user to select a positive value
                 otherwise if deposit value >= 0
                    i. add deposit value to total value
                    ii. convert total value to float
                    iii. output to user their balance
        b. if total value < 0
            output to user "WARNING: You will be charged 5% interest if your balance is under $0.")


    ii. otherwise if decision == W:
        a. Prompt user to enter the amount they wish to withdraw, withdraw_value
            i. convert withdraw_value to float
            ii. if withdraw_value < 0
                    output to user to select a positive value
                 otherwise if withdraw_value >= 0
                    i. subtract withdraw value from total value
                    ii. convert total value to float
                    iii. output to user their balance

        b. if total value < 0
            output to user "WARNING: You will be charged 5% interest if your balance is under $0.")

    iii. otherwise if decision == V
        a. Display to user total_value

    iv. otherwise 
        a. Display to user ("Enter a valid interaction")

    v. Prompt user to select D: Deposit, W: Withdraw, V: View Balance, or E: Exit,store under decision
        a. use .upper() so capitalization doesn't matter
        
    