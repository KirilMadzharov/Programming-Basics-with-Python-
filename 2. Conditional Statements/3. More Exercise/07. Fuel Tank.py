"""
Write a program that knows whether a vehicle's tank needs refueling or not.
Two lines are read from the console - text and a real number, the first line reads
the type of fuel - text with options: "Diesel", "Gasoline" or "Gas",
and the second line shows the liters of fuel in the tank.

If the liters of fuel are more than or equal to 25, the console should
 print "You have enough {type of fuel}.", if they are less than 25, it should print
 "Fill your tank with {type of fuel}!" .

 In case a fuel other than the one specified is entered, "Invalid fuel!" will be printed.
"""

fuel_type = str(input())
litres = float(input())

if fuel_type in ("Diesel", "Gasoline", "Gas"):
    if litres >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
