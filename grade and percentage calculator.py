english_marks = float(input("Enter marks obtained in English: "))
math_marks = float(input("Enter marks obtained in Math: "))
science_marks = float(input("Enter marks obtained in Science: "))
history_marks = float(input("Enter marks obtained in History: "))
geography_marks = float(input("Enter marks obtained in Geography: "))

total_marks = english_marks + math_marks + science_marks + history_marks + geography_marks
average_marks = total_marks / 5

if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Percentage: ", average_marks)
print("Grade: ", grade)
