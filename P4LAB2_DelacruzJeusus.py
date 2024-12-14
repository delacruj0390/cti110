# Delacruz, Jesus M.
# 2989390
# November 2, 2024
# This program creates a multiplication table of 12 for an integer, no negative numbers allowed 



while True:
    # Ask user to enter a integer
    number = int(input("Enter an integer: "))
    print("")

    # Check if the integer is zero or more
    if number >= 0:

        # Display multiplication table from 1- 12 using a for loop
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
    else:
        print("This program does not handle negative number")

    # Ask user if they want to run the program again
    run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
    print("")

    # Use a while loop to ensure valid input (only "yes" or "no")
    while run_again not in ("yes", "no"):
        run_again = input("Please type 'yes' or 'no': ").strip().lower()
        print("")

    # If the user types "no", break out of the main loop to end the program
    if run_again == "no":
        print("")
        print("Exiting Program...")
        break
