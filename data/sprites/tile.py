import pygame as pg


class Tile(pg.sprite.Sprite):

    revealed: bool = False
    x: int
    y: int
    size: int
    floor: int
    
    def __init__(self, image_path, x, y, floor, size=100):

        super().__init__()

        self.x = x
        self.y = y
        self.floor = floor
        self.size = size
        self.image_path = image_path
        
        self.image = pg.image.load("resources/graphics/tiles/tile_back.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()

        #  1        2      3       4       5      Next floor
        # 0 100 120 220 240 340 460 560 580 680   720
        self.rect.x = self.x*self.size + 20*self.x + 5*(self.size+20)*self.floor
        self.rect.y = self.y*self.size + 20*self.y

    def reveal(self):
        self.image = pg.image.load(self.image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.size, self.size))