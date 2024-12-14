# Jesus Delacruz
# 12NOV2024
# P5LAB_DelacruzJesus
# This program will simulate a customer using a self-checkout machine



import random

def disperse_change(cents):
    """Display & Calculate the change in $1, 25C, 10C, 5C, and 1C."""

    # Calculate Amounts
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5

    # Print results
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


def main():
    """Main function to display & calculate the change returned."""
    # Populate random amount 
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    # Allow user input
    amount_paid = float(input("How much cash will you put in the self checkout? $"))

    # Determine change in cents
    change = round((amount_paid - amount_owed) * 100)
    print(f"\nChange is: ${change / 100:.2f}")

    # Call function to display change breakdown
    disperse_change(change)


# Start the program
if __name__ == "__main__":
    main()
