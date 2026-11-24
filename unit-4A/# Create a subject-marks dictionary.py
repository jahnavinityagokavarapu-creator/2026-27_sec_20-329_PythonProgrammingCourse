# Create a subject-marks dictionary
subjects = {
    "Python": 95,
    "Maths": 90,
    "English": 85,
    "Physics": 88
}

# Print keys
print("Subject Names:")
for key in subjects.keys():
    print(key)

# Print values
print("\nSubject Marks:")
for value in subjects.values():
    print(value)

# Print items
print("\nSubject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)