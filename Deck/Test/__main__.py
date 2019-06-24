from Deck.deck import Deck, SUITS, RANK_AND_VALUE

def testShuffle(deck = Deck()):
	#test that the deck has been shuffled
	print("Testing deck shuffling\n")
	printDeckComp(deck)
	dupe_deck = deck.copyDeck()
	print()
	print("Shuffling Deck\n")
	deck.shuffle()
	printDeckComp(deck)
	if dupe_deck == deck:
		#if the the original deck and the old deck have the cards in the same position then the deck did not get shuffled
		raise RuntimeError("Deck was not shuffled")


def testDeckSize(deck):
	#test that the deck has the correct deck size
	print("Testing for the correct size of the Deck\n")
	print("The Deck Has %s cards" %len(deck.cards))
	if len(deck.cards) != 52:
		#if the deck does not have 52 cards then there are new cards in the deck
		#this will be edited when we handle multiple decks
		raise RuntimeError(" incorrect number of cards")



def testSuits(deck = Deck()):
	#check that there are the correct number of suites in the deck
	print("Testing for correct number of suits\n")
	for suit in SUITS:
		num = 0
		for card in deck.cards:
			if card.suit == suit:
				num +=1
		print("The Deck Has %s %s" %(num, suit))
		if num !=13:
			#if there are no 13 cards per suit something is wrong
			#this will be edited when we handle multiple decks
			raise RuntimeError("incorrect number of %s suits" %suit)


def testForDuplicates(deck= Deck()):
	#Test for duplicates
	print("Testing for duplicates\n")
	dupe_deck = deck.copyDeck()
	result = ""
	for card in deck.cards:
		count = 0
		for s_card in deck.cards:
			if card == s_card:
				count += 1
		result +=str(card) +":"+str(count)+"|"
		#if there are more than one of each card there are duplicates
		#this will be edited when we handle multiple decks
		if count > 1: raise RuntimeError("To many %s cards %s where found" % (str(card), str(count)))
	print(result)

def testCardValue(deck = Deck()):
	#Test that each card has the righ Value
	print("Testing for correct rank value\n")
	for card in deck.cards:
		print(card+":"+card.value)
		if card.value != RANK_AND_VALUE[card.rank]:
			#if the cards do not  have the correct value something went wrong
			raise RuntimeError("Card %s has the value of %s" %(str(card), card.value))

def testCardIntegrity(deck = Deck()):
	#Test that cards have a valid rank and suit
	print("Testing Cards integrity")
	for card in deck.cards:
		print(card)
		#if the card has a none existen rank or suit raise an error
		if card.suit not in SUITS: raise RuntimeError("Suit %s does not exist" %(card.rank))
		if card.rank not in RANK_AND_VALUE.keys(): raise RuntimeError("Rank %s does not exist" %(card.rank))



def TestDeal(deck = Deck()):
	#Testing the deal function
	print("Testing the Deal function\n")
	printDeckComp(deck)
	print()
	result = ""
	while deck.cards:
		result += str(deck.deal()) + "|"
	print(result)


def printDeckComp(deck):
	#annouce you are pringting the deck and print it
	print("the deck composition is:")
	print(deck)	
def test():
	divider = "-"*30
	deck = Deck()
	print("Created the Deck")
	print(divider)
	testShuffle(deck)
	print(divider)
	testDeckSize(deck)
	print(divider)
	testSuits(deck)
	print(divider)
	testForDuplicates(deck)
	print(divider)
	TestDeal()
	print(divider)

if __name__ == "__main__":


    test()
