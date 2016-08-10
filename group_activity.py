
class Deck(object):
    def __init__(self):
        cards = []
        suits = ['H', 'C', 'S', 'D']
        values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def generateCards(self):
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        pass

class Cards(object):
    def __init__(self, suit, value):
        self.suit
        self.value

    def shuffle(self):
		i = len(self.card)
		while i > 0:
			rand_card = random.choice(self.card)
			temp = rand_card
			rand_card = self.card[i]
			self.card[i] = temp
			i -= 1

class Player(object):
    def __init__(self, name, hand):
        print "A new player has been created!"
        self.name = name
        self.hand = []

    def draw(self):
        # take an object "card" as "card(suit,value)" from object deck and add it to players hand  --- check
        # this will increase player's hand count by 1 and decrease deck count by 1
        Deck.cards = ['H2','H3','H4','H5']
        player.hand = []
        player.hand.append(cards(len(cards -1)))
        player.hand_count += 1
        cards(len(cards -1)).pop # is pop redundant? I just want to make sure that that card with its suit and value are no longer in the deck
        deck_count -= 1

    def deal(self):
        for x in len(player.hand):
            if x <= 5:
                draw()
            else: break


    def discard(self):
        cards = []
        player.hand = ['H1','H2','H3','H4','H5']
        deck.append(hand(len(hand -1)))
        deck_count += 1
        hand(len(hand -1)).pop
        hand_count -= 1

    def displayInfo(Player):
        print self.hand, self.name

John = Player("John", [])

#
# import random
# 5cards =[]
# while len(5cards) < 5:
# cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# rand_card = random.choice(cards)
# suit = ['H','C','S','D']
# rand_suit = random.choice(suit)
# deck_card = rand_card + rand_suit
# # it's too complicated to filter out all possible duplicates. you'd have to keep every generated comiinatino in memory
# # then
# print deck_card
#     i = 0
#     while i =< len(arr){
#         if deck_card != arr[i]{
#             i++;
#         }
#         else break;
#     }
#     5cards += deck_card
# }
