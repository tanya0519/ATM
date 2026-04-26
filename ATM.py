# display menu
def show_menu():
    print("ATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Statement")
    print("5. Exit")


# check balance
def check_balance(bal):
    print("Current Balance: Rs.", bal)


# deposit money
def deposit(bal, trans):
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        bal += amount
        trans.append("Deposited: ₹" + str(amount))
        print("Deposit successful")
    else:
        print("Invalid amount")
    
    return bal


# withdraw money
def withdraw(bal, trans):
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount")
    elif amount > bal:
        print("Insufficient balance")
    else:
        bal -= amount
        transactions.append("Withdrawn: Rs." + str(amount))
        print("Withdrawal successful")
    
    return bal


# show transactions
def show_statement(trans):
    print("\n Transaction Statement ")
    
    if not trans:
        print("No transactions yet")
    else:
        for t in trans:
            print(t)


# Main program
bal = 0
trans = []

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance(bal)

    elif choice == '2':
        bal = deposit(bal, trans)

    elif choice == '3':
        bal = withdraw(bal, trans)

    elif choice == '4':
        show_statement(trans)

    elif choice == '5':
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice")