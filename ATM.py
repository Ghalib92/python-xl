def get_balance(balance):
    return balance

def withdraw_money(balance):
    try:
        user_amount = int(input("Enter amount to withdraw: "))
        if balance == 0:
            print("Insufficient balance! Please deposit money.")
        elif balance < user_amount:
            print(f"Your balance is less than {user_amount}.")
        else:
            balance -= user_amount
            print(f"You have withdrawn {user_amount}. Your new balance is {balance}.")
    except ValueError:
        print("Please enter a valid number.")
    return balance

def deposit_money(balance):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            balance += amount
            print(f"You have deposited {amount}. Your new balance is {balance}.")
    except ValueError:
        print("Please enter a valid number.")
    return balance

def exit_program():
    print("Thank you for using our services!")
    return False  # Used to break the loop

# Initialize balance
current_balance = 100

# Main program loop
print("Welcome dear customer!")
running = True  # Control variable to keep the loop running
while running:
    print('''
        What service do you want today?
        1. Check balance
        2. Withdraw money
        3. Deposit money
        4. Exit
    ''')
    service = input("Enter service: ")

    if service == '1':
        print(f"Your current balance is: {get_balance(current_balance)}")
    elif service == '2':
        current_balance = withdraw_money(current_balance)
    elif service == '3':
        current_balance = deposit_money(current_balance)
    elif service == '4':
        running = exit_program()  # Exit the program by setting `running` to False
    else:
        print("Invalid option, please try again.")
