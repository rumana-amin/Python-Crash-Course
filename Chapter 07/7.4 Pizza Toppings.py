#7.4 Pizza Toppings
"""Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

prompt = "\nEnter your requested topping for pizza: "
prompt += ("\nEnter 'quit' to close.")

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("Adding " + topping + "to the pizza.")
    else:
        break