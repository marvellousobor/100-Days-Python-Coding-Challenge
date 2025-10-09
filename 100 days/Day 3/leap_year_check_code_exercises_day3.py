#LEAP YEAR CODING EXERCISE
year = int(input("Which year do you want to check? "))

print(f"The year {year}: ")

#Error from Me
# div4 = year % 4
# div100 = year % 100
# div400 = year % 400

# if div4 == 0 or div100 == 0:
#     print(f"The year {year}, is a leap year")
# elif div400 == 0:
#     print(f"The year {year}, is a leap year")
# else:
#     print(f"The year {year}, is not a leap year")

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
 