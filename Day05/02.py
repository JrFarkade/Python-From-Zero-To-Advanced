# String Indexing
# Each character in a string has a position (index).
# Index starts from 0.

# Example:
word = "Python"
print(word[0])   # P
print(word[3])   # h


# String Slicing
# Used to get part of a string.
# Syntax: string[start:end]

# Example:
word = "Python"
print(word[0:3])   # Pyt
print(word[2:5])   # tho


# Common String Methods
text = "hello world"

print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.capitalize())# Hello world
print(text.replace("world","python"))
print(len(text))         # length of string
