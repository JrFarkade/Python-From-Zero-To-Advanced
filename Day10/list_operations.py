# append()  → adds item at end of list
# insert()  → adds item at specific index  
# remove()  → removes given item  
# pop()     → removes last item  
# len()     → gives total items  
# in        → checks item exists  
# sort()    → arranges items in order  
# reverse() → reverses list order  

# Program to demonstrate different list operations

colors = ["Red", "Blue", "Green"]

# Add item at end
colors.append("Yellow")
print(colors)

# Insert item at specific position
colors.insert(1, "Black")
print(colors)

# Remove specific item
colors.remove("Green")
print(colors)

# Remove last item
colors.pop()
print(colors)

# Find length of list
print(len(colors))

# Check item exists
print("Blue" in colors)

# Sort list
colors.sort()
print(colors)

# Reverse list
colors.reverse()
print(colors)
