countries =["algeria", "angola", "benin", "botswana", "burkina faso", "burundi", "cabo verde", "cameroon", "central african republic", "chad", "comoros", "ivory coast", "djibouti", "democratic republic of the congo", "egypt", "equatorial guinea", "eritrea", "eswatini", "ethiopia", "gabon", "gambia", "ghana", "guinea", "guinea-bissau", "kenya", "lesotho", "liberia", "libya", "madagascar", "malawi", "mali", "mauritania", "mauritius", "morocco", "mozambique", "namibia", "niger", "nigeria", "republic of the congo", "rwanda", "sao tome & principe", "senegal", "seychelles", "sierra leone", "somalia", "south africa", "south sudan", "sudan", "tanzania", "togo", "tunisia", "uganda", "zambia", "zimbabwe"] #signed by 1ntl
print (" --- Countries Of Africa --- ")
difficulty = input ("please select difficulty : Easy - Medium - Hard : ")
option = True
while option:
    difficulty = str.lower(difficulty)
    if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
        print (difficulty, "difficlulty selected")
        option = False
    else:
        print ("invalid selection, make sure to select from list")
        difficulty = input ("please select difficulty : Easy - Medium - Hard : ")
score = 0
if difficulty == 'easy':
    lives = 10
if difficulty == 'medium':
    lives = 5
if difficulty == 'hard':
    lives = 3
while lives > 0 :
    if (len(countries) == 0):
        break
    if score == 54:
        break
    print("Number of countries to guess :",len(countries))
    print("score : ",score)
    print("lives left : ",lives)
    country = input("Enter the name of a country : ")
    country = str.lower(country)
    if country in countries:
        print ("good guess")
        score = score + 1
        countries.remove(country)
        
    else:
        print("invalid guess")
        lives = lives - 1
        if lives == 1:
            print ("last life, be carful")
if lives == 0:
    print("no more lives")
    print("you missed these countries", countries)
import time
while score == 54:
    print("congratulations! you won!")
    time.sleep(1)
    

