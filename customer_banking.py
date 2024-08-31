# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("We are going to create a savings account!")
    while True:
        savings_balance_input = input("Enter your starting savings balance ")
        if savings_balance_input.isdigit():
            savings_balance = float(savings_balance_input)
            break
        else:
            print("Please enter a digit")
    
    while True:
        savings_interest_rate = input("Enter your Interest Rate ")
        if savings_interest_rate.isdigit():
            savings_interest = float(savings_interest_rate)
            break
        else:
            print("Please enter a digit")

    while True:
        savings_months_input = input("Enter the months you'll be saving in this account ")
        if savings_months_input.isdigit():
            savings_maturity = int(savings_months_input)
            break
        else:
            print("Please enter a digit")
    


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"From your Savings Account you earned ${interest_earned: ,.2f} and have an ending balance of ${updated_savings_balance: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    print("Now we will create a CD account")

    while True:
        cd_balance_input = input("Enter your starting CD balance ")
        if cd_balance_input.isdigit():
            cd_balance = float(cd_balance_input)
            break
        else:
            print("Please enter a digit")
    
    while True:
        cd_interest_rate = input("Enter your Interest Rate ")
        if cd_interest_rate.isdigit():
            cd_interest = float(cd_interest_rate)
            break
        else:
            print("Please enter a digit")

    while True:
        cd_months_input = input("Enter the months you'll be saving in this CD ")
        if cd_months_input.isdigit():
            cd_maturity = int(savings_months_input)
            break
        else:
            print("Please enter a digit")


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"From your CD account, you will earn ${interest_earned:,.2f} and your ending balance will be ${updated_cd_balance:,.2f}" )

if __name__ == "__main__":
    main()