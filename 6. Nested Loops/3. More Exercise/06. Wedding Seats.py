"""
The newlyweds want to make a list of who will sit in which place
 at the wedding ceremony. The seats are divided into different sectors.

Sectors are capital Latin letters starting with A.
Each sector has a certain number of rows.

The number of rows in the first sector (A) is read from the console,
and in each subsequent sector the rows are increased by 1.

Each row has a certain number of places - their numbering is
represented by small Latin letters. The number of places on the
odd rows is read from the console, and on the even rows there are 2 more places.
"""



last_sector = input()
rows_first_sector = int(input())
odd_row_seats = int(input())
seats = 0

for a in range(ord("A"), ord(last_sector) + 1):
    rows_first_sector += 1
    for b in range(1, rows_first_sector):
        if b % 2 == 0:
            for c in range(ord("a"), ord("a") + odd_row_seats + 2):
                print(f"{chr(a)}{b}{chr(c)}")
                seats += 1
        else:
            for c in range(ord("a"), ord("a") + odd_row_seats):
                print(f"{chr(a)}{b}{chr(c)}")
                seats += 1
print(seats)

