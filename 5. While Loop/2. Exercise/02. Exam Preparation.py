"""
Write a program in which Marin solves exam problems until she receives an
 "Enough" message from her lecturer. For each solved task he gets a grade.

  The program should stop reading data on the command "Enough" or if Marin
  receives the specified number of unsatisfactory marks.

  Any score less than or equal to 4 is unsatisfactory.
"""



bad_grades = int(input())
problem_title = input()
grade_total = 0
solved_problems = 0
last_problem = ""
bad_grade_count = 0

while problem_title != "Enough":
    grade = int(input())

    grade_total += grade
    solved_problems += 1
    last_problem = problem_title

    if grade <= 4:
        bad_grade_count += 1
        if bad_grade_count >= bad_grades:
            print(f"You need a break, {bad_grade_count} poor grades.")
            break

    problem_title = input()

else:
    average_score = grade_total / solved_problems

    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")

