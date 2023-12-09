#7.3 Multiples of Ten
"""Ask the user for a number, and then report whether the
number is a multiple of 10 or not."""

num = input("Please enter a number: ")
num = int(num)

if num % 3 == 0:
    print("\nIt's a multiple of three.")
else:
    print("\nIt's not a multiple of three.")