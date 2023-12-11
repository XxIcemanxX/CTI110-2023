#Brief description: simple math quizzes
#Date-11/25/2023
#CTI - 110 P5HW1
#Kenneth Somers

import random

def main():
    print("Welcome to Math Quiz")

    add_random_numbers()
    
    

        
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
            add_random_numbers()


if __name__ == "__main__":
    main()
