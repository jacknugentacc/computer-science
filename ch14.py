number=int(input("enter a number above 10 and under 20 : "))
if number in list(range(10,21)):
    print ("thank you")
while number < 10:
    print ("incorrect answer")
    number=int(input("enter a number UNDER 20 : "))
    if number in list(range(10,21)):
        print ("thank you")
while number > 20:
    print ("incorrect answer")
    number=int(input("enter a number UNDER 20 : "))
    if number in list(range(10,21)):
        print ("thank you")