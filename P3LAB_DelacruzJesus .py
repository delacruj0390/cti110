# Jesus Delacruz
# 17 Oct 2024
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal





# Total up the money from the user 
amount = float(input("Enter the amount of money as a float: $"))

# Step 3 : Convert to an integer number of cents 
cents = int(round(amount * 100))

# Step 4 Check for zero amount
if cents == 0:
    print("No change")
else:
    # Add up the total Dollars (1Dollar)
    dollars = cents // 100
    cents %= 100

    # Add up the total Quaters (25Cents)
    quarters = cents // 25
    cents %= 25

    # Add up the total Dimes (10Cents)
    dimes = cents // 10
    cents %= 10

    # Add up the total Nickels (5Cents)
    nickels = cents // 5
    cents %= 5

    # Add up the total Pennies (1Cent)
    pennies = cents

    # Output the results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
