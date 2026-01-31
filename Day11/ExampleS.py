# Program to demonstrate set examples

# Example 1: Store unique colors
colors = {"Red", "Blue", "Green", "Red"}

print(colors)   # duplicate removed

# Example 2: Add item to set
colors.add("Yellow")
print(colors)

# Example 3: Remove item from set
colors.remove("Blue")
print(colors)

# Example 4: Loop through set
for color in colors:
    print(color)
