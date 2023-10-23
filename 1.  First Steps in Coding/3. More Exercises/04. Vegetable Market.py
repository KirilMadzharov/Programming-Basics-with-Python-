"""
A gardener was selling the harvest from his garden at the vegetable market.
It sells vegetables for N BGN per kilogram and fruit for M BGN per kilogram.
Write a program to calculate the income from the harvest in euros (assuming that one euro is equal to BGN 1.94).
"""

vegetables_kg = float(input())
fruits_kg = float(input())
total_vegetables = int(input())
total_fruits = int(input())
# * 1.94
total = ((vegetables_kg * total_vegetables) + (fruits_kg * total_fruits)) / 1.94

print(f"{total:.2f}")
