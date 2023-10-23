"""
Your task is to write a program that calculates
the percentage of tickets for each type of ticket sold:
student, standard, and kid, for all screenings.

You should also calculate what percentage of the hall
is filled for each screening.
"""


line_input = input()

total_count_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0

while line_input != "Finish":
    movie = line_input
    capacity = int(input())

    command_line = input()
    current_movie_count = 0

    while command_line != "End":
        type_ticket = command_line
        total_count_tickets += 1
        current_movie_count += 1
        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kid_count += 1

        if current_movie_count == capacity:
            break
        command_line = input()

    percentage_current = current_movie_count / capacity * 100
    print(f"{movie} - {percentage_current:.2f}% full.")

    line_input = input()

print(f"Total tickets: {total_count_tickets}")
percent_student = student_count / total_count_tickets * 100

print(f"{percent_student:.2f}% student tickets.")
percent_standard = standard_count / total_count_tickets * 100

print(f"{percent_standard:.2f}% standard tickets.")
percent_kid = kid_count / total_count_tickets * 100

print(f"{percent_kid:.2f}% kids tickets.")
