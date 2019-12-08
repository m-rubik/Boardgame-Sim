from src.floors.floor import Floor

class Game():

    floor_0: Floor = None
    floor_1: Floor = None
    floor_2: Floor = None
    players: dict = dict()

    def __init__(self, num_players):
        self.generate_floors()
        self.randomly_assign_characters(num_players)
        self.choose_starting_coords()
        self.start_guard()

    def generate_floors(self):
        self.floor_0 = Floor(0)
        self.floor_1 = Floor(1)
        self.floor_2 = Floor(2)

    def randomly_assign_characters(self, num_players):
        from src.characters.characters import generate_character_stack
        from src.players.player import Player
        character_stack = generate_character_stack()
        for _ in range(0,num_players):
            new_player = Player(character_stack=character_stack)
            self.players[new_player.name] = new_player
    
    def choose_starting_coords(self):
        # This might be different for each player. Could use "input" boxes here
        for player_name, player in self.players.items():
            player.x_coord = 0
            player.y_coord = 0
            self.floor_0.players[player_name] = player
    
    def start_guard(self):
        self.floor_0.set_guard_starting_point()


if __name__ == "__main__":
    game = Game(num_players=1)
    print(1)