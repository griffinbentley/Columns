import pygame
from settings import Settings
import game_logic as gl
from pygame.sprite import Group

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Columns")

    lose = False

    column = Group()

    board = Group()

    gl.create_column(settings,screen,column)

    while not lose:
        if gl.check_events(column,board):
            run_game()
        gl.update_screen(settings,screen,column,board)
        gl.update_column(settings,screen,column,board)
        lose = gl.check_state(board,screen)

    if lose:
        while True:
            if gl.check_events(column,board):
                run_game()
            gl.lose_screen(settings,screen)

run_game()