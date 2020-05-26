from src.characters.characters import Character
from src.characters.characters import get_random_character
import names
import src.database as db

class Player():

    name: str = None
    character: Character = None
    x_coord: int = None
    y_coord: int = None
    current_floor: int = 0
    stealth_level: int = 3
    
    def __init__(self, name=None, character_stack=None):
        if name is None:
            self.name = names.get_full_name()
        else:
            self.name = name
        self.character = get_random_character(character_stack)

    def lose_stealth(self):
        self.stealth_level = self.stealth_level - 1
        if self.stealth_level == 0:
            print(self.name, "has been caught!")
            del db.game_dict['Players'][self.name]    
        else:
            print(self.name, "has lost 1 stealth. Remaining stealth:", self.stealth_level)