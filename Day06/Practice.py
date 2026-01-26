# Program to convert weight between kilograms and pounds

weight = float(input("Enter your weight: "))
unit = input("Enter K for kilograms or P for pounds: ")

if unit == "K":
    pounds = weight * 2.2046
    print("Weight in pounds:", pounds)

elif unit == "P":
    kilograms = weight * 0.4535
    print("Weight in kilograms:", kilograms)

else:
    print("Invalid input")
