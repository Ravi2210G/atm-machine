import time  # Importing time module to use the sleep function for simulating card processing

# Prompt user to insert their card (simulated)
print("Please insert Your CARD")

# Simulating the card processing delay with a 5-second pause
time.sleep(5)

# Predefined ATM PIN (this would usually be securely stored and checked against user input)
password = 1234

# Prompt the user to enter their ATM PIN
pin = int(input("Enter your ATM pin: "))

# User's initial account balance (for demonstration purposes)
balance = 5000

# Check if the entered PIN is correct
if pin == password:
    # If the PIN is correct, enter a loop to allow the user to perform multiple transactions
    while True:

        # Displaying the options available to the user
        print(""" 
        1 == Check Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Exit
        """)

        try:
            # Prompt the user to choose an option from the menu
            option = int(input("Please enter your choice: "))
        except ValueError:
            # Handle the case where the user inputs something other than a number
            print("Please enter a valid option")
            continue  # Restart the loop and prompt the user again

        # Option 1: Check the current balance
        if option == 1:
            print(f"Your current balance is {balance}")

        # Option 2: Withdraw money from the account
        elif option == 2:
            # Prompt the user to enter the amount they wish to withdraw
            withdraw_amount = int(input("Please enter the amount to withdraw: "))

            # Check if the user has enough balance to withdraw the entered amount
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                # Deduct the withdrawal amount from the balance
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your new balance is {balance}")

        # Option 3: Deposit money into the account
        elif option == 3:
            # Prompt the user to enter the amount they wish to deposit
            deposit_amount = int(input("Please enter the amount to deposit: "))
            # Add the deposit amount to the balance
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your new balance is {balance}")

        # Option 4: Exit the program
        elif option == 4:
            print("Thank you for using our ATM. Have a nice day!")
            break  # Exit the loop and end the program

        else:
            # Handle invalid options
            print("Invalid option. Please try again.")

else:
    # If the entered PIN is incorrect, display an error message
    print("Incorrect PIN. Please try again.")