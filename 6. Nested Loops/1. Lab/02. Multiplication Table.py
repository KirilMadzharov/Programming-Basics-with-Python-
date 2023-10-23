"""
Print to the console the multiplication table for the numbers 1 to 10 in the format:

"{first multiplier} * {second multiplier} = {result}".
"""

for i in range(1, 10 + 1):
    for j in range(1, 10 + 1):
        print(f"{i} * {j} = {i * j}")
