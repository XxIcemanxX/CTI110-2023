#Brief description: simple math quizzes
#Date-11/25/2023
#CTI - 110 P5HW2
#Kenneth Somers

import random

def main():
    print("Welcome to Math Quiz")
    
    while True:
        display_menu()  
        choice = input("Please choose one of the menu options: ")

        
        if choice == "1":
            add_random_numbers()
        elif choice == "2":
            subtract_random_numbers()
        elif choice == "3":
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("Invalid choice. Please select from the given options.")


def display_menu():
    print("MAIN MENU")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")


def add_random_numbers():
    num1 = random.randint(1, 100)  
    num2 = random.randint(1, 100)  
    correct_answer = num1 + num2   
    guess_count = 0                

    print(f"{num1: >3}\n+{num2: >2}\nEnter answer.")

    
    
    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\ntry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\ntry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break


def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    guess_count = 0

    print(f"{num1: >3}\n-{num2: >2}\nEnter answer.")

    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\ntry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\ntry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break


if __name__ == "__main__":
    main()

