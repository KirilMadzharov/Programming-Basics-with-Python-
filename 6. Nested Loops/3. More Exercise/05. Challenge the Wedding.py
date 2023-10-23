"""
Provoked by their wedding, Michaela and Ivan decide to provide a new service to customers of
their restaurant, namely a dating dinner - "Challenge the Wedding".

Write a program that prints all possible restaurant customer encounters.

Upon check-in, each man and each woman receives coupons with consecutive
numbers starting from 1. If all tables are occupied, the program must end.

Each table has two seats.
"""


male_clients = int(input())
female_clients = int(input())
max_tables = int(input())
counter = 0

for i in range(1, male_clients + 1):
    for j in range(1, female_clients + 1):
        if counter >= max_tables:
            break
        print(f"({i} <-> {j})", end=" ")
        counter += 1

