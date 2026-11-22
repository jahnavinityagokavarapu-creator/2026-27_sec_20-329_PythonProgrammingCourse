# Creating a set
my_set = {10, 20, 30, 40, 50}

print("Original Set:", my_set)

# Membership testing
print("Is 20 present?", 20 in my_set)
print("Is 60 present?", 60 in my_set)

# Adding an element
my_set.add(60)
print("After add():", my_set)

# Removing an element
my_set.remove(30)
print("After remove():", my_set)

# Discarding an element
my_set.discard(100)
print("After discard():", my_set)