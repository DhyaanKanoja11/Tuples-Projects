## QUESTION

#A bank is a financial institution which is involved in
#borrowing and lending of money. With advancement
#in technology, online banking, also known as
#nternet banking allows customers of a bank to
#conduct a range of financial transactions through
#the bank’s website anytime, anywhere. As part of
#initial investigation you are suggested to
#• collect a bank’s application form. After careful
#analysis of the form, identify the information
#required for opening a savings account. Also
#enquire about the rate of interest offered for a
#saving account.
#• The basic two operations performed on an
#account are Deposit and Withdrawal. Write a
#menu driven program that accepts either of the
#two choices of Deposit and Withdrawal, then
#accepts an amount, performs the transaction
#and accordingly displays the balance.
#Remember, every bank has a requirement of
#minimum balance which needs to be taken care
#of during withdrawal operations. Enquire about
#the minimum balance required in your bank.
#• Collect the interest rates for opening a fixed
#deposit in various slabs in a savings bank
#account. Remember, rates may be different for
#senior citizens.
#Finally, write a menu driven program having the
#following options (use functions and appropriate
#data types):
#• Open a savings bank account
#• Deposit money
#• Withdraw money
#• Take details, such as amount and period for a
#Fixed Deposit and display its maturity amount
#for a particular customer.

account = ()  # Initialize an empty tuple for account details

while True:
    # Display menu options
    print("\nMenu:")
    print("1. Open a savings bank account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Fixed Deposit details")
    print("5. Exit")

    # Get user choice
    choice = int(input("Enter your choice: "))

    # Perform actions based on user choice
    if choice == 1:
        # Open a new account
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        customer_type = input("Enter customer type (General/Senior Citizen): ")
        account = (account_number, initial_balance, customer_type)
        print("Account opened successfully!")
    elif 2 <= choice <= 3:
        # Deposit or Withdraw money
        account_number = input("Enter account number: ")
        amount = float(input(f"Enter the {'deposit' if choice == 2 else 'withdrawal'} amount: "))
        balance, customer_type = account[1], account[2]
        minimum_balance = 1000  # Adjust as per your bank's requirement
        if choice == 3 and balance - amount < minimum_balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            balance = balance + amount if choice == 2 else balance - amount
            account = (account_number, balance, customer_type)
            print(f"{'Deposit' if choice == 2 else 'Withdrawal'} successful. New balance: {balance}")
    elif choice == 4:
        # Calculate and display Fixed Deposit details
        account_number = input("Enter account number: ")
        amount = float(input("Enter the deposit amount for Fixed Deposit: "))
        period = int(input("Enter the period (in years) for Fixed Deposit: "))
        customer_type = input("Enter customer type (General/Senior Citizen): ")
        balance, _ = account[1], account[2]
        interest_rate = 7 if customer_type == 'Senior Citizen' else 5
        maturity_amount = amount + (amount * interest_rate * period / 100)
        print(f"Fixed Deposit details - Amount: {amount}, Period: {period} years")
        print(f"Maturity Amount: {maturity_amount}")
    elif choice == 5:
        # Exit the program
        print("Exiting program. Goodbye!")
        break
    else:
        # Handle invalid choices
        print("Invalid choice. Please try again.")
