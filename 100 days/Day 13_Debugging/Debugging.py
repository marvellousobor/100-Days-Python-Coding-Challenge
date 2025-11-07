###############DEBUGGING###################

def my_function():
    for i in range(1, 21):
        if i = 20: #You can only use one equal to when assigning variables use double equals for conditionals
            print("You got it")
my_function()

from random import randint
dice_imgs = ["*", "*", "*", "*", "*", "*"]
dice_num = randint[1, 6] #In the random here the number ends at 5 not 6 that is [1, 2, 3, 4, 5]
print(dice_imgs[dice_num])

#LEAP YEAR DEBUGGING
year = input("Which year do you want to check? ") #Inputs are saved as strings not integers
print(f"The year {year}: ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else: 
        print("Leap year.")
else:
    print("Not leap year.")
 
# FIZZBUZZ DEBUGGING   
for number in range(1,101):
    if number % 3 == 0 or number % 5 == 0: # 'and' not 'or'. In 'or' just one has to be true but for 'and' the two statement has to be true
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")