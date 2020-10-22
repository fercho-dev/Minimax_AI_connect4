import numpy as np
import pygame
import sys
import math
from board import Board


# function to draw the board in pygame
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, colors["blue"], (c*SQUARESIZE, r *
                                                      SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, colors["black"], (int(
                c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, colors["red"], (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, colors["yellow"], (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


if __name__ == '__main__':
    # colors for game
    colors = {"blue": (0, 0, 255),
              "black": (0, 0, 0),
              "red": (255, 0, 0),
              "yellow": (255, 255, 0)}

    # size of board
    ROW_COUNT = 6
    COLUMN_COUNT = 7

    # create board
    board = Board(ROW_COUNT, COLUMN_COUNT)

    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board.status)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(
                    screen, colors["black"], (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(
                        screen, colors["red"], (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(
                        screen, colors["yellow"], (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(
                    screen, colors["black"], (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if board.is_valid_location(col):
                        row = board.get_next_open_row(col)
                        board.insert_piece(row, col, 1)

                        if board.is_winning_position(1):
                            label = myfont.render(
                                "Player 1 wins!!", 1, colors["red"])
                            screen.blit(label, (40, 10))
                            game_over = True

                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if board.is_valid_location(col):
                        row = board.get_next_open_row(col)
                        board.insert_piece(row, col, 2)

                        if board.is_winning_position(2):
                            label = myfont.render(
                                "Player 2 wins!!", 1, colors["red"])
                            screen.blit(label, (40, 10))
                            game_over = True

                draw_board(board.status)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)
