# Program to demonstrate break, continue, and pass

for number in range(1, 6):

    if number == 2:
        continue    # skips 2

    if number == 4:
        pass        # does nothing

    if number == 5:
        break       # stops loop

    print(number)

print("Done")
