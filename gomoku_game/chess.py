import random
import numpy as np
import gomoku_ai.base as base


class GomokuGame(base.BaseBoard):
    def __init__(self, size):
        super().__init__()
        self._BOARD_SIZE = size
        self.__board = [[0 for _ in range(self._BOARD_SIZE)] for _ in range(self._BOARD_SIZE)]

    def Check_win(self, borad):
        for x in range(len(borad)):
            for y in range(len(borad)):
                if (borad[x][y] == 0):
                    continue
                if self._check_connected(borad, [x, y], 5):
                    self.__print_winner(borad[x][y])
                    return True
        return False

    def __print_winner(self, var):
        if var == 1:
            print('You win!')
        else:
            print('Com Win!')

    def get_board(self):
        return self.__board

    def set_board(self, x, y):
        self.__board[x][y] = 1

    def set_board_com(self, x, y):
        self.__board[x][y] = 2

    def randon_chessborad(self):
        for i in range(0, len(self.__board)):
            temp = np.random.randint(3, size=19)
            temp = temp.tolist()
            self.__board[i] = temp

    def __clear_board(self):
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                self.__board[i][j] = 0

    def Continue(self):
        while True:
            again = input('Do you want to again? Input Y or Ctrl+C exit!')
            if (again == 'Y'):
                self.__clear_board()
                return True