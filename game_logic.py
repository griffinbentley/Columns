import pygame
import random
from block import Block

# Checks to see if there were any button events.
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

# Checks to see if any buttons were pressed.
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

# Checks to see if any buttons were released.
def check_keyup_events(event,column):
    if event.key == pygame.K_DOWN:
        for block in column:
            block.slow_down()

# Alternates the order of the blocks in the given column, moving them from bottom to top.
def swap(column):
    lowest = column.sprites()[0]
    for block in column:
        if block.rect.y > lowest.rect.y:
            lowest = block
    lowest.y -= 2*lowest.width
    lowest.rect.y = lowest.y
    for block in column:
        if block != lowest:
            block.y += lowest.width
            block.rect.y = block.y

# Creates a column and populates it with 3 blocks.
def create_column(settings,screen,column):
    x = random.randint(0,5)*settings.block_width
    for y in range(0,3):
        create_block(settings,screen,column,y,x)

# Creates a block and adds it to the given column.
def create_block(settings,screen,column,y,x):
    block = Block(settings,screen)
    block_width = block.rect.width
    block.x = x+screen.get_rect().centerx-settings.block_width*3
    block.rect.x = block.x
    block.y = y*block_width-3*block_width+screen.get_rect().centery-settings.block_width*6-screen.get_rect().top
    block.rect.y = block.y
    column.add(block)

# Adds the given column to the board and checks matches.
def add_to_board(column,board,score):
    for block in column:
        block.board_x = (block.rect.x - 255) / 40
        block.board_y = (block.rect.y * 11 - 1485) / 440
        board[block.board_y][block.board_x] = block
    for block in column:
        check_matches(block, board, score)
    column.empty()

# Checks to see if the given block has any matches in its vicinity.
def check_matches(block, board, score):
    to_remove = [[]]
    x = block.board_x
    y = block.board_y

    # Checks horizontally.
    h_remove = [block]
    if x >= 1 and isinstance(board[y][x - 1], Block):
        if board[y][x - 1].color == block.color:
            h_remove.append(board[y][x - 1])
            if x >= 2 and isinstance(board[y][x - 2], Block):
                if board[y][x - 2].color == block.color:
                    h_remove.append(board[y][x - 2])
    if x <= 4 and isinstance(board[y][x + 1], Block):
        if board[y][x + 1].color == block.color:
            h_remove.append(board[y][x + 1])
            if x <= 3 and isinstance(board[y][x + 2], Block):
                if board[y][x + 2].color == block.color:
                    h_remove.append(board[y][x + 2])
    if len(h_remove) >= 3:
        to_remove.append(h_remove)

    # Checks vertically.
    v_remove = [block]
    if y >= 1 and isinstance(board[y - 1][x], Block):
        if board[y - 1][x].color == block.color:
            v_remove.append(board[y - 1][x])
            if y >= 2 and isinstance(board[y - 2][x], Block):
                if board[y - 2][x].color == block.color:
                    v_remove.append(board[y - 2][x])
    if y <= 10 and isinstance(board[y + 1][x], Block):
        if board[y + 1][x].color == block.color:
            v_remove.append(board[y + 1][x])
            if y <= 9 and isinstance(board[y + 2][x], Block):
                if board[y + 2][x].color == block.color:
                    v_remove.append(board[y + 2][x])
    if len(v_remove) >= 3:
        to_remove.append(v_remove)

    # Checks angle top left to bottom right.
    ua_remove = [block]
    if x >= 1 and y >= 1 and isinstance(board[y - 1][x - 1], Block):
        if board[y - 1][x - 1].color == block.color:
            ua_remove.append(board[y - 1][x - 1])
            if x >= 2 and y >= 2 and isinstance(board[y - 2][x - 2], Block):
                if board[y - 2][x - 2].color == block.color:
                    ua_remove.append(board[y - 2][x - 2])
    if x <= 4 and y <= 10 and isinstance(board[y + 1][x + 1], Block):
        if board[y + 1][x + 1].color == block.color:
            ua_remove.append(board[y + 1][x + 1])
            if x <= 3 and y <= 9 and isinstance(board[y + 2][x + 2], Block):
                if board[y + 2][x + 2].color == block.color:
                    ua_remove.append(board[y + 2][x + 2])
    if len(ua_remove) >= 3:
        to_remove.append(ua_remove)

    # Checks angle bottom left to top right.
    da_remove = [block]
    if x >= 1 and y <= 10 and isinstance(board[y + 1][x - 1], Block):
        if board[y + 1][x - 1].color == block.color:
            da_remove.append(board[y + 1][x - 1])
            if x >= 2 and y <= 9 and isinstance(board[y +2][x - 2], Block):
                if board[y + 2][x - 2].color == block.color:
                    da_remove.append(board[y +2][x - 2])
    if x <= 4 and y >= 1 and isinstance(board[y - 1][x + 1], Block):
        if board[y - 1][x + 1].color == block.color:
            da_remove.append(board[y - 1][x + 1])
            if x <= 3 and y >= 2 and isinstance(board[y - 2][x + 2], Block):
                if board[y - 2][x + 2].color == block.color:
                    da_remove.append(board[y - 2][x + 2])
    if len(da_remove) >= 3:
        to_remove.append(da_remove)

    # Stores columns that need to be moved down after removal.
    cols = set()

    # Removes appropriate blocks from the board.
    num_remove = 0
    for remove in to_remove:
        for block in remove:
            num_remove += 1
            board[block.board_y][block.board_x] = 0
            cols.add(block.board_x)

    # Moves down columns where blocks were removed.
    for column in cols:
        move_down(column, board, score)

    # Adds to score based on the number of blocks removed.
    if num_remove >= 5:
        score[0] += num_remove * 1500
    elif num_remove == 4:
        score[0] += num_remove * 1000
    elif num_remove == 3:
        score[0] += num_remove * 500

