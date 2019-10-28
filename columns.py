import pygame
from settings import Settings
import game_logic as gl
from pygame.sprite import Group

# Initializes variables used in running the game.
pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
pygame.display.set_caption("Columns")
lose = False
column = Group()
board = [[0] * 6 for i in xrange(12)]
gl.create_column(settings,screen,column)
score = [0]

# Runs the game while the user hasn't lost.
while not lose:
    if gl.check_events(column,board):
        run_game()
    gl.update_screen(settings,screen,column,board,score)
    gl.update_column(settings,screen,column,board,score)
    lose = gl.check_state(board,screen)

# Displays the end screen until the user closes the program.
while True:
    gl.check_events(column,board)
    gl.lose_screen(settings,screen)
