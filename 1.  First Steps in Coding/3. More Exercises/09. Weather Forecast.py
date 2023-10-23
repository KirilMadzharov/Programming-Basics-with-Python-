"""
Write a program that knows whether it is hot or cold outside.
One line is read from the console - a text that tells what the time is.
Typing "sunny" should print "It's warm outside!".
In all other cases "It's cold outside!" should be printed.
"""

weather = str(input())

if weather == "sunny":
    print("It's warm outside!")
else:
    print("It's cold outside!")
