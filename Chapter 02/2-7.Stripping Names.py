#Exercise 2-7.Stripping Names
#Storing a person’s name including some whitespace characters at the beginning and end of the name.
#printing the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = "\t\n  Rumana Amin \n\t"
print("Name with whitespace:", name)

print("Name stripped with lstrip():", name.lstrip())
print("Name stripped with rstrip():", name.rstrip())
print("Name stripped with strip():", name.strip())