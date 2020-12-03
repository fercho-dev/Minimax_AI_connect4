from ai import Minimax_AI
from board import Board
import numpy
import pickle

# one dict for each player
first5moves1 = {}
first5moves2 = {}

# size of board
ROW_COUNT = 6
COLUMN_COUNT = 7

# players
ai_players = [1, 2]

# iterate for both players
for ai_player in ai_players:
    if ai_player == 1:
        opp_player = 2
    else:
        opp_player = 1
    # create board
    board = Board(ROW_COUNT, COLUMN_COUNT)
    # initialize AI
    ai_depth = 6
    ai = Minimax_AI(ai_depth, ai_player, ROW_COUNT, COLUMN_COUNT)

    if ai_player == 1:
        col = ai.make_move(board.status)
        # add info to dict
        board_str = ''
        for r in board.status:
            for c in r:
                board_str = board_str + str(c)
        first5moves1[board_str] = col

        row = board.get_next_open_row(col)
        board.insert_piece(row, col, ai_player)

    # at least tens pieces need to be move
    board_tmp0 = board.status
    # check all possibilities 7 columns
    for column in range(COLUMN_COUNT):
        board.status = board_tmp0
        row = board.get_next_open_row(column)
        board.insert_piece(row, column, opp_player)
        col = ai.make_move(board.status)
        # add info to dict
        board_str = ''
        for r in board.status:
            for c in r:
                board_str = board_str + str(c)
        if ai_player == 1:
            first5moves1[board_str] = col
        else:
            first5moves2[board_str] = col


with open('firstmove1', 'wb') as file:
    pickle.dump(first5moves1, file)

with open('firstmove2', 'wb') as file:
    pickle.dump(first5moves2, file)
