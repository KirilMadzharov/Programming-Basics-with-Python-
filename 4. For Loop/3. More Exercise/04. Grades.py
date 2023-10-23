"""
Write a program to calculate exam grade statistics.

At the beginning, the program receives the number of students
who took the exam and for each student his grade.

At the end, the program should print the percentage of students
with a grade:

between 2.00 and 2.99, between 3.00 and 3.99, between 4.00 and 4.99, 5.00 or higher.

 Also the GPA on the exam.
"""



students = int(input())

less_3 = 0
around_3 = 0
around_4 = 0
more_5 = 0
grade_avg = 0

for i in range(students):
    grade = float(input())

    if grade < 3:
        less_3 += 1
        grade_avg += grade
    elif grade < 4:
        around_3 += 1
        grade_avg += grade
    elif grade < 5:
        around_4 += 1
        grade_avg += grade
    elif grade >= 5:
        more_5 += 1
        grade_avg += grade

top = (more_5 / students) * 100
betw_4 = (around_4 / students) * 100
betw_3 = (around_3 / students) * 100
fail = (less_3 / students) * 100
average = grade_avg / students

print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {betw_4:.2f}%")
print(f"Between 3.00 and 3.99: {betw_3:.2f}%")
print(f"Fail: {fail:.2f}%")
print(f"Average: {average:.2f}")
