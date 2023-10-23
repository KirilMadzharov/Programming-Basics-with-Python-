"""
To write a program that reads text (string) entered by the user
and calculates and prints the sum of the vowel values according to the table below:

letter a e i o u
value 1 2 3 4 5
"""

text = input()
result = 0

for i in range(0, len(text)):
    if text[i] == "a":
        result += 1
    if text[i] == "e":
        result += 2
    if text[i] == "i":
        result += 3
    if text[i] == "o":
        result += 4
    if text[i] == "u":
        result += 5

print(result)
