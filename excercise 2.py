year = int (input("Enter the current year"))
age = int (input ("What age will you be at the end of this year?")) # Note the int() cast on the input
print("You were born in", (year-age))

# a) will give error because you cant add a string and a integer
# b) will not give an error because of the str() infront of the 18, although it will just add the 18 to the end of the 2000