# Moves down all blocks with no blocks under them in the given column.
def move_down(x, board, score):
    blocks = set()
    y = 10
    while y != -1:
        if y != 11 and board[y][x] != 0 and board[y + 1][x] == 0:
            blocks.add(board[y][x])
            board[y][x].rect.y += board[y][x].width
            board[y][x].y = board[y][x].rect.y
            board[y][x].board_y += 1
            board[y + 1][x] = board[y][x]
            board[y][x] = 0
            y += 1
        else:
            y -= 1
    for block in blocks:
        check_matches(block, board, score)

# Moves the columns down the screen.
def update_column(settings,screen,column,board,score):
    lowest = column.sprites()[0]
    for block in column:
        if block.rect.y > lowest.rect.y:
            lowest = block
    if pygame.time.get_ticks() - column.sprites()[0].last >= column.sprites()[0].tick_length:
        if lowest.check_bottom(board):
            column.update()
        else:
            add_to_board(column,board,score)
            create_column(settings,screen,column)

# Checks all blocks to see if one has been placed on top of the playfield and if so
# returns true.
def check_state(board,screen):
    for col in board:
        for block in col:
            if isinstance(block, Block):
                if block.rect.bottom == screen.get_rect().centery-block.width*6:
                    return True
    return False

# Draws the grid of the gameboard.
def draw_grid(screen,settings):
    leftx = screen.get_rect().centerx-settings.block_width*3
    rightx = leftx + settings.block_width*6
    topy = screen.get_rect().centery - settings.block_width*6
    bottomy = topy + settings.block_width*12
    for x in range(0,13):
        pygame.draw.line(screen,(160,160,160),(leftx,topy+x*settings.block_width),(rightx,topy+x*settings.block_width),5)
    for x in range(0,7):
        pygame.draw.line(screen,(160,160,160),(leftx+x*settings.block_width,topy),(leftx+x*settings.block_width,bottomy),5)

# Displays "YOU LOSE" text at the end of the game.
def lose_screen(settings,screen):
    font = pygame.font.Font(None, 100)
    text = font.render('YOU LOSE', True, (0,0,0))
    screen.blit(text, (settings.screen_width/2-text.get_rect().centerx,settings.screen_height/2-text.get_rect().centery))
    pygame.display.flip()

# Displays the player's score at the top of the window.
def update_score(settings,screen,score):
    font = pygame.font.Font(None, 50)
    text = font.render('SCORE: ' + str(score[0]), True, (0,0,0))
    screen.blit(text, (settings.screen_width/2-text.get_rect().centerx, 0))
    pygame.display.flip()

# Draws in the gameboard.
def update_screen(settings,screen,column,board,score):
    screen.fill(settings.screen_color)

    for block in column:
        if not block.y < screen.get_rect().centery-settings.block_width*6-screen.get_rect().top:
            block.draw_block()

    for col in board:
        for block in col:
            if isinstance(block, Block):
                block.draw_block()

    draw_grid(screen,settings)
    update_score(settings,screen,score)

    pygame.display.flip()
