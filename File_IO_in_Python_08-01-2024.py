file = open ("C:\\Users\\19JackHalligan.ACC\\Downloads\\remainder.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file = open ("C:\\Users\\19JackHalligan.ACC\\Downloads\\remainder.txt", "r")
print(file.read())
file = open ("C:\\Users\\19JackHalligan.ACC\\Downloads\\remainder.txt", "r")
for line in file:
    print(file.read())
file.close()
file = open ("C:\\Users\\19JackHalligan.ACC\\Downloads\\courses.csv","r")

count = 0
for line in file:
    line = line[:-1]
    fields = line.split(",")
    if fields[0] == "CS":
        print(fields[0],fields[1])
        count+=1
file.close()

file = open ("C:\\Users\\19JackHalligan.ACC\\Downloads\\results.txt","r")

UL = 0
DCU = 0
TCD = 0
for line in file:
    line = line [:-1]
    fields = line.split(",")
    if fields[1] == "UL":
        UL+=1
    if fields[1] == "DCU":
        DCU+=1
    if fields[1] == "TCD":
        TCD+=1
print("UL has",UL,"result(s)")
print("DCU has",DCU,"result(s)")
print("TCD has",TCD,"result(s)")

file.close()