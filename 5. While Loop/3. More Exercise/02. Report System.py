"""
At a charity event, payments for purchased products always alternate: cash payment and card payment.

The following payment rules are established:
• If the product exceeds BGN 100, it cannot be paid for in cash
• If the product is priced below BGN 10, it cannot be paid for by credit card
The program ends either after we receive an "End" command or after the funds are collected.
"""



expected_sum = int(input())

payment_type = 0
cash_payment = 0
card_payment = 0
cash_count = 0
card_count = 0

command = input()

while command != "End":
    payment_type += 1
    product_price = int(command)

    if product_price > 100 and payment_type == 1:
        print("Error in transaction!")
    elif product_price <= 10 and payment_type == 2:
        print("Error in transaction!")

    if product_price <= 100 and payment_type == 1:
        cash_payment += product_price
        cash_count += 1
        print("Product sold!")

    elif product_price > 10 and payment_type == 2:
        card_payment += product_price
        card_count += 1
        print("Product sold!")

    total_payment = card_payment + cash_payment

    if total_payment >= expected_sum:
        print(f"Average CS: {cash_payment / cash_count:.2f}")
        print(f"Average CC: {card_payment / card_count:.2f}")
        break

    if payment_type == 2:
        payment_type = 0

    command = input()

else:
    print("Failed to collect required money for charity.")
