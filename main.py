import numpy as np


class Game:
    def __init__(self):
        self.board = np.array([0, 0, 0, 0, 0])
        self.balance = 700
        self.bet = 5
        self.values = np.array([2, 3, 4, 5, 10, 15, 15])
        self.symbols = ['10', 'J', 'Q', 'A', 'S', 'R', 'W']

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
        value = 15
        for element in line:
            if element != 6:
                line = np.where(line==6, element, line)
                value = self.values[element]
                break
        for i in range(4):
            if line[i] == line[i+1]:
                win += 1
            else:
                break
        if win > 0:
            print('value', value)
            print('win', value*win)

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
