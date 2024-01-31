def Binary_To_Decimal():
    binary1 = input("please enter a binary number (e.g. 10101)   :")
    
    decimal = int(binary1, 2)
    
    print(binary1,"equals",decimal)


def Decimal_To_Binary():
    decimal = int(input("please enter a decimal number (e.g. 21)     :"))
    
    binary1 = bin(decimal)[2:]
    
    print(decimal,"equals",binary1)


def Binary_Addition():
    binary1 = input("please enter a binary number (e.g. 10101)   :")
    binary2 = input("please enter a binary number (e.g. 10101)   :")
    
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    
    decimal3 = decimal1 + decimal2
    
    bin_decimal3 = bin(decimal3)[2:]
    
    print(binary1,"plus",binary2,"equals",bin_decimal3)
    print(bin_decimal3,"equals",decimal3)


def Hexadecimal_To_Binary():
    hexadecimal = input("Please enter a hexadecimal (e.g. a1)        :")
    
    scale = 16
    
    binary1 = bin(int(hexadecimal, scale)).zfill(8)[2:]
    
    print (hexadecimal,"equals",binary1)
    
    
def Binary_To_Hexadecimal():
    binary1 = input("please enter a binary number (e.g. 10101)   :")
    
    hexadecimal = hex(int(binary1))#[2:]
    
    print (binary1,"equals",hexadecimal)
    
    
def Hexadecimal_To_Decimal():
    hexadecimal = input("please enter a hexadecimal  (e.g. c469)     :")
    
    decimal = int(hexadecimal, 16)
    
    print(hexadecimal,"equals",decimal)
    
    
def Decimal_To_Hexadecimal():
    decimal = input("please enter a decimal number (e.g. 50281)   :")
    
    hexadecimal = hex(int(decimal))[2:]
    
    print (decimal,"equals",hexadecimal)
    
    
while True:
    while True:
        try:
            choice = int(input("Bin to Dec = 1, Dec to Bin = 2, Binary Addition = 3, \nHex to Bin = 4, Bin to Hex = 5, Hex to Dec = 6, \nDec to Hex = 7, Exit = 8 \nChoice -> "))
            break
        except:
            print("invalid selection.")
    if choice == 1:
        Binary_To_Decimal()
        
    elif choice == 2:
        Decimal_To_Binary()
        
    elif choice == 3:
        Binary_Addition()
        
    elif choice == 4:
        Hexadecimal_To_Binary()
        
    elif choice == 5:
        Binary_To_Hexadecimal()
        
    elif choice == 6:
        Hexadecimal_To_Decimal()
        
    elif choice == 7:
        Decimal_To_Hexadecimal()
        
    elif choice == 8:
        break
    
    else:
        print("invalid selection.")
        
#100 lines yay
