balance = 1000  # Global variable

def deposit(amount):
    global balance
    balance += amount
    print("Deposited Amount:", amount)
    print("Updated Balance:", balance)

def show_balance():
    balance = 500  # Local variable
    print("Local Balance:", balance)

deposit(500)
show_balance()

print("Actual Bank Balance:", balance)