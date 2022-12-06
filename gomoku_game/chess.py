import random
import numpy as np


class GomokuGame():
    def __init__(self, row, col):
        self.__chess_row = row
        self.__chess_col = col
        self.__chessboard = [[0 for _ in range(row)] for _ in range(col)]

    def get_chessboard(self):
        return self.__chessboard

    def set_chessboard(self, x, y):
        self.__chessboard[x][y] = 1

    def randon_chessborad(self):
        for i in range(0, len(self.__chessboard)):
            temp = np.random.randint(3, size=19)
            temp = temp.tolist()
            self.__chessboard[i] = temp

    def check_five(self):
        for y in range(self.__chess_col):
            for x in range(self.__chess_row):
                if self.__chessboard[y][x] == 0:
                    continue
                if all(i == self.__chessboard[y][x] for i in self.__chessboard[y][x:x+5:1]):
                    return True
                if all(i == self.__chessboard[y][x] for i in self.__chessboard[y][x:x-5:-1]):
                    return True
                if all(i == self.__chessboard[y][x] for i in self.__chessboard[y:y+5:1][x:x+5:1]):
                    return True
                if all(i == self.__chessboard[y][x] for i in self.__chessboard[y:y-5:-1][x:x-5:-1]):
                    return True

        return False
