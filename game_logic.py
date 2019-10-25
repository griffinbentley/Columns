import pygame
import random
from block import Block
from pygame.sprite import Group

def check_events(column,board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if check_keydown_events(event,column,board):
                return True
        if event.type == pygame.KEYUP:
            check_keyup_events(event,column)

def check_keydown_events(event,column,board):
    if event.key == pygame.K_RIGHT:
        for n in range(2,-1,-1):
            x = column.sprites()[n].rect.centerx
            if column.sprites()[n].move_right(x,board):
                pass
            else:
                break
    elif event.key == pygame.K_LEFT:
        for n in range(2,-1,-1):
            x = column.sprites()[n].rect.centerx
            if column.sprites()[n].move_left(x,board):
                pass
            else:
                break
    elif event.key == pygame.K_DOWN:
        for block in column:
            block.speed_up()
    elif event.key == pygame.K_q:
        pygame.quit()
        quit()
    elif event.key == pygame.K_r:
        return True
    elif event.key == pygame.K_SPACE:
        swap(column)

def check_keyup_events(event,column):
    if event.key == pygame.K_DOWN:
        for block in column:
            block.slow_down()

def swap(column):
    lowest = column.sprites()[0]
    for block in column:
        if block.rect.y > lowest.rect.y:
            lowest = block
    lowest.y -= 2*lowest.width
    lowest.rect.y = lowest.y
    for block in column:
        if block != highest:
            block.y += highest.width
            block.rect.y = block.y

def create_column(settings,screen,column):
    x = random.randint(0,5)*settings.block_width
    for y in range(0,3):
        create_block(settings,screen,column,y,x)

def create_block(settings,screen,column,y,x):
    block = Block(settings,screen)
    block_width = block.rect.width
    block.x = x+screen.get_rect().centerx-settings.block_width*3
    block.rect.x = block.x
    block.y = y*block_width-3*block_width+screen.get_rect().centery-settings.block_width*6-screen.get_rect().top
    block.rect.y = block.y
    column.add(block)

def add_to_board(column,board):
    for block in column:
        board.add(block)
        check_matches(board, block)
    column.empty()

def check_matches(board, block):
    

def update_column(settings,screen,column,board):
    lowest = column.sprites()[0]
    for block in column:
        if block.rect.y > lowest.rect.y:
            lowest = block
    if pygame.time.get_ticks() - column.sprites()[0].last >= column.sprites()[0].tick_length:
        if lowest.check_bottom(board):
            column.update()
        else:
            add_to_board(column,board)
            create_column(settings,screen,column)

def check_state(board,screen):
    for block in board:
        if block.rect.bottom == screen.get_rect().centery-block.width*6:
            return True
    return False

def draw_grid(screen,settings):
    leftx = screen.get_rect().centerx-settings.block_width*3
    rightx = leftx + settings.block_width*6
    topy = screen.get_rect().centery - settings.block_width*6
    bottomy = topy + settings.block_width*12
    for x in range(0,13):
        pygame.draw.line(screen,(160,160,160),(leftx,topy+x*settings.block_width),(rightx,topy+x*settings.block_width),5)
    for x in range(0,7):
        pygame.draw.line(screen,(160,160,160),(leftx+x*settings.block_width,topy),(leftx+x*settings.block_width,bottomy),5)

def lose_screen(settings,screen):
    font = pygame.font.Font(None, 100)
    text = font.render('YOU LOSE', True, (0,0,0))
    screen.blit(text, (settings.screen_width/2-text.get_rect().centerx,settings.screen_height/2-text.get_rect().centery))
    pygame.display.flip()

def update_screen(settings,screen,column,board):
    screen.fill(settings.screen_color)

    for block in column:
        if not block.y < screen.get_rect().centery-settings.block_width*6-screen.get_rect().top:
            block.draw_block()

    for block in board:
        block.draw_block()

    draw_grid(screen,settings)

    pygame.display.flip()
