# Create a list of student dictionaries
students = [
    {"name": "Jahnavi", "marks": 95},
    {"name": "Rahul", "marks": 80},
    {"name": "Priya", "marks": 90},
    {"name": "Arun", "marks": 75}
]

# Sort in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

# Sort in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

# Display results
print("Ascending Order:")
for student in ascending:
    print(student)

print("\nDescending Order:")
for student in descending:
    print(student)