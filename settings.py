import random
class Settings():
    def __init__(self):
        self.block_width = 40

        self.screen_width = 750
        self.screen_height = 750

        self.screen_color = 255, 255, 255
        self.grid_color = 0, 0, 0
        self.lose_color = 255, 0, 0

        self.colors = [[(246, 255, 0), 1], [(181, 45, 45), 2], [(74, 131, 255), 3], [(235, 129, 38), 4]]
