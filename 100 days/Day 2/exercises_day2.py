#DATA TYPE EXERCISE CODE
# two_digit_number = input("Type a two digit numbers: ")

# print(type(two_digit_number))

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]


#BMI (Body Mass Index) Calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / int(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)