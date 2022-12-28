import random
import numpy as np
import gomoku_ai.base as base


class GomokuGame(base.BaseBoard):
    def __init__(self, row, col):
        self._BOARD_SIZE = row
        self.__chessboard = [[0 for _ in range(self._BOARD_SIZE)] for _ in range(self._BOARD_SIZE)]

    def check_win(self, board):
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if self._check_connected(board, x, y, 5):
                    return board[x][y]
        return False

    def get_chessboard(self):
        return self.__chessboard

    def set_chessboard(self, x, y):
        self.__chessboard[x][y] = 1

    def set_chessboard_com(self, x, y):
        self.__chessboard[x][y] = 2

    def randon_chessborad(self):
        for i in range(0, len(self.__chessboard)):
            temp = np.random.randint(3, size=19)
            temp = temp.tolist()
            self.__chessboard[i] = temp
