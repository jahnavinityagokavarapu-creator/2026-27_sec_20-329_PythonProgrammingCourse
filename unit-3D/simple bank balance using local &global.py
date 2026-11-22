balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited Amount:", amount)
    print("Updated Balance:", balance)

def show_balance():
    balance = 500
    print("Local Balance:", balance)

print("Initial Balance:", balance)

deposit(500)

show_balance()

print("Final Bank Balance:", balance)