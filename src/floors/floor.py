from src.guards.guard import Guard
from src.cards.patrol_cards import build_patrol_deck
import src.database as db

class Floor():

    number: int = None
    guard: Guard = None
    patrol_deck: list = list()
    patrol_discard_pile: list = list()

    def __init__(self, number):
        self.number= number
        self.guard = Guard(number)
        self.patrol_deck = build_patrol_deck()

    def set_guard_starting_point(self):
        self.guard.x_coord, self.guard.y_coord = self.patrol_deck[0].x_coord, self.patrol_deck[0].y_coord
        self.patrol_discard_pile.append(self.patrol_deck.pop(0))
        self.check_seen()

    def check_seen(self):
        for player_name, player in db.game_dict['Players'].items():
            if player.current_floor == self.number:
                if player.x_coord == self.guard.x_coord and player.y_coord == self.guard.y_coord:
                    print(player_name, "has been seen by guard on floor", self.number)
                    player.lose_stealth()
                else:
                    print(self.guard.x_coord, self.guard.y_coord)

if __name__ == "__main__":
    pass
