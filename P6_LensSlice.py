# Len's Slice

# 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# 2
costs = [2, 6, 1, 3, 2, 7, 2]

# 3
num_two_dollar_slices = costs.count(2)
# print(num_two_dollar_slices)

# 4
num_pizzas = len(toppings)

# 5
print(f"We sell {num_pizzas} different kind of pizza!")

# 6
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# 7
print(pizza_and_prices)

# 8
pizza_and_prices.sort()
print(pizza_and_prices)

# 9
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# 10
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# 11
pizza_and_prices.pop()
print(pizza_and_prices)

# 12
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# 13
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
