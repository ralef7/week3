#intro
import random
import time

def intro():
    print("Welcome to the Robert Alef blackjack game! Enjoy!\n")
#deck
suits = "h d c s".split()
faces = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

cards=[]
for suit in suits:
    for face in faces:
        cards.append(face+suit)

#shuffle
random.shuffle(cards)

#How we score this
def bj_score(x):
    score = 0
    for card in x:
        face = card[:-1]
        if face == "J":
            value = 10
        elif face == "Q":
            value = 10
        elif face == "K":
            value = 10
        elif face == "A":
            value = 11               
        else:
            value = int(face)
        score+= value

    return score
y = "true"
while y:
    intro()
            #Player 1:

    dealer_holding = [(cards.pop(0))]
    print("Dealer's face up card is {0}".format(dealer_holding))
    time.sleep(2)
    holding = [(cards.pop(0)), (cards.pop(0))]
    print("Your current hand is: {0}".format(holding))
    count = bj_score(holding)


    while count < 21 and input("Care to draw another card? y or n ") == "y":
        holding.append (cards.pop(0))
        count = bj_score(holding)
        print("Now, your hand is: {0} and you have {1} points".format(holding, count))

    if count > 21: 
        print("Sorry, you have {0}. You have busted.".format(count))

    elif count == 21:
        print("BlackJack! You win!")
    else:
        print("you have {0} points.\n".format(count))

#Dealer
    
    
        dealer_holding.append(cards.pop(0))
        dealer_count = bj_score(dealer_holding)
        time.sleep(2)
                        
        print("The dealer turns over {0}".format(dealer_holding))
        print("The dealer begins with {0} points.".format(dealer_count))
        time.sleep(2)
        while dealer_count < 17:
            print("The dealer is required to draw another card.")
            time.sleep(3)
            dealer_holding.append(cards.pop(0))
            dealer_count = bj_score(dealer_holding)
            print("The dealer now has {0}".format(dealer_holding))
            print("The dealer's new point total is {0}\n".format(dealer_count))
            time.sleep(2)

        if dealer_count > 21:
            print("The dealer busts! You're the winner!\n")
        elif dealer_count == 21:
            print("Shoot! The dealer drew 21. You lose.\n")
        elif dealer_count == count:
            print("Push.  Please take your bet back.\n")
        elif dealer_count > count:
            print("Shoot. The dealer wins.\n")
        else:
            print("You win!\n")
    j = input("Play again (y / n)? ")
    if j == "y":
       y = "true"
    if j == "n":
        break

    

    
          
          

            
