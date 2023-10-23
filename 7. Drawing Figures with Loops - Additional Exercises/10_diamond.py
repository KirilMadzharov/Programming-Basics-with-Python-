"""

--**--
-*-*-
*---*
-*-*-
--**--

"""

diamond = int(input())

half_diamond = diamond // 2

def print_line(outer_dashes, inner_dashes):
    print(f"{'-' * outer_dashes}*{'-' * inner_dashes}*{'-' * outer_dashes}")

for i in range(half_diamond):
    outer_dashes = half_diamond - i
    inner_dashes = diamond - 2 * outer_dashes - 2
    print_line(outer_dashes, inner_dashes)

if diamond % 2 != 0:
    print_line(0, diamond - 2)

for i in range(half_diamond - 1, -1, -1):
    outer_dashes = half_diamond - i
    inner_dashes = diamond - 2 * outer_dashes - 2
    print_line(outer_dashes, inner_dashes)
