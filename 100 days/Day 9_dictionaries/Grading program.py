student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermitone": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 75:
        student_grades[student] = "A"
    elif score >= 65:
         student_grades[student] = "B"
    elif score >= 55:
        student_grades[student] = "C"
    elif score >= 45:
        student_grades[student] = "D"
    else:
        student_grades[student] = "E"
        
print(student_grades)