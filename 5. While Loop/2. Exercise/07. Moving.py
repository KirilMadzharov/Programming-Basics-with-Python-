"""
On his eighteenth birthday, Jose decided he was going to move out and live in a boarding house.
He packed his luggage in boxes and found a suitable ad for an apartment for rent.
He starts carrying his luggage in parts because he can't do it all at once.
He has limited free space in his new home where he can arrange things so that the place is livable.
Write a program that calculates the free volume of Jose's apartment that remains after he has moved his luggage.
Each carton has exact dimensions: 1m x 1m x 1m.
"""



free_spase_width = int(input())
free_spase_length = int(input())
free_spase_high = int(input())
volume = free_spase_length * free_spase_width * free_spase_high

volume_is_full = False
finished = False

while not(volume_is_full or finished):
    boxes = input()

    if boxes == "Done":
        finished = True
        print(f"{volume} Cubic meters left.")
    else:
        volume -= int(boxes)
        if volume < 0:
            volume_is_full = True
            print(f"No more free space! You need {abs(volume)} Cubic meters more.")

