# LOVE CALCULATOR
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

combined_names = lower_case_name1 + lower_case_name2
print(combined_names)

# It would have been better to do this here:
#t = combined_names.count("t")
#... and so on for better understanding
calculate_true = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
calculate_love = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

love_score = str(calculate_true) + str(calculate_love) #or love_score = int(str(calculate_true) + str(calculate_love))
love_score = int(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 90:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")