# Getting Ready for Physics Class

# variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# 1 define function convert fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5 / 9)
  return c_temp

# 2 test function
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

# 3 define function convert celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return f_temp

# 4 test function
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# 5 define force function
def get_force(mass, acceleration):
  return mass * acceleration

# 6, 7 test function
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print(f"The GE train supplies {train_force} Newtons of force")

# 8 define EMC2 function
def get_energy(mass, c=3*10**8):
  energy = mass * (c ** 2)
  return energy

# 9, 10 test function
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# 11 define work function
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

# 12, 13 test function
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

