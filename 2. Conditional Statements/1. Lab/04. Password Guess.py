"""
To write a program that reads a password (text) entered by the user and checks whether the entered password matches
 the phrase "s3cr3t!P@ssw0rd".

  If there is a match, display "Welcome". In case of mismatch, display "Wrong password!".
"""

password = input()

if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")
