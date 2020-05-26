

class Card():
    def __init__(self, value):
        self.value = value
        self.name = None

a = Card(1)
b = Card(2)
deck = [a,b]

from random import shuffle

shuffle(deck)
for card in deck:
    print(card.value)

import src.main as main
print(main.myList[0])
