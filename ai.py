import copy
import random


class Minimax_AI:
    """Artificial Intelligence based in Minimax and alpha-beta-prunning.

    It has the next instances variables:
        * depth -> how many moves ahead the AI will search
        * player -> the role of AI (player 1 or player 2)
        * opponent - > the role of opponent (player 1 or player 2)
        * board_rows -> number of rows in board
        * board_columns -> number of columns in board

    It has the next public methods:
        * make_move(board) -> makes a move in game for board position

    It has the next private methods for functioning
        * _to_move(board) -> returns which player to move in board position
        * _actions(board) -> returns a list with all possible actions in board
        * _result(board, action) -> returns board state after action in board
        * _is_endgame(board) -> returns True if board is in a end of game position
        * _utility(board, piece) -> returns the numerical value of a board position
        * _minimax(board, current_depth, max_turn, alpha, beta, node)
    """

    def __init__(self, depth, player, rows, columns):
        """Create AI instance with depth and player variables."""
        self._depth = depth
        self._player = player
        self._board_rows = rows
        self._board_columns = columns
        if self._player == 1:
            self._opponent = 2
        else:
            self._opponent = 1

    @property
    def depth(self):
        return self._depth

    @property
    def player(self):
        return self._player

    @property
    def board_rows(self):
        return self._board_rows

    @property
    def board_columns(self):
        return self._board_columns

    @property
    def opponent(self):
        return self._opponent

    def make_move(self, board):
        """Returns the number of the optimal column to insert a piece by using minimax."""
        value, col = self._minimax(
            board, 0, True, float('-inf'), float('inf'), 0)
        return col

    def _to_move(self, board_status):
        """returns which player to move in board position."""
        player1_pieces = 0
        player2_pieces = 0
        for row in board_status:
            for col in row:
                if col == 1:
                    player1_pieces += 1
                elif col == 2:
                    player2_pieces += 1
        return 1 if player1_pieces == player2_pieces else 2

    def _actions(self, board_status):
        """returns a list with the numbers of the columns that have space for
        a new piece.
        The columns start at 0"""
        actions = []
        for col in range(0, self._board_columns):
            if board_status[self._board_rows-1][col] == 0:
                actions.append(col)
        return actions

    def _result(self, board_status, action, piece):
        """returns board state after action in board.
        action = number of column
        piece = number of player's turn (1, 2)"""
        new_board = copy.deepcopy(board_status)
        col = action
        for r in range(self._board_rows):
            if new_board[r][col] == 0:
                row = r
                break
        new_board[row][col] = piece
        return new_board

    def _is_endgame(self, board_status, player):
        """Returns True if board is in a winning position for player."""
        # Check horizontal locations for win
        for c in range(self._board_columns-3):
            for r in range(self._board_rows):
                if board_status[r][c] == player and board_status[r][c+1] == player and board_status[r][c+2] == player and board_status[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(self._board_columns):
            for r in range(self._board_rows-3):
                if board_status[r][c] == player and board_status[r+1][c] == player and board_status[r+2][c] == player and board_status[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(self._board_columns-3):
            for r in range(self._board_rows-3):
                if board_status[r][c] == player and board_status[r+1][c+1] == player and board_status[r+2][c+2] == player and board_status[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(self._board_columns-3):
            for r in range(3, self._board_rows):
                if board_status[r][c] == player and board_status[r-1][c+1] == player and board_status[r-2][c+2] == player and board_status[r-3][c+3] == player:
                    return True

    def _is_tie(self, board):
        """Returns True if the board position is a tie."""
        if not self._is_endgame(board, self._player) and not self._is_endgame(board, self._opponent):
            for row in board:
                for col in row:
                    if col == 0:
                        return
            return True

    def _utility(self, board_status):
        """Assign a numerical value to a board position based on player
        and oponent pieces.
        A winning position for player = 100
        A lossing position for player = -100
        A tie = 0

        For a non final position the value consist on:
        - given the importance of the center column each piece
            in this column adds a value of 3
        - every two consecutive pieces with the opportunity to be four
            add a value of 2
        - every three consecutive pieces with the opportunity to be four
            add a value of 3

        For opponent pieces the values are the same but negative.

        For looking consecutive pieces we create windows of lenght 4.
        """
        window_len = 4
        center_pieces_value = 3
        player_two_pieces_value = 2
        opponent_two_pieces_value = 2
        player_three_pieces_value = 5
        opponent_three_pieces_value = 5
        value = 0
        if self._is_tie(board_status):
            return value
        if self._is_endgame(board_status, self._player):
            value = 1000
            return value
        if self._is_endgame(board_status, self._opponent):
            value = -1000
            return value

        # non final position

        # check center column for player pieces
        center_column = [int(i) for i in list(
            board_status[:, self._board_columns//2])]
        center_count = center_column.count(self._player)
        value += center_count * center_pieces_value

        # check center column for opponent pieces
        center_column = [int(i) for i in list(
            board_status[:, self._board_columns//2])]
        center_count = center_column.count(self._opponent)
        value -= center_count * center_pieces_value

        # check horizontal consecutive pieces
        for r in range(self._board_rows):
            row_array = [int(i) for i in list(board_status[r, :])]
            for c in range(self._board_columns-3):
                window = row_array[c:c+window_len]
                # add player values
                if window.count(self._player) == 3 and window.count(0) == 1:
                    value += player_three_pieces_value
                elif window.count(self._player) == 2 and window.count(0) == 2:
                    value += player_two_pieces_value
                # subtract opponent values
                elif window.count(self._opponent) == 3 and window.count(0) == 1:
                    value -= opponent_three_pieces_value
                elif window.count(self._opponent) == 2 and window.count(0) == 2:
                    value -= opponent_two_pieces_value

        # check vertical consecutive pieces
        for c in range(self._board_columns):
            col_array = [int(i) for i in list(board_status[:, c])]
            for r in range(self._board_rows-3):
                window = col_array[r:r+window_len]
                # add player values
                if window.count(self._player) == 3 and window.count(0) == 1:
                    value += player_three_pieces_value
                elif window.count(self._player) == 2 and window.count(0) == 2:
                    value += player_two_pieces_value
                # subtract opponent values
                elif window.count(self._opponent) == 3 and window.count(0) == 1:
                    value -= opponent_three_pieces_value
                elif window.count(self._opponent) == 2 and window.count(0) == 2:
                    value -= opponent_two_pieces_value

        # check positive sloped diagonal
        for r in range(self._board_rows-3):
            for c in range(self._board_columns-3):
                window = [board_status[r+i][c+i] for i in range(window_len)]
                # add player values
                if window.count(self._player) == 3 and window.count(0) == 1:
                    value += player_three_pieces_value
                elif window.count(self._player) == 2 and window.count(0) == 2:
                    value += player_two_pieces_value
                # subtract opponent values
                elif window.count(self._opponent) == 3 and window.count(0) == 1:
                    value -= opponent_three_pieces_value
                elif window.count(self._opponent) == 2 and window.count(0) == 2:
                    value -= opponent_two_pieces_value

        # check negative sloped diagonal
        for r in range(self._board_rows-3):
            for c in range(self._board_columns-3):
                window = [board_status[r+3-i][c+i] for i in range(window_len)]
                # add player values
                if window.count(self._player) == 3 and window.count(0) == 1:
                    value += player_three_pieces_value
                elif window.count(self._player) == 2 and window.count(0) == 2:
                    value += player_two_pieces_value
                # subtract opponent values
                elif window.count(self._opponent) == 3 and window.count(0) == 1:
                    value -= opponent_three_pieces_value
                elif window.count(self._opponent) == 2 and window.count(0) == 2:
                    value -= opponent_two_pieces_value

        # return value
        return value

    def _minimax(self, board, current_depth, max_turn, alpha, beta, node):
        """Returns the score of the optimal column and the number of the column."""
        if current_depth == self._depth or self._is_endgame(board, self._player) or self._is_endgame(board, self._opponent) or self._is_tie(board):
            return self._utility(board), None

        node += 1

        list_of_actions = self._actions(board)
        random.shuffle(list_of_actions)

        best_value = float('-inf') if max_turn else float('inf')
        action_target = None

        if max_turn:
            for action in list_of_actions:
                new_board = self._result(board, action, self._player)
                value_child, col_child = self._minimax(
                    new_board, current_depth+1, not max_turn, alpha, beta, node)

                if best_value < value_child:
                    best_value = value_child
                    action_target = action
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break

        else:
            for action in list_of_actions:
                new_board = self._result(board, action, self._opponent)
                value_child, col_child = self._minimax(
                    new_board, current_depth+1, not max_turn, alpha, beta, node)

                if best_value > value_child:
                    best_value = value_child
                    action_target = action
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break

        return best_value, action_target
