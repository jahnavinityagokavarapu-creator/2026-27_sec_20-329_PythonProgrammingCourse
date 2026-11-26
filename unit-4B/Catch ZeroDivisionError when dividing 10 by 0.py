# Example solution: try-except block
try:
    a =int(input("enter a value"))
    b =int(input("enter a value"))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")