"""
Grigor Dimitrov is a tennis player whose next goal is to
climb the world rankings in men's tennis.

During the year, Grisho participated in a certain number
of tournaments, and for each tournament he received points
 that depend on the position in which he finished in the tournament.

 There are three options for completing a tournament:

 W - if winner gets 2000 points
 F - if he is a finalist he gets 1200 points
 SF - if semi-finalist gets 720 points

Write a program that calculates how many points Grigor will have
after playing all the tournaments, knowing how many points he started
the season with.

Also calculate how many points he averaged from all the tournaments
played and what percentage of the tournaments he won.
"""



from math import floor

tournaments_participated = int(input())
starting_points = int(input())

rank_list_points = 0
wins = 0

for i in range(tournaments_participated):
    tournament_stage = input()

    if tournament_stage == "W":
        rank_list_points += 2000
        wins += 1
    elif tournament_stage == "F":
        rank_list_points += 1200
    elif tournament_stage == "SF":
        rank_list_points += 720

p_wins = (wins / tournaments_participated) * 100
average_points = rank_list_points / tournaments_participated
final_points = rank_list_points + starting_points

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{p_wins:.2f}%")

