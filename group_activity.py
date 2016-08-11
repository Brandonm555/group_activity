
class Deck(object):
    def __init__(self):
        self.cards = []

    def generateCards(self, suits = ['H', 'C', 'S', 'D'], values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']):
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        # didn't quite get this to work out, but we decided to keep moving as none of us were near the minimum target for the day.
		# i = len(self.card)
		# while i > 0:
		# 	rand_card = random.choice(self.card)
		# 	temp = rand_card
		# 	rand_card = self.card[i]
		# 	self.card[i] = temp
		# 	i -= 1
        pass

    def displayInfo(self):
        print self.cards


class Card(object):
    def __init__(self, suit, value):
        print "A new card has been created!"
        self.suit = suit
        self.value = value

    def displayInfo(self):
        print self.value, self.suit

class Player(object):
    def __init__(self, name, hand):
        print "A new player has been created!"
        self.name = name
        self.hand = []

    def draw(self,deck):
        # take an object "card" as "card(suit,value)" from object deck and add it to players hand  --- check
        # this will increase player's hand count by 1 and decrease deck count by 1
        self.hand.append(deck.cards[len(deck.cards) - 1])
        deck.cards.pop() # is pop redundant? I just want to make sure that that card with its suit and value are no longer in the deck

    def deal(self, deck):
        while len(self.hand) < 6:
            self.draw(deck)


    def discard(self):
        deck.cards.append(self.hand[len(self.hand) - 1])
        self.hand.pop()

    def displayInfo(self):
        print self.name, self.hand

KennyLoggins = Player('KennyLoggins', [])
KennyLoggins.draw(Deck)
