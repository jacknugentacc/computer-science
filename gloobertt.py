#caesar cipher
deco = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
caci = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
txtenc = input("enter a message you would like to be encoded : ")
encset = input("do you want this message encoded or decoded : ")
enckey = int(input("what key would you like to use : "))
for x in range(0, enckey):
    pop = caci.pop(0)
    caci.append(pop)
count = 0
if encset == "encoded":
    for x in txtenc:
        if txtenc[count] in deco:
            txtenc = txtenc.replace(txtenc[count], caci[deco.index(txtenc[count])])
        else:
            pass
    count = count + 1
    print(txtenc)