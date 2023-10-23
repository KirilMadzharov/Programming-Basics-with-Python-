"""
Congratulations, because of your deep knowledge in the field of programming,
the Ministry of Interior decided to hire you to create their new system
for generating special car numbers. Each special vehicle number consists of four numbers.

The conditions that distinguish special from ordinary numbers are the following:

• If the number starts with an even number, it must end with an odd number,
and vice versa – if it starts with an odd number, it must end with an even number

• The first digit of the number is greater than the last
• The sum of the second and third digits must be an even number

The input consists of two numbers - the start and end of an interval,
between which each number of the number must be generated.
"""



start = int(input())
end = int(input())

for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            if (b + c) % 2 != 0:
                continue
            for d in range(start, end + 1):
                if a < d:
                    continue
                if a % 2 == 0 and d % 2 == 0:
                    continue
                if a % 2 != 0 and d % 2 != 0:
                    continue
                print(f"{a}{b}{c}{d}", end=" ")
