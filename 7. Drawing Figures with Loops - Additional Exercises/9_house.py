"""

--*--
-***-
*****
|***|
|***|

"""


from math import ceil

number = int(input())

half_number = ceil(number / 2)
dashes = (half_number - 1) * "-"

for n in range(half_number):
    if n == 0:
        if number % 2 == 0:
            print(f"{dashes}{2 * '*'}{dashes}")
        else:
            print(f"{dashes}*{dashes}")
    else:
        num_stars = 2 * n + 1
        dashes_2 = ceil((number - num_stars) / 2) * "-"
        print(f"{dashes_2}{num_stars * '*'}{dashes_2}")

for n in range(1, number - half_number + 1):
    print(f"|{(number - 2) * '*'}|")
