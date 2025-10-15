#You can't use len or sum function use only for loops
h = 0
student_heights = input("Input a list of student heights: ").split()

total_height = 0

for height in student_heights:
    total_height += int(height)
#print(total_height)

number_of_students = 0
for student in student_heights: 
    number_of_students += 1
#print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)