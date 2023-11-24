# 4.11 My Pizzas, Your Pizzas
pizzas = ['chesse pizza', 'mushroom pizza', 'chicken pizza']
friend_pizzas = pizzas[:]

pizzas.append("veg pizza")
friend_pizzas.append("beef pizza")

print("My favorite pizzas are:")
for item in pizzas:
    print(item)

print("\nMy friend's favorite pizzas are:")
for item in friend_pizzas:
    print(item)
    
print("Who doesn't like pizza? Well, everyone loves it.")