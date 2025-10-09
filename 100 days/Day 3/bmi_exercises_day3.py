
#BMI 2.O
height = (float(input("Enter your height in m: ")))
weight = (float(input("Enter your weight in kg: ")))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi < 25: 
    print(f"Your bmi is {bmi}, You have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
    
    
