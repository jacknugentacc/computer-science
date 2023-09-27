countries =["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
print (" --- Countries Of Africa --- ")
score = 0
lives = 3
while lives > 0 :
    if (len(countries) == 0):
        break
    print("Number of countries to guess")
    print(len(countries))
    print("score : ",score)
    print("lives left : ",lives)
    country = input("Enter the name of a country : ")
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
if score == 54:
    print("you win")
