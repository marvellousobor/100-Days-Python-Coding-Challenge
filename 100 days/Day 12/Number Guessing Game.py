import random #or from random import randint

# Welcome statements and input
def play_game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")

    def invalid_inputs_try_again():
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        #use for loop to get numbers from 1 to 100
        numbers = []
        for number in range(1, 101):
            numbers.append(number)
            
        #function for both easy and hard level of the games
        def easy_level():
            computer_guess = random.choice(numbers)
            attempts = 10
            print(f"You have {attempts} attempts remaining to guess the number")
            
            while attempts > 0:
                user_guess = int(input("Make a guess: "))
                if user_guess == computer_guess:
                    print(f"You got it.\nThe answer was {user_guess}")
                    attempts = -1
                elif user_guess > computer_guess:
                    print("Too high.\nGuess again.")
                    attempts -= 1
                    print(f"You have {attempts} attempts remaining to guess the number.")
                elif user_guess < computer_guess:
                    print("Too low.\nGuess again.")
                    attempts -= 1
                    print(f"You have {attempts} attempts remaining to guess the number.")    
                
        def hard_level():
            computer_guess = random.choice(numbers)
            attempts = 5
            print(f"You have {attempts} attempts remaining to guess the number")
        
            while attempts > 0:
                user_guess = int(input("Make a guess: "))
                if user_guess == computer_guess:
                    print(f"You got it.\nThe answer was {user_guess}")
                    attempts = -1
                elif attempts == 0:
                    print("You didn't pick correctly.")
                elif user_guess > computer_guess:
                    print("Too high.\nGuess again.")
                    attempts -= 1
                    print(f"You have {attempts} attempts remaining to guess the number.")
                elif user_guess < computer_guess:
                    print("Too low.\nGuess again.")
                    attempts -= 1
                    print(f"You have {attempts} attempts remaining to guess the number.")
                elif attempts == 0:
                    print("You didn't pick correctly.")
                
        if difficulty_level == "easy":
            easy_level()
        elif difficulty_level == "hard":
            hard_level()
        else:
            print("Invalid input. Try again")
            invalid_inputs_try_again()
            
    invalid_inputs_try_again()

play_game()
    
play_again = input("Do you want to play again. Type 'yes' or 'no': ").lower()
if play_again == "yes":
    play_game()
else:
    print("Bye!")
#if statement calling function by user for both easy and hard
