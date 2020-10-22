import numpy as np


class Board:
    """Class for connect4 board game.
    It has the next instances variables:
        * status -> a numpy matriz with current board status
        * rows -> number of rows in the board
        * columns -> number of columns in the board

        Once initialized rows and columns can't be changed but status
        can be set to any matriz -as long as the shape remains the same- 
        at any moment with the syntax:
            Board.status = matriz

    It has the next public methods:
        * .print_status() -> prints the board
        * .insert_piece(row, col, piece) -> puts a piece in the board
        * .is_winning_position(player) -> returns True if the move makes the player win
        * .is_valid_location(col) -> Returns True if there is space for a new piece
        * .get_next_open_row(col) -> Returns the available row for a new piece
    """

    def __init__(self, ROW_COUNT, COLUMN_COUNT):
        """initialize and empty board (a matriz of zeros).
        Receives the number of rows and columns."""
        self._status = np.zeros((ROW_COUNT, COLUMN_COUNT))
        self._rows = ROW_COUNT
        self._columns = COLUMN_COUNT

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def print_status(self):
        print(np.flip(self._status, 0))

    def is_valid_location(self, col):
        """Checks if a column still have empty space.
        Returns True if there is space for a new piece."""
        return self._status[self._rows-1][col] == 0

    def get_next_open_row(self, col):
        """Returns the available row for a new piece."""
        for r in range(self._rows):
            if self.status[r][col] == 0:
                return r

    def insert_piece(self, row, col, piece):
        """Sets a new piece in the board"""
        self._status[row][col] = piece

    def is_winning_position(self, player):
        """Returns True if player wins in this board position"""
        # Check horizontal locations for win
        for c in range(self._columns-3):
            for r in range(self._rows):
                if self._status[r][c] == player and self._status[r][c+1] == player and self._status[r][c+2] == player and self._status[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(self._columns):
            for r in range(self._rows-3):
                if self._status[r][c] == player and self._status[r+1][c] == player and self._status[r+2][c] == player and self._status[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(self._columns-3):
            for r in range(self._rows-3):
                if self._status[r][c] == player and self._status[r+1][c+1] == player and self._status[r+2][c+2] == player and self._status[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(self._columns-3):
            for r in range(3, self._rows):
                if self._status[r][c] == player and self._status[r-1][c+1] == player and self._status[r-2][c+2] == player and self._status[r-3][c+3] == player:
                    return True
