# Create a sample dictionary
student = {
    "name": "Jahnavi",
    "age": 18,
    "course": "B.Tech"
}

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())

# Display all key-value pairs
print("Items:", student.items())

# Get a value using get()
print("Name:", student.get("name"))

# Update dictionary
student.update({"age": 19, "city": "Mudinepalli"})
print("After Update:", student)

# Remove an item using pop()
student.pop("course")
print("After Pop:", student)