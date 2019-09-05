import random
def blackjacksum(hand):# computes the sum by assuming appropriate value
    if sum(hand)<=11:  # of Ace card(either 1 or 11) acc. to the sum.
        if hand[0]==1:
            hand[0]==11
        elif hand[1]==1:
            hand[1]==11
    elif sum(hand)>21:
        if hand[0]==11:
            hand[0]==1
        elif hand[1]==11:
            hand[1]==1
    return sum(hand),hand
###################################
def move(hand,cards,bet):
    sum,hand[0]=blackjacksum(hand[0])
    if sum>=21:
        if sum>21:
            print("You got busted!")
        else:
            print("Blackjack!")
        return hand,bet
    print("Your sum is",sum)
    choice=input("Press H to Hit, S to Stand, D to Double-Down, P to sPlit")

    if choice in['H','h']:
        newcard=random.choice(cards)
        print("Newcard is",newcard)
        hand[0].append(newcard)
        print("Updated hand is",hand[0])
        sum, hand[0] = blackjacksum(hand[0])
        print("Your sum is", sum)
        hand,bet=move(hand,cards,bet)
        return hand,bet

    if choice in['S','s']:
        return hand,bet

    if choice in['D','d']:
        newcard = random.choice(cards)
        print("Newcard is", newcard)
        hand[0].append(newcard)
        print("Updated hand is", hand[0])
        sum, hand[0] = blackjacksum(hand[0])
        print("Your sum is", sum)
        bet[0]=bet[0]*2
        print("Your new bet is", bet[0])
        return hand,bet

    if choice in['P','p']:
        if hand[0][0]==hand[0][1]:
            if not hand[0][0]==1:
                splitHand1=[[0,0]]
                splitHand2=[[0,0]]
                newcard1=random.choice(cards)
                print("Newcard for first split is",newcard1)
                newcard2 = random.choice(cards)
                print("Newcard for second split is", newcard2)
                splitHand1[0][0] = hand[0][0]
                splitHand2[0][0] = hand[0][0]
                splitHand1[0][1] = newcard1
                splitHand2[0][1] = newcard2
                print("Split hands are",splitHand1,", ",splitHand2)
                sum1,splitHand1[0] = blackjacksum(splitHand1[0])
                sum2, splitHand2[0] = blackjacksum(splitHand2[0])
                print("Your sum for split 1 is", sum1)
                print("Your sum for split 2 is", sum2)
                splitHand1,bet1=move(splitHand1,cards,bet)
                splitHand2,bet2=move(splitHand2,cards,bet)
                splitHand1.extend(splitHand2)#converting both hands to a single list
                bet1.extend(bet2)#converting both bets to a single list
                return splitHand1,bet1
            else:
                print("Sorry,you can't split aces")
                hand,bet=move(hand,cards,bet)
                return hand,bet
        else:
            print("Sorry, you can only split hands with identical cards")
            hand, bet = move(hand, cards, bet)
            return hand, bet
############################################################################

# Main driver code
print("Welcome to the casino! Let's play blackjack!")
n=int(input("How many players are playing?"))
players=[]
dealerhand=[]
for i in range(n):
    name=input("Enter name, Player{}".format(i+1))
    players.append({"name":name,"hands":[],"bets":[],'profit':[]})
print(players)
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
print("Let's start the game!")
for i in range(n):
    print(players[i]["name"],",How much are you betting?")
    bet=int(input())
    players[i]["bets"].append(bet)
print("Dealing the cards............")
for i in range(n):
    print(players[i]["name"],"Your cards....")
    hand=[random.choice(cards),random.choice(cards)]
    players[i]["hands"].append(hand)
    print(hand)
dealerhand=[random.choice(cards),random.choice(cards)]
print("Dealer hand:",dealerhand[0],",hidden")
for i in range(n):
    print("It's your turn,", players[i]['name'])
    players[i]['hands'],players[i]['bets']=move(players[i]['hands'],cards,players[i]['bets'])
    print(players[i]['hands'],"      ",players[i]['bets'])
print("Dealer hand:",dealerhand)
while sum(dealerhand)<17:
    dealerhand.append(random.choice(cards))
for i in range(n):
    print("Let's see your results")
    for j in range(len(players[i]['hands'])):
        hand=players[i]['hands'][j]
        bet=players[i]['bets'][j]
        sum,hand=blackjacksum(hand)
        dealersum,dealerhand=blackjacksum(dealerhand)
        print("For the hand-",hand,'sum is-',sum)
        if len(hand)==2 and sum==21:
            print("Blackjack!")
            players[i]['profit'].append(bet*1.5)
        elif sum>21:
            print("Busted")
            players[i]['profit'].append(bet * -1)
        elif dealersum>21:
            print("Dealer Busted")
            players[i]['profit'].append(bet*1)
        elif dealersum>sum:
            print("You lost")
            players[i]['profit'].append(bet * -1)
        elif sum>dealersum:
            print("You win")
            players[i]['profit'].append(bet * 1)
        elif sum==21 and dealersum==21 and len(dealerhand)==2 and len(hand)>2:
            print("You lost")
            players[i]['profit'].append(bet * -1)
        elif sum==dealersum:
            print("Push")
            players[i]['profit'].append(bet * 0)




