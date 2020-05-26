import pygame as pg
import random
from data.sprites.tile import Tile
pg.init()


class Game():

    screen_width: int
    screen_height: int
    grid_width: int
    grid_height: int
    num_floors: int
    tile_size: int
    game_over: bool = False
    clock: pg.time.Clock

    def __init__(self, grid_width=4, grid_height=4, num_floors=3, screen_width=1500, screen_height=500, tile_size=75):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.num_floors = num_floors
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile_size = tile_size
        self.screen_size = (self.screen_width, self.screen_height)

    def setup_game(self):

        self.screen = pg.display.set_mode(self.screen_size)
        self.screen.fill((255, 255, 255))

        pg.display.set_caption("Sample Game Title")
        
        # Container for all tile sprites
        self.tiles_group = pg.sprite.Group()
        self.tiles_dict = {}

        for index_floor in range(self.num_floors):
            for index_width in range(self.grid_width):
                for index_height in range(self.grid_height):
                    # print(index_width, index_height)
                    tile_number = random.randint(1,2)
                    tile = Tile(image_path="resources/graphics/tiles/"+str(tile_number)+".png", x=index_width, y=index_height, floor=index_floor, size=self.tile_size)
                    self.tiles_group.add(tile)
                    self.tiles_dict[(index_floor, index_height, index_height)] = tile

        self.tiles_group.update()
        self.tiles_group.draw(self.screen)
        pg.display.flip()

        self.tiles_dict[(0,0,0)].reveal()
        # TODO: Add guard decks
        # TODO: Shuffle other stuff?

    def play(self):

        self.game_over = False
        self.clock=pg.time.Clock()
        
        while not self.game_over:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    self.game_over=True
                    
            #Game Logic
            self.tiles_group.update()
    
            # #Drawing on Screen
            # #Draw The Road
            # pg.draw.rect(screen, GREY, [40,0, 200,300])
            # #Draw Line painting on the road
            # pg.draw.line(screen, WHITE, [140,0],[140,300],5)
            
            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            self.tiles_group.draw(self.screen)
    
            #Refresh Screen
            pg.display.flip()
    
            #Number of frames per secong e.g. 60
            self.clock.tick(60)
        
        pg.quit()

if __name__ == "__main__":
    g = Game()
    g.setup_game()
    g.play()