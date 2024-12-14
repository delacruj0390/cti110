# Jesus Delacruz
# 20 Nov 2024
# P5HW
# Program will create 2 math games for the user. 1 will be a addition of numbers and
# second will be subraction of numbers. 

import random


def generate_numbers():
    # Generates two random numbers
    num1 = random.randint(1, 99)  # Smaller numbers for clearer display
    num2 = random.randint(1, 99)
    return num1, num2


def get_user_guess(prompt="Enter your answer: "):
    # User will enter their answer
    return int(input(prompt))


def addition_quiz():
    # Will conduct an ddition quiz
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    print(f"  {num1}")
    print(f"+ {num2}")
    guesses = 0

    while True:
        user_guess = get_user_guess()
        guesses += 1
        if user_guess == correct_answer:
            print("Congratulations! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
            break
        elif user_guess < correct_answer:
            print("Sorry, guess is too low.")
            print("Try again: ", end="")
        else:
            print("Sorry, guess is too high.")
            print("Try again: ", end="")


def subtraction_quiz():
    # Conducts a subtraction quiz.
    num1, num2 = generate_numbers()
    # Ensure num1 >= num2 to avoid negative results
    if num1 < num2:
        num1, num2 = num2, num1
    correct_answer = num1 - num2
    print(f"  {num1}")
    print(f"- {num2}")
    guesses = 0

    while True:
        user_guess = get_user_guess()
        guesses += 1
        if user_guess == correct_answer:
            print("Congratulations! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
            break
        elif user_guess < correct_answer:
            print("Sorry, guess is too low.")
            print("Try again: ", end="")
        else:
            print("Sorry, guess is too high.")
            print("Try again: ", end="")


def main_menu():
    # Displays the main menu.
    while True:
        print("\nWelcome to Math Quiz")
        print("")
        print("")
        print("MAIN MENU")
        print("-------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("")
        choice = input("Please only choose one of the menu options: ")
        print("")
        print("")

        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing.")
            print("Bye")
            break
        else:
            print("Invalid selection. Choose a valid option.")


# Start the program
if __name__ == "__main__":
    main_menu()
