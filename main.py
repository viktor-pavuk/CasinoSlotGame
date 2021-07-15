import numpy as np


class Game:
    def __init__(self):
        self.board = np.array([0, 0, 0, 0, 0])
        self.balance = 700
        self.bet = 5
        self.values = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                                [100, 40, 30, 20, 20, 10, 10, 5, 5, 5],
                                [300, 200, 150, 100, 75, 50, 40, 30, 25, 20],
                                [500, 400, 300, 250, 200, 160, 140, 120, 110, 100]])
        self.symbols = ['W', 'P', 'D', 'Z', 'M', 'A', 'K', 'Q', 'J', '1']

    def gen_board(self):
        self.board = np.random.randint(0,6,(3,5))

    def print_board(self):
        new_board = []
        for line in self.board:
            new_line = []
            for element in line:
                new_line.append(self.symbols[element])
            new_board.append(new_line)
        print(np.array(new_board))

    def print_balance(self):
        print(self.balance)

    def check_lines(self, line):
        win = 0
        value = 0
        for element in line:
            if element != 0:
                line = np.where(line==0, element, line)
                value = element
                break
        for i in range(4):
            if line[i] == line[i+1]:
                win += 1
            else:
                break
        if self.values[win][value] > 0:
            print('value', self.symbols[value])
            print('win', self.values[win][value])

    def spin(self):
        self.gen_board()
        self.print_board()
        for i in range(3):
            self.check_lines(self.board[i])


if __name__ == "__main__":
    g = Game()
    endgame = ''
    while endgame != 'q':
        g.spin()
        endgame = input('Enter q to exit:')
