#7.8 Deli
"""Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made"""

sandwich_orders = ['egg sandwich', 'potato sandwich', 'chicken sandwich']
finished_orders = []

for sandwich in sandwich_orders: #though for loop wok inside a list. Better use while loop.
    print("I made your " + sandwich + ".")
    finished_orders.append(sandwich)
    
print(finished_orders)