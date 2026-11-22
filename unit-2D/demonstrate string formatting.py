name = "Jahnavi"
age = 18
marks = 95.5

# Using format()
print("Using format():")
print("My name is {} and my age is {}".format(name, age))

# Using f-string
print("\nUsing f-string:")
print(f"My name is {name} and my age is {age}")

# Using % operator
print("\nUsing % operator:")
print("My name is %s and my age is %d" % (name, age))

# Formatting decimal values
print("\nMarks: {:.2f}".format(marks))
print(f"Marks: {marks:.2f}")
print("Marks: %.2f" % marks)