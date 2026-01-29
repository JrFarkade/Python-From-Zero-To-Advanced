# The return statement is used to send a value back from a function.
# After return, the function stops executing.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

result = celsius_to_fahrenheit(30)
print("Temperature in Fahrenheit:", result)

## return is used to send a value back from a function and stop its execution.
