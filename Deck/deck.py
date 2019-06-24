from random import shuffle
from Deck.card import Card
#List for all available suits
SUITS = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
#Dictionary to keep all rank and rank values
RANK_AND_VALUE = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 1, 'Q': 2, 'K': 3}

#Class used to store and manage the deck and all containing cards
class Deck():
    def __init__(self):
        self.cards = []#list to keep all cards currently in the deck
        self.reset()

    def shuffle(self):
        print("Deck Is shuffled")
        shuffle(self.cards)#randomly shuffle the cards list

    def deal(self):
        #pop the last element on the list(the top of the deck)
       return self.cards.pop()
    
    def copyDeck(self):
        #this is maninly used for testing
        #it will create a new Deck Object with new Cards all in the exact same postion as the current Object
        dupe_deck = Deck()
        for card in self.cards:
            dupe_deck.cards.append(Card(card.suit, card.rank, card.value))
        return dupe_deck
    def reset(self):
        del self.cards[:]
        for suit in SUITS:
            #create a new card for each suit and rank available
            for rank in RANK_AND_VALUE:
                self.cards.append(Card(suit, rank, RANK_AND_VALUE[rank]))        


    def __str__(self):
        #return a string of the order the cards are in the deck
        deck_comp = ""
        for card in self.cards:
            deck_comp += str(card) + " "
        return deck_comp

    def __eq__(self,deck):
        #mainly used for testing
        #if all the cards are in the same position it returns true
        if len(deck.cards) != len(self.cards):
            return False
        for i in range(len(self.cards)):
            if self.cards[i] != deck.cards[i]: return False
        return True


