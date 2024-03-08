#Exercise 1

def add(n1,n2):
    return n1+n2

n1 = int(input("Please Enter a Number : "))
n2 = int(input("Please Enter a Number : "))

print(add(n1,n2))

#Exercise 2

def unstring(user_un_string):
    modified_string = "un"+user_un_string
    return modified_string

user_un_string = input("Please Enter a String to be UN'd : ")

print(unstring(user_un_string))

#Exercise 3

def palindrome(user_pal_string):
    user_string_reversed = user_pal_string [::-1]
    if user_string_reversed == user_pal_string:
        return True 

user_pal_string = input("is This a Palindrome? : ")

user_pal_string = user_pal_string.lower()

palindrome(user_pal_string)

if palindrome(user_pal_string) == True:
    print("das a palindrome")
elif user_pal_string == "palindrome":
    print("har har \nthats not a palindrome")
else:
    print("das not a palindrome")

#Exercise 4
    
def even_odd_count(number_list):
    print("goob")
