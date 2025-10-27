import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(f"The Solution to the word is {chosen_word}.")

from hangman_art import logo, stages
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}. That's not in the word. Hangman Loses a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])