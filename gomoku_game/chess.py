import random
import numpy as np

class GomokuGame():
    def __init__(self):
        self.__chess_row = 19
        self.__chess_col = 19
        self.__chessboard = [[0]*self.__chess_row]*self.__chess_col

    def get_chessboard(self):
        return self.__chessboard

    def randon_chessborad(self):
        for i in range(0, len(self.__chessboard)):
            temp = np.random.randint(3, size=19)
            temp = temp.tolist()
            self.__chessboard[i] = temp