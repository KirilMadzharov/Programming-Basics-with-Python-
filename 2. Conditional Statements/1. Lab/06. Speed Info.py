"""
To write a program that reads speed (real number) entered by the user and prints speed information.

• For speed up to 10 (inclusive) print "slow"
• For speed above 10 and up to 50 (inclusive) print "average"
• For speed over 50 and up to 150 (inclusive) print "fast"
• For speed over 150 and up to 1000 (inclusive) print "ultra fast"
• For higher speed, print "extremely fast"
"""

speed = float(input())

if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
