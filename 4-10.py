prices = [90, 75, 46, 22, 80, 65, 8, 79]
max_price = 0
for price in prices:
    if price > max_price:
        max_price = price
min_price = prices[0]
for price in prices:
    if price < min_price:
        min_price = price
print(max_price, min_price)