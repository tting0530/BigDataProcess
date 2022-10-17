#!/usr/bin/python3

price = [10000, 8000, 7500, 12000, 25000]
sale = []

for i in range(len(price)):
	sale.append(price[i] * 0.8)

print(sale)
