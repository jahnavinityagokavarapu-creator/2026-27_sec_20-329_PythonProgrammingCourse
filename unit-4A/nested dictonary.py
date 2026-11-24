# Create a nested dictionary
students = {
    1: {"name": "Jahnavi", "marks": 95},
    2: {"name": "Rahul", "marks": 88},
    3: {"name": "Priya", "marks": 92}
}

# Print student names and marks
print("Student Details:")

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()