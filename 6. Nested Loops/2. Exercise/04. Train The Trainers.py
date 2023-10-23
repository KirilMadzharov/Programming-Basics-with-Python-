"""
The "Train the trainers" course is coming to an end and the final evaluation is approaching.
Your task is to help the jury that will evaluate the presentations by writing a program to calculate
the average grade of each student's presentation, and finally the average grade of all of them.
From the console of the first row, the number of people in the jury is read n - an integer.
After that, the name of the presentation – text – is read on a separate line.
For each presentation on a new line, read n - the number of ratings - a real number.
After calculating the average score for a particular presentation, the console prints:
  "{presentation name} - {average grade}."
After receiving a "Finish" command, the console prints "Student's final assessment is
 {average of all presentations}." and the program ends.
All values must be formatted to the second decimal place.
"""


jury = int(input())

avg_presentation = 0
total_presentations = 0
avg_course = 0
course_finished = False

while not course_finished:
    presentation_name = input()

    if presentation_name == "Finish":
        course_finished = True
        break
    total_presentations += 1
    for n in range(1, jury + 1):
        grade = float(input())
        avg_presentation += grade

    avg_presentation = avg_presentation / jury
    print(f"{presentation_name} - {avg_presentation:.2f}.")
    avg_course += avg_presentation
    avg_presentation = 0

if course_finished:
    avg_course = avg_course / total_presentations
    print(f"Student's final assessment is {avg_course:.2f}.")

