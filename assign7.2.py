balance = 0

def show_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

while True:
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 4:
        break

    if ch == 1:
        show_balance()
    elif ch == 2:
        amt = float(input("Enter amount: "))
        deposit(amt)
    elif ch == 3:
        amt = float(input("Enter amount: "))
        withdraw(amt)
    else:
        print("Invalid choice")