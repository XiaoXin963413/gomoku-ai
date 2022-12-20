import random, asyncio
import numpy as np
    

class BaseBoard():
    def set_board(self, board):
        self.__board = board
        self.__col = len(board)
        self.__row = len(board)

    def __check_straight_line(self, val, list, num):
        if (list == []): 
            return False
        if 0 not in list:
            return False
        if (list.count(val) == num and list.count(0) == 1):
            return True;
        return False;
        
    def __check_all_list(self, val, list):
        if (list == []): 
            return False
        return all(x == val and x is not True for x in list)

    def __check_upper_right(self, position, len):
        x, y = position[0], position[1]
        if (x+5 >= self.__col or y+5 >= self.__row):
            return False
        list = []
        j = 0
        for i in range(len):
            list.append(self.__board[x+j][y+i])
            j = j - 1
        return self.__check_all_list(self.__board[x][y], list)

    def __check_bottom_right(self, position, len):
        x, y = position[0], position[1]
        if (x+5 >= self.__col or y+5 >= self.__row):
            return False
        list = []
        j = 0
        for i in range(len):
            list.append(self.__board[x+i][y+j])
            j = j + 1
        return self.__check_all_list(self.__board[x][y], list)

    def check_five(self):
        for x in range(self.__col):
            for y in range(self.__row):
                if self.__board[x][y] == 0:
                    continue
                if self.__check_all_list(self.__board[x][y], self.__board[x][y:y+5:1]):
                    return True
                if self.__check_all_list(self.__board[x][y], [i[y] for i in self.__board[5:5+5:1]]):
                    return True
                if self.__check_bottom_right([x, y], 5):
                    return True
                if self.__check_upper_right([x, y], 5):
                    return True
        return False

    def check_check(self):
        for x in range(self.__col):
            for y in range(self.__row):
                if self.__board[x][y] == 0:
                    continue
                if self.__check_straight_line(self.__board[x][y], self.__board[x][y:y+5:1], 4):
                    return True
                if self.__check_straight_line(self.__board[x][y], [i[y] for i in self.__board[5:5+5:1]], 4):
                    return True
                # if self.__check_bottom_right([x, y], 5):
                #     return True
                # if self.__check_upper_right([x, y], 5):
                #     return True  
        return False

class gomokuAI(BaseBoard):
    def Next_step(self):
        if self.check_five():
            return "Five chess line."
        if self.check_check():
            return "Check!"