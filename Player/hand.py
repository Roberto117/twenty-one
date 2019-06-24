from Deck.card import Card

BUSTED_VALUE = 21
class Hand():
    def __init__(self, label):
        self.cards = []#list to store the cards
        self.value = 0#the total value of the cards
        self.pair = -1#true if there is two card with the same rank on the deck
        self.standing = False#true if the hand is standing
        self.label = label#label for the hans(since a player can have multiple hands)
    def __str__(self):
        #returns a string of the cards status
        
        hand_comp = "hand:%s\ncards:" %self.label
        for card in self.cards:
            #get the string of each card
            hand_comp += str(card)+ " "
        hand_comp +="\nValue:%s\n"%str(self.value)
        hand_comp +="Status:"
        if self.standing:
            hand_comp +="Standing\n"
        else:
            hand_comp += "Busted\n" if self.isBusted() else "Playing\n"
        return hand_comp


    def hit(self, card):
        #if the player hits we append the given card to the hand
        #check if there are pairs
        self.cards.append(card)
        self.value += card.value
        self.checkForPairs()
    def isBusted(self):
        return self.value >= BUSTED_VALUE # if the hand has a higher or equal value to the player the hand is Busted and return True otherwise False
    
    
    def atPlay(self):
        #if the hand is not standing or busted return True otherwise False
        if not self.standing and not self.isBusted():
            return True
        else:
            return False
    
    def checkForPairs(self):
        seen = []
        for card_index, card in enumerate(self.cards):
            if card.rank not in seen:
                seen.append(card.rank)
            else:
                self.pair = card_index
                return
        self.pair = -1
    
    def hasPair(self):
        #return True if pair is not -1 (has an index to some pair)
        return self.pair != -1
    
    def split(self):
        #remove one of the pairs if there are pairs
        if not self.hasPair: return False
        pair_card = self.cards.pop(self.pair) #remove the pair card for the hand
        self.checkForPairs()#check if there are still any pairs
        self.value -= pair_card.value
        return pair_card
    def stand(self):
        self.standing = True
    
    def reset(self):
        del self.cards[:]
        self.value = 0
        self.pair = -1
        self.standing = False