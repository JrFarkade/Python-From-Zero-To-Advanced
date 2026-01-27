# Program to print number pattern and star pattern using while loop

# Pattern 1: Numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number = number + 1

print("Done")

# Pattern 2: Increasing star pattern
row = 1
while row <= 5:
    print("*" * row)
    row = row + 1

print("Done")

# Pattern 3: Decreasing star pattern
row = 5
while row >= 1:
    print("*" * row)
    row = row - 1

print("Done")
