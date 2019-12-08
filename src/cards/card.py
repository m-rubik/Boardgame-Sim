from src.main import test_func

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
