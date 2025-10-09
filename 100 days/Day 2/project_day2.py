# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill: $"))
# tip= float(input("What ercentage tip would you like to give 10, 12, 15: $"))
# people = float(input("How many people to split the bill? "))

# percentage_tip = tip / 100
# new_bill = (total_bill * percentage_tip) + total_bill
# payment = (new_bill / people)

# print("Each person should pay: $" + "%.2f" % round(payment, 2))


# TREASURE ISLAND GAME
print("Welcome to Treasure Island. Your mission is to find the treasure")
choice1 = input("Reached a road with two ways, which way will you go Type 'left' to go left or 'right' to go right: ").lower()

if choice1 == "left":
    choice2 = input("Gotten to a river. Type 'swim' to swim across or 'wait' to wait for a boat): ").lower()
    if choice2 == "wait":
        print("Found a boat crossed to the other side. A house with three doors appears...")
        choice3 = input("...Which door would you choose 'Red' 'Yellow' or 'Blue': ").lower()
        if choice3 == "yellow":
            print("You found the treasure: You Win!")
        else:
            print("Entered a room full of danger, Game Over")
    else:
        print("Drowning, Game over")   
else: 
    print("Caught by island raiders. Game over!")