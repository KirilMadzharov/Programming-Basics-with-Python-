"""
Sally Yashar's great-great-grandson received an inheritance - a safe with a password
- four digits. In it is locked the secret of the singing carts. He has a car repair
shop and needs advertising, so he decided to make such a cart. The problem is that the
 password is hidden in the following task:

"You will get a password if you know an integer, a check value is called that,
it rests in the interval from 4 to 144 inclusive, but finding it might be a pain. "
The password has the format: "abcd" and the check value must be equal to a*b + c*d ,
 but the following conditions must be met:

• when finding a and b: a < b
• when finding c and d: c > d
• a, b, c and d are numbers in the interval [1 - 9]

The cart has four wheels, so the password will be a fourth number that must be printed.
If NO such number is found, "No!" is printed.
"""



control_number = int(input())
password = ""
counter = 0
is_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and (a * b + c * d == control_number):
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        password = f"{a}{b}{c}{d}"
                        is_found = True
if is_found:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")

