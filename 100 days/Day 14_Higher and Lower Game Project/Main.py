from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Take the account data and return printable Format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
        
# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make the game repeatable
while game_should_continue:
    #Generate a random account from the game data.
    
    #Make account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account = account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account = account_b)}.")

    #Ask user for a guess
    guess = input("Who has more input? Type 'A' or 'B': ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear()
    print(logo) #print logo just after you cleared the screen
    
    ## Get follwer count of each account
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}")
    ### Use if statement to check if user is correct

    #Give user feedback on their guess