from Deck.card import Card
from Player.hand import Hand
class Player():
    def __init__(self,label, hand_label = ""):
        self.bet = 0#the money the player put in a bet
        self.money =0#the money the player has left over
        self.label = label#the name of the player
        self.hands = []#a list with all the hands the player has at play
        self.hands.append(self.createHand(hand_label))#append the first hand to the list
    def __str__(self):
        #returns a string of the player's hands and current status in the current game.
        
        player_string = "Player:%s\n" % str(self.label)
        player_string += "Money:%s\n" % str(self.money)
        player_string += "Bet:%s" % str(self.bet)
        return player_string

    def makeBet(self, bet):
        #this function will set the bet for the player, if the player bets 0 then the player wont play this round
        if bet == 0:
            print("%s won't play this round" %self.label)
            return  True
        elif bet < 0:
            print("Bet has to be at least 1")
            return False
        elif bet > self.money:
            print("Not enough Money to make that bet")
            return False
        print("%s will bet %s this round" %(self.label, str(bet)))
        self.bet = bet
        self.money -= bet
        return True
    
    def hit(self, card, hand_index = 0):
        #append the card to the given hand_index
        if hand_index >= len(self.hands):
            #check if the index exists
            return False
        self.hands[hand_index].hit(card)#append the card to the hand with the given hand_index
        return True

    def stand(self, hand_index = 0):
        #set the hand on the hand _index to stading and check if there any hands that can still play
        if hand_index >= len(self.hands):
            return False
        self.hands[hand_index].standing = True
        return True

    
    def setMoney(self, money):
        #set the amount of money the player has
        if money <= 0:
            print("Player can not have 0 or negative amount of Money!")
            return False
        self.money = money
        return True
    def havePlayableHand(self):
        if self.bet == 0: return False #if the player did not bet, the player is not playing
        #Check if there is at least one hand not standing or busted
        for hand in self.hands:
            if hand.atPlay():
                return True
        return False
    def isBusted(self):
        #if all the hands the player has are busted it returns True, otherwise false
        for hand in self.hands:
            if not hand.busted:
                return False
        return True
    def isStanding(self):
        #if at least one hand is standin return True, otherwise false
        for hand in self.hands:
            if hand.standing:
                return True
        return False
    def lose(self):
        #if the player loses reset the bet and annouce it to the player
        print("%s,You lose, Better Luck Next time!"% self.label)
        self.bet = 0

    def win(self):
        #if the player wins double the money on the bet add it to the players money and reset the bet
        print("You win!You got %s" %str(self.bet*2))
        self.money += self.bet*2
        self.bet = 0
    def reset(self):
        #reset the player to play again
        self.bet= 0
        del self.hands[:]
        self.hands.append(self.createHand())


    def createHand(self, new_hand_label = ""):
        #create a hand with a new label, labelr start with the letter a then moving b , c and so on
        hand_label = chr(65 + len(self.hands)) if new_hand_label == "" else new_hand_label
        return  Hand(hand_label)

    def split(self, hand_index):
        #split the deck and create a new hand
        if not self.hands[hand_index].hasPair():return False #if there are not pairs do nothing
        new_hand = self.createHand() #create the new hand
        pair_card = self.hands[hand_index].split()#get one of pair cards from the hand
        new_hand.hit(pair_card)#add the card to the new hand
        self.hands.append(new_hand)#add the new hand to the players platable hands
        
