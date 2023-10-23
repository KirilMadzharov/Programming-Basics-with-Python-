"""
Jessie has decided to raise money for a field trip and she wants you to help
her find out if she will be able to raise the necessary amount.

She saves or spends some of her money every day. If she wants to spend more
 than her available money, she will spend as much as she has and she will have BGN 0 left.
"""



needed_money = float(input())
available_money = float(input())
days = 0
days_spent = 0

while available_money < needed_money:
    action = input()
    action_money = float(input())
    days += 1
    if action == "save":
        available_money += action_money
        days_spent = 0
    else:
        available_money -= action_money
        if available_money < 0:
            available_money = 0
        days_spent += 1
        if days_spent == 5:
            print("You can't save the money.")
            print(days)
            break
else:
    print(f"You saved the money for {days} days.")

