"""
We have 1 BGN, 2 BGN banknotes and coins. and BGN 5 each.

Write a program that reads the number of notes and coins
entered by the user and the amount, and displays on the screen
all possible ways in which the amount can be paid with the available notes.
"""


one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
total_sum = int(input())

for a in range(one_lv + 1):
    for b in range(two_lv + 1):
        for c in range(five_lv + 1):
            if total_sum == a + b * 2 + c * 5:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total_sum} lv.")

