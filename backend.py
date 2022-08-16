class TicTocToe:

    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        board_row = 3
        for i in range(0, board_row):
            row = list(['-', '-', '-'])
            self.board.append(row)

    def perform_player_choice(self, row, column, sign):
        self.board[row - 1][column - 1] = sign

    def is_won(self):
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][2] != '-':
            return True
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][2] != '-':
            return True
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][2] != '-':
            return True
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[2][0] != '-':
            return True
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[2][1] != '-':
            return True
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[2][2] != '-':
            return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != '-':
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != '-':
            return True
        return False

    def is_allowed_to_choose(self, row, column):
        if self.board[row - 1][column - 1] == '-':
            return True
        return False

    def clear(self):
        self.board = []
        board_row = 3
        for i in range(0, board_row):
            row = list(['-', '-', '-'])
            self.board.append(row)


game = TicTocToe()
