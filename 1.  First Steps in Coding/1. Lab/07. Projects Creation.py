"""
Write a program that calculates how many hours it will take an architect to prepare
the designs of several construction sites. It takes three hours to prepare one project.
"""

architect_name = input()
project_count = int(input())
hours = project_count * 3

print(f"The architect {architect_name} will need {hours} hours to complete {project_count} project/s.")
