# continue is used to skip the current loop iteration and move to the next one.
# It does NOT stop the loop — it only skips one step.

for number in range(1, 6):
    if number == 3:
        continue
    print(number)
