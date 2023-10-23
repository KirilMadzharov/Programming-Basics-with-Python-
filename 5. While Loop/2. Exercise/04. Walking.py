"""
Gabby wants to start a healthy lifestyle and has set a goal of walking 10,000 steps every day.
Some days, however, she is very tired from work and will want to go home before she achieves her goal.

Write a program that reads from the console how many steps she takes each time she goes out during the day,
and when she reaches her goal it says

"Goal reached! Good job!" and how many more steps did "{difference between steps} steps over the goal!"

If she wants to go home before then, she will enter the command "Going home" and enter the steps she took
on her way home. After which, if she failed to reach her goal, the console should read:

"{difference between steps} more steps to reach goal."
"""



input_line = input()
steps_count = 0

while input_line != "Going home":
    steps = int(input_line)
    steps_count += steps
    if steps_count >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    steps_count += steps_home

diff = abs(10000 - steps_count)

if steps_count >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

