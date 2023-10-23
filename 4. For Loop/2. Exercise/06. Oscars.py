"""
You are invited by the academy to write software to calculate the points for an actor/actress.
The academy will give you initial points for the actor.
Each rater will then give their rating.

he points the actor receives are formed by: the length of the evaluator's
name multiplied by the points he gives divided by two.

If the score at any point exceeds 1250.5 the program should abort and
print that the given actor has received a nomination.

"""



actors_name = input()
academy_points = float(input())
n_graders = int(input())

final_points = academy_points

for i in range(n_graders):
    grader_name = input()
    grader_points = float(input())
    final_points += (len(grader_name) * grader_points) / 2
    if final_points > 1250.5:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {final_points:.1f}!")
        break

diff = 1250.5 - final_points

if final_points <= 1250.5:
    print(f"Sorry, {actors_name} you need {diff:.1f} more!")

