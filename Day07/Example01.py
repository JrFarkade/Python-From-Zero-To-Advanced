# Loop Examples

# 1) Loop through string  
# Prints characters one by one. `break` stops the loop.

# 2) range(start, end, step)  
# Prints numbers from 5 to 9 with gap of 2.

# 3) Loop through list  
# Adds all prices and prints total.


# Program to demonstrate for loop with string, range, and list

# Loop through a string
for letter in "Python":
    print(letter)
    break   # stops loop after first character

# Loop using range with step
for number in range(5, 10, 2):
    print(number)

# Loop through list and calculate total
prices = [10, 20, 30]
total = 0

for price in prices:
    total = total + price

print("Total:", total)
