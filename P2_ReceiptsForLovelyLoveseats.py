# Lovely Loveseat description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Lovely Loveseat price
lovely_loveseat_price = 254.00

# Stylish Settee description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Stylish Settee price
stylish_settee_price = 180.50

# Luxurious Lamp description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Luxurious Lamp price
luxurious_lamp_price = 52.15

# sales tax
sales_tax = 0.088

# customer one total bill
customer_one_total = 0

# customer one item
customer_one_itemization = ""

# customer one buy Lovely Loveseat, Luxurious Lamp
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "\n"

# calculate customer one sale tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# customer one summary
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)
