number=0
option1 = True
while option1:
    try:
        num1 = int(input("Please enter a number : "))
        option2 = True
        break
    except:
        print("That is not a valid option")
while option2:
    try:
        num2 = int(input("Please enter a second number : "))
        option3 = True
        num3 = num1 + num2
        break
    except:
        print("That is not a valid option")    
while option3:
    while option3:
        cont = input("do you want to add another number? (y/n) : ")
        cont = str.lower(cont)
        if cont == "y":
            break
        if cont == "n":
            break
        else:
            print("invalid selection, please select y or n")               
    if "y" == cont:
        try:
            num1 = int(input("Please enter a number : "))
            option2 = True
            num3 = num1+num3
        except:
            print("That is not a valid option")
    if cont == "n":
        break
print("the total is :",num3)