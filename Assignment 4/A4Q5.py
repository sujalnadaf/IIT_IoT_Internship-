conversions = [
 lambda t: t * 1000, # tonns to kg
 lambda kg: kg * 1000, # kg to grams
 lambda g: g * 1000, # grams to mg
 lambda mg: mg * 0.00000220462 # mg to pounds
]
t = float(input("Enter weight in tonns: "))
kg = conversions[0](t)
g = conversions[1](kg)
mg = conversions[2](g)
lbs = conversions[3](mg)
print("Kg:", kg)
print("Grams:", g)
print("Milligrams:", mg)
print("Pounds:", lbs)
