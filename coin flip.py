import random
Money = 100000
while True:
    CoinFaces = ['h','t']
    SideChosen = False
    while SideChosen == False:
        CoinLand = random.choice(CoinFaces)

        while True:
            PlayerSide = input('choose a side! Heads or Tails (h/t) : ')
            PlayerSide = str.lower(PlayerSide)
            if PlayerSide == 'h'
                SideChosen = True
                break        
            elif PlayerSide == 't':
                SideChosen = True
                break
            else:
                print('Please select from list')
        if SideChosen == True:
            break
    while Money >= 1:
        print('you have', Money, 'remaining')
        while True:
            try:
                PlayerBet = int(input('Place a bet ammount within your budget : '))
                break
            except:
                print("thats not a number. try again.")
        if PlayerBet <= Money:
            Money = Money-PlayerBet
            print('you bet $', PlayerBet, 'you have $',Money ,'left')
            break
        if PlayerBet > Money:
            print('BROKE')
    if PlayerSide == CoinLand:
        Money = Money + PlayerBet * 2
        print("you win! you won", PlayerBet, "and now have $", Money)
    else:
        print("you lost! you chose", PlayerSide, "and the coin landed", CoinLand)
        if Money == 0:
            print("you have no more money!")
            break
            
    while True:
        if Money == 0:
            break
        PlayAgain = input("Do you want to play again? (y/n) : ")
        PlayAgain = str.lower(PlayAgain)
        if PlayAgain == "y":
            print("OK time to flip the coin!")
            break
        if PlayAgain == "n":
            print("Thanks For Playing!")
            break
        else:
            print("Please select from list.")
    if PlayAgain == "n":
        break
    if Money == 0:
        break