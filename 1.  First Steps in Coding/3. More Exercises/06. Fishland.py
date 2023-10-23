"""
Georgi will have guests in the evening and decides to treat them with bonito,
 saffron and mussels. So he goes to the fish market to buy a few kilos.
 The prices in BGN of mackerel and sprat are entered from the console.
 Also, the amount of bonito, saffron and mussels in kilograms.

 How much money will he need to pay his bill if stock market prices are:
• Bonito – 60% more expensive than mackerel
• Safrid – 80% more expensive than sprat
• Mussels – BGN 7.50 per kilogram
"""

mackerel_price = float(input())
sprat_price = float(input())
bonito_weight = float(input())
horse_mackerel_weight = float(input())
mussels_count = int(input())

bonito_price = mackerel_price * 1.6
horse_mackerel_price = sprat_price * 1.8
final_price = bonito_price * bonito_weight + horse_mackerel_price * horse_mackerel_weight + mussels_count * 7.5

print(f"{final_price:.2f}")
