import random
import time
import threading


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __str__(self):
        return "%s of %s" % (self.value, self.suit)

    def __gt__(self, othercard):
        if self.suit == othercard.suit:
            if self.values.index(self.value) > self.values.index(othercard.value):
                return True
        else:
            return False
        if self.value.index(self.value) == self.values.index(othercard.value):
            if self.suit.index(self.suit) > self.suit.index(othercard.suit):
                return True
            else:
                return False


class Deck():
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(s, v) for s in self.suits for v in self.values]

    def __str__(self):
        description = "Deck: \n"
        for s in self.cards:
            description += str(s) + "\n"
        return description

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            print("Deal")
        return self.cards.pop()

    def getCard(self):
        card = self.cards[0]
        del self.cards[0]
        return card

    def checkDeck(self):
        if len(self.cards) == 0:
            return False
        return True

    def newDeck(self):
        self.cards = [Card(s, v) for s in self.suits for v in self.values]


# player_deck = [[''] for i in range(4)]


def player_cards(id, mode):
    global d
    player_deck = []
    st = 0.0
    while d.checkDeck():
        if st != 0.0:
            st = 0.01 - st
            time.sleep(st)
        player_deck.append(d.getCard())
        st = random.uniform(0, 0.01)
        time.sleep(st)
    print("Player {0}'s deck is:\n{1}".format(id+1, player_deck))


d = Deck()
d.shuffle()
players = []

for i in range(4):
    player = threading.Thread(target=player_cards, args=(i, False))
    player.start()
    players.append(player)
for p in players:
    p.join()

for i in range(4):
    print("Player {0}'s deck is:\n".format(i + 1))
    for
