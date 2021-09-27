from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    # dollars must be greater than or equal to zero
    if dollars >= 0:
        # breaks out of loop
        break

# rounding it up
cents = int((dollars * 100) + 0.5)

total = 0
for coin in [25, 10, 5, 1]:
    # double dashe is integer division
    total += cents // coin
    cents %= coin

print(total)