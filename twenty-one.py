from Player.player import Player
from Deck.deck import Deck
from Player.hand import Hand

players = []#list to store the  players currently playing
deck = Deck()#The Deck being used for the game
bank = Hand("Bank")#the bank
HIT_INPUT = "H"
STAND_INPUT = "S"
SPLIT_INPUT = "$"

def addPlayers():
    #add new players to the game
    num_of_players = 0
    
    while num_of_players <1 or num_of_players > 3:
        #get the number of players being added
        try:
            num_of_players = int(input("How many players will play today? 1-3:"))
            if num_of_players <1 or num_of_players > 3:
                print("Invalid number of players")
        except ValueError:
            print("Not a Number!")
    #create all new players
    for new_player in range(num_of_players):
        createPlayer()


def createPlayer():
    #create a new player
    money = 0
    new_player =  Player("P"+ str(len(players)+1))#create a player with a new label

    while money <= 0:
        #set the money on the player
        try:
            money = int(input("How much money does %s have " % new_player.label)) #get input from the user
            if new_player.setMoney(money):break#try to put the money in the Player Objecet if it meets parameters
        except ValueError:
            print("Not a Number!")#money value must be some integer
    players.append(new_player)
        

def play():
    firstPass() 
    while checkIfCanPlay(): # if there is at least one player that has a not busted or standing hand the game continues
        for player in players:
                playersTurn(player)#do the players turn
        
        if not checkIfCanPlay():
            if haveStandingPlayer():
                banksTurn()
                if bank.isBusted():
                    bankBusted()
                else:
                    bankStanding()
            else:
                allPlayerslose()

            playAgain()

def firstPass():  
    #the first pass when the game will deal one card to each player
    
    deck.shuffle()
    print("Dealing cards to all players\n")
    for player in players:
        #deal each player a card
        hit(player.hands[0])
        print(playerStatusString(player))

    askForBets()#Ask the players for bets

def playerStatusString(player, hand = None):
    #get the player and all their hands status
    string = "-"*40 +"\n"
    string +=str(player) + "\n"
    if hand == None:
        for h in player.hands:
            string+= "\n"+str(h)
    else:
        string += "\n" + str(hand)
    
    return string

def askForBets():
    #make each player make a bet
    for player in players:
        makeBet(player)

def makeBet(player):
    bet = 0 # the bet the player will make
    print(playerStatusString(player))  
    while True:
        try:          
            bet = int(input("%s how much will you bet? if you bet 0 you won't play this round:" %player.label))#ask for input
            if player.makeBet(bet):break #if the bet mets all constrains we can break out of the loop
        except ValueError:
            print("Invalid Number!")


def checkIfCanPlay():
    for player in players:
        if player.havePlayableHand(): return True
    return False


def playersTurn(player):
    #the players turn where they can choose their next action
    if not player.havePlayableHand():
        return #if the player does not have any avaiable hand to play the player is unavailable
    
    for hand_index ,hand in enumerate(player.hands):
        if not hand.atPlay():continue #if the hand is busted or standing then we skip this hand
        print(playerStatusString(player, hand))
        i = getPlayerInput(hand)
        #do the action ask by the player
        if i == HIT_INPUT: 
            hit(hand)
            
            print(playerStatusString(player,hand))
            print("HIT")
            if(hand.isBusted()):print("Busted!")
        elif i == STAND_INPUT:
            print(playerStatusString(player,hand))
            stand(hand)
            print("STAND")

        elif i == SPLIT_INPUT:
            player.split(hand_index)
            print(playerStatusString(player,hand))
            print("SPLIT")
       
        else:print("Invalid Input!")        

def getPlayerInput(hand):
    #get the player input based on the hands content
    input_string = "What would you like to do?\n | %s: Hit | %s: Stand |" %(HIT_INPUT, STAND_INPUT)
    i =  ""
    if hand.hasPair():
        #if the hand has a pair give the player the choice to split
        input_string += "%s: Split |\n" %SPLIT_INPUT #if the hand has a pair the player can split this hand:
        while True:
            i = input(input_string).upper()
            if i not in [HIT_INPUT, STAND_INPUT, SPLIT_INPUT]:
                #if the input is not valid announce it to the player
                print("Invalid input")
            else:
                break            
    else:
        input_string += "\n"
        while True:
            i = input(input_string).upper()
            if i not in [HIT_INPUT, STAND_INPUT]:
                #if the input is not valid announce it to the player
                print("Invalid input")
            else:
                break
    return i



def hit(hand):
    hand.hit(deck.deal())#deal the hand a new card

def stand(hand):#simple function to make a hans"stand"
    hand.stand()

def haveStandingPlayer():
    #returns true if there is at least one player with a hand standing
    for player in players:
        if  player.isStanding():
            return True
    return False

def banksTurn():
    #play the banks turn
    while bank.atPlay():
        hit(bank)#hit the bank
        #if the banks value is over or equal to 17 the bank stansa
        if bank.value >= 17 and not bank.isBusted(): 
            stand(bank)
        print(bank)
        print("-"*40)

def bankBusted():
    #if the bank does not play this round, the winner is determined by who is left standing
    for player in players:
        if player.bet == 0: continue
        if player.isStanding():
            player.win()
        else:
            player.lose()
        print(playerStatusString(player))
def bankStanding():
    for player in players:
        if player.bet == 0: continue
        compareAgainstBank(player)

def compareAgainstBank(player):
    #check if there is at least one hand that wins against the bank
    for hand in player.hands:
        print(playerStatusString(player, hand))
        if handWinsAgainstBank(hand):
            player.win()
            return
    player.lose()

def handWinsAgainstBank(hand):
    #compare a hand with the bank to determine if player won
    if hand.isBusted():
        print("Hand is Busted.")
        return False
    elif hand.value == bank.value:
        #if players hand has the same value as the bank, this hand loses
        print("Hand %s  scored the same as the bank" % hand.label)
        return False
    elif hand.value < bank.value:
        #if the player has a lower value than the bank, this hand loses
        print("Hand %s scored lower than the bank" %hand.label)
        return False

    elif hand.value > bank.value:
        #if the player has a higher value than the bank, the player wins
        print("Hand %s scored Higher than the bank!" %hand.label)
        return True
    return False




def resetGame():
    #reset all players to their starting positions
    for player in players:
        player.reset()
    bank.reset()
    deck.reset()

def allPlayerslose():
    for player in players:
        if player.bet == 0: continue
        print(playerStatusString(player))
        player.lose()
def playAgain():
    #ask the players if they will like to play again
    #if yes then all players hands get reset and the everyone is dealt one card
    while True:
        i = input("Would You like to play again? Y: yes | N: no|\n").upper()
        if i =="Y":
            resetGame()
            print(bank)
            firstPass()
            return True
        elif i == "N":
            return False



def game_exit():
    print('Thank you for playing, hope to see you soon!')
    exit()

def main():
    print("-------------Welcome to Twenty One-------------")
    addPlayers()
    play()
    game_exit()
	

if __name__ == "__main__":

    main()
