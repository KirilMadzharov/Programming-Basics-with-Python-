"""
Write a program that reads text from the console (string)
 and prints it until it receives the "Stop" command.
"""


text = input()

while text != 'Stop':
    print(text)
    text = input()
