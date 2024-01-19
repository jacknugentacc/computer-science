def Binary_To_Decimal():
    binary = input("please enter a binary number (e.g. 10101)   :")
    decimal = int(binary, 2)
    print(binary,"equals",decimal)

def Decimal_To_Binary():
    decimal = int(input("please enter a decimal number (e.g. 21)     :"))
    bin_decimal = bin(decimal)[2:]
    print(decimal,"equals",bin_decimal)

def Binary_Addition():
    binary1 = input("please enter a binary number (e.g. 10101)   :")
    binary2 = input("please enter a binary number (e.g. 10101)   :")
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    decimal3 = decimal1 + decimal2
    bin_decimal3 = bin(decimal3)[2:]
    print(binary1,"plus",binary2,"equals",bin_decimal3)
    print(bin_decimal3,"equals",decimal3)
    
