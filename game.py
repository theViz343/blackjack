import random
def pprinthand(hand):
    temphand=hand[:]
    for i in range(len(temphand)):
        if temphand[i]==1 or temphand[i]==11:
            temphand[i]='A'
    return temphand
def pprinthandlist(handlist):
    newhandlist=[]
    for hand in handlist:
        newhandlist.append(pprinthand(hand))
    return newhandlist
def calcprof(handlist,profitlist):
    profit=0
    for i in range(len(handlist)):
        profit+=profitlist[i]
        return profit
##################################
def blackjacksum(hand):# computes the sum by assuming appropriate value
    if sum(hand)<=11:  # of Ace card(either 1 or 11) acc. to the sum.
        for i in range(len(hand)):
            if hand[i]==1:
                hand[i]=11
                break
    elif sum(hand)>21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                break
    return sum(hand),hand
###################################
def move(hand,cards,bet):# Here, hand is a nested list inside a list. It is a list of all hands of a player.
    sum_,hand[0]=blackjacksum(hand[0])
    print("Your hand is", pprinthand(hand[0]))
    print("Your sum is", sum_)
    if sum_>=21:
        if sum_>21:
            print("You got busted!")
        else:
            print("Blackjack!")
        return hand,bet
    choice=input("Press H to Hit, S to Stand, D to Double-Down, P to sPlit")

    if choice in['H','h']:
        newcard=random.choice(cards)
        print("Newcard is",newcard)
        hand[0].append(newcard)
        print("Updated hand is",pprinthand(hand[0]))
        sum_, hand[0] = blackjacksum(hand[0])
        hand,bet=move(hand,cards,bet)
        return hand,bet

    if choice in['S','s']:
        return hand,bet

    if choice in['D','d']:
        newcard = random.choice(cards)
        print("Newcard is", newcard)
        hand[0].append(newcard)
        print("Updated hand is", pprinthand(hand[0]))
        sum_, hand[0] = blackjacksum(hand[0])
        print("Your sum is", sum_)
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
                print("Split hands are",pprinthand(splitHand1),", ",pprinthand(splitHand2))
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
choice='y'
while choice in "Yy":
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
        print(pprinthand(hand))
    dealerhand=[random.choice(cards),random.choice(cards)]
    print("Dealer hand:",pprinthand(dealerhand)[0],",hidden")
    print(players)
    for i in range(n):
        print("It's your turn,", players[i]['name'])
        players[i]['hands'],players[i]['bets']=move(players[i]['hands'],cards,players[i]['bets'])
        print("Your hands and respective bets for this round are:")
        print(pprinthandlist(players[i]['hands']),"      ",players[i]['bets'])
    print("Dealer hand:",pprinthand(dealerhand))
    dealersum,dealerhand=blackjacksum(dealerhand)
    print("Dealer's sum is",dealersum)
    while dealersum<17:
        print("Dealer draws another card")
        dealerhand.append(random.choice(cards))
        print("Newcard is",dealerhand[-1])
        dealersum,dealerhand=blackjacksum(dealerhand)
        print("Dealer's sum is", dealersum)
        print("Dealer's hand is", pprinthand(dealerhand))
    for i in range(n):
        print("Let's see your results",players[i]['name'])
        for j in range(len(players[i]['hands'])):
            hand=players[i]['hands'][j]
            bet=players[i]['bets'][j]
            sum_,hand=blackjacksum(hand)
            dealersum,dealerhand=blackjacksum(dealerhand)
            print("For the hand-",pprinthand(hand),'sum is-',sum_)
            if len(hand)==2 and sum==21:
                print("Blackjack!")
                profit=bet*1.5
                players[i]['profit'].append(bet*1.5)
            elif sum_>21:
                print("Busted")
                profit = bet * -1
                players[i]['profit'].append(bet * -1)
            elif dealersum>21:
                print("Dealer Busted")
                profit = bet * 1
                players[i]['profit'].append(bet*1)
            elif dealersum>sum_:
                print("You lost")
                profit = bet * -1
                players[i]['profit'].append(bet * -1)
            elif sum_>dealersum:
                print("You win")
                profit = bet * 1
                players[i]['profit'].append(bet * 1)
            elif sum_==21 and dealersum==21 and len(dealerhand)==2 and len(hand)>2:
                print("You lost")
                profit = bet * -1
                players[i]['profit'].append(bet * -1)
            elif sum_==dealersum:
                print("Push")
                profit = bet * 0
                players[i]['profit'].append(bet * 0)
            print("Profit is-",profit)
    choice=input("Do you wish to play another round?Y/n")
print("OK then, Let's see the results")
for i in range(n):                     # total profit calculation
    name=players[i]['name']
    profit=calcprof(players[i]['hands'],players[i]['profit'])
    if profit>=0:
        print(name,", your total profit is",profit)
    else:
        print(name, ", your total loss is", profit * -1)
