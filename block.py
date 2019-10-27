import pygame
from pygame.sprite import Sprite
import random

class Block(Sprite):
    def __init__(self,settings,screen):
        super(Block,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,settings.block_width,settings.block_width)
        self.width = settings.block_width

        self.board_x = 0
        self.board_y = 0

        self.y = float(self.rect.y)
        self.center = float(self.rect.centerx)

        self.color,self.color_value = settings.colors[random.randint(0,9)]

        self.last = pygame.time.get_ticks()

        self.tick_length = 1000

    def speed_up(self):
        self.tick_length = 100

    def slow_down(self):
        self.tick_length = 1000

    def update(self):
        self.y += self.width
        self.rect.y = self.y
        self.last = pygame.time.get_ticks()

    def draw_block(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def move_right(self,x,board):
        collide = False
        for col in board:
            for block in col:
                if isinstance(block, Block):
                    if block.rect.left == self.rect.right and block.rect.y == self.rect.y:
                        collide = True

        if self.rect.right < self.screen.get_rect().centerx+self.width*3 and not collide:
            self.center = x
            self.center += self.width
            self.rect.centerx = self.center
            return True
        else:
            return False

    def move_left(self,x,board):
        collide = False
        for col in board:
            for block in col:
                if isinstance(block, Block):
                    if block.rect.right == self.rect.left and block.rect.y == self.rect.y:
                        collide = True

        if self.rect.left > self.screen.get_rect().centerx-self.width*3 and not collide:
            self.center = x
            self.center -= self.width
            self.rect.centerx = self.center
            return True
        else:
            return False

    def check_bottom(self,board):
        collide = False
        for col in board:
            for block in col:
                if isinstance(block, Block):
                    if block.rect.top == self.rect.bottom and block.rect.x == self.rect.x:
                        collide = True

        if self.rect.bottom < self.screen.get_rect().centery+self.width*6 and not collide:
            return True
        else:
            return False
