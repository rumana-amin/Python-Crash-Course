#7.2 Restaurant Seating
"""Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready."""

num = input("How many people are in your group? ")
num = int(num)

if num > 8:
    print("\nPlease wait a bit more.")
else:
    print("\nYuor table is ready.")