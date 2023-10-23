"""
Write a program that initially reads a user profile name and password.
It then reads a login password.

• when entering a wrong password: prompt the user to enter a new password.
• when entering a correct password: we print "Welcome {username}!".
"""


user = input()
password = input()
data = input()

while data != password:
    data = input()

print(f"Welcome {user}!")
