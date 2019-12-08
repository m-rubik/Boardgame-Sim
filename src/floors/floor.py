from src.guards.guard import Guard
from src.cards.patrol_cards import build_patrol_deck

class Floor():

    number: int = None
    guard: Guard = None
    patrol_deck: list = list()
    patrol_discard_pile: list = list()
    players: dict = dict()

    def __init__(self, number):
        self.number= number
        self.guard = Guard(number)
        self.patrol_deck = build_patrol_deck()

    def set_guard_starting_point(self):
        self.guard.x_coord, self.guard.y_coord = self.patrol_deck[0].x_coord, self.patrol_deck[0].y_coord
        self.patrol_discard_pile.append(self.patrol_deck.pop(0))

if __name__ == "__main__":
    pass
