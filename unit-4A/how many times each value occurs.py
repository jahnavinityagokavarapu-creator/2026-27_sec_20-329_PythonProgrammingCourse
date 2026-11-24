# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Create an empty dictionary
word_count = {}

# Split sentence into words
words = sentence.split()

# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display word frequency
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)