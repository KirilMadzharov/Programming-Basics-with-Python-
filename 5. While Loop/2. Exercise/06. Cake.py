"""
You're invited to a 30th birthday party where the birthday boy treats himself to a huge cake.
However, he does not know how many pieces the guests can take from it.

Your task is to write a program that counts the number of pieces the guests have taken before it runs out.
You will get the dimensions of the cake (width and length - integers and then on each line,
until you receive the command "STOP" or until the cake runs out, the number of pieces that the
guests take from it.

Each piece of cake is 1x1 cm in size.

Print one of the following lines to the console:

• "{number of pieces} pieces are left." - if you reach STOP and have not run out of cake pieces;
• "No more cake left! You need {number of missing pieces} pieces more."
"""



cake_length = int(input())
cake_width = int(input())
cake = cake_length * cake_width

cake_finished = False

while cake_finished != True:
    command = input()

    if command == "STOP":
        print(f"{cake} pieces are left.")
        break
    else:
        cake -= int(command)
        if cake <= 0:
            cake_finished = True
            break

if cake_finished:
    print(f"No more cake left! You need {abs(cake)} pieces more.")

