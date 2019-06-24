#simple  Class to store and mange an single card
class Card():
    def __init__(self, suit, rank, value):
        self.suit = suit # the suit of the cards (Hears, Dimonds, Spade, Clubs)
        self.rank = rank #the rank of the card (A, K,Q,J, 2-10)
        self.value = value#The given point value of the card

    def __str__(self):
    	#returns a string with the first letter of the card's suit and the cards rank
    	#for example 4 of Diamonnds will be D4
        return self.suit[0] + self.rank
    
    def __eq__(self, card):
    	#used to compare two cards, if they have the same rank and suit it will return True otherwise False
    	return (self.suit == card.suit and self.rank == card.rank)
