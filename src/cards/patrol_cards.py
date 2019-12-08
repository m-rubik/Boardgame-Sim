from random import shuffle

class PatrolCard():
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

def build_patrol_deck():
    patrol_deck = list()
    for x in range(0,4):
        for y in range(0,4):
            patrol_deck.append(PatrolCard(x,y))
    shuffle(patrol_deck)
    return patrol_deck
