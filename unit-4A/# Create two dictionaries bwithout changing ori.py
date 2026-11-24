# Create two dictionaries
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Create a copy of the first dictionary
merged = dict1.copy()

# Merge second dictionary into the copy
merged.update(dict2)

# Display dictionaries
print("Original Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged)