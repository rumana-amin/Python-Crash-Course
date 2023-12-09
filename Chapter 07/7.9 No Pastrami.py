#7.9 No Pastrami
"""Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

sandwich_orders = ['pastrami','veggie', 'grilled cheese', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        if sandwich == 'pastrami':
            sandwich_orders.remove("pastrami")
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")