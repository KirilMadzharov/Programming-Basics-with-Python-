"""
Write a program that calculates the grade point average of a student over his entire course.

On the first line, you will get the student's name, and on each subsequent line,
their annual grades. The student advances to the next grade if his annual grade is
greater than or equal to 4.00. If the student is interrupted more than once,
the student is expelled and the program ends, printing the name of the student and
 the class in which he was expelled.

  On successful completion of 12th grade to print:

"{student name} graduated. Average grade: {the average grade of the entire study}"

In case the student is excluded from school, print:
"{student name} has been excluded at {grade in which he was excluded} grade"

The value must be formatted to the second decimal place.
"""



student_name = input()

current_class = 1
total_grade = 0
fail = 0

is_excluded = False

while current_class <= 12:
    current_grade = float(input())

    if current_grade < 4:
        fail += 1
        if fail > 1:
            is_excluded = True
            break

    else:
        current_class += 1
        total_grade += current_grade

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
