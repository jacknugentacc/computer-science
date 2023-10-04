gb = 10
while gb >= 1:
    print(" there are", gb, "green bottles hanging on the wall, \n", gb, "green bottles hanging on the wall \n","and if one green bottle should accidentaly fall")
    option1 = True
    while option1:
        try:
            ngb = int(input("how many green bottles will be hanging on the wall? : "))
            break
        except:
            print("invalid selection.")
    if ngb == gb-1:
        print ("CORRECT")
        gb = ngb
    else:
        print ("INCORRECT")
print("no more bottles hanging on the wall")