# import module
from datetime import time

# 1,2 create Menu class and constructor
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  # 7 create string representation
  def __repr__(self):
    start_hour = f"{self.start_time % 12 or 12}{'am' if self.start_time < 12 else 'pm'}"
    end_hour = f"{self.end_time % 12 or 12}{'am' if self.end_time < 12 else 'pm'}"
    return f"{self.name} menu available from {start_hour} to {end_hour}."

  # 9 create method calculate_bill
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
    return total_bill

# 12,13 create class Franchise and constructor
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  # 15 create string representation
  def __repr__(self):
    return f"Franchise located at {self.address}"

  # 16 create available_menus
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# 19,20 create class Business and constructor
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# brunch_items contain name and price, served 11am to 4pm
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# 3 create brunch object
brunch = Menu("brunch", brunch_items, 11, 16)

# early_bird_items contain name and price, served 3pm to 6pm
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

# 4 create early_bird object
early_bird = Menu("early_bird", early_bird_items, 15, 18)

# dinner_items contain name and price, served 5pm to 11pm
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

# 5 create dinner object
dinner = Menu("dinner", dinner_items, 17, 23)

# kids_items contain name and price, served 11am to 9pm
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# 6 create kids object
kids = Menu("kids", kids_items, 11, 21)

# 8 test string representation
##print(brunch)
##print(early_bird)
##print(dinner)
##print(kids)

# 10 test Menu.calculate_bill for brunch
## expected 13.5
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

# 11 test Menu.calculate_bill for early_bird
## expected 21.5
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# 14 create 2 franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# 17,18 test available_menus()
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# 21 create first Business
my_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# 22 arepas_items contain name and price, served 10am to 8pm
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("arepas", arepas_items, 10, 18)

# 23 create arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# 24 create new Business
my_business_2 = Business("Take a' Arepa", [arepas_place])






