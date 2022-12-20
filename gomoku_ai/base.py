import random
import asyncio
import numpy as np


class BaseBoard():
    def set_board(self, board):
        self.__board = board
        self.__col = len(board)
        self.__row = len(board)

    def __get_upper_left(self, position, num):
        x, y = position[0], position[1]
        if (x - num) > self.__col or (y + num) > self.__row:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(self.__board[x+i][y+j])
            i, j = i - 1, j + 1
        return list

    def __get_bottom_left(self, position, num):
        x, y = position[0], position[1]
        if (x + num) > self.__col or (y + num) > self.__row:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(self.__board[x+i][y+j])
            i, j = i + 1, j + 1
        return list

    def __check_straight_line(self, val, list, num):
        if (list == []):
            return False
        if 0 not in list:
            return False
        if (list.count(val) == num and list.count(0) == 1):
            return True
        return False

    def __check_all_list(self, val, list):
        if (list == []):
            return False
        return all(x == val and x is not True for x in list)

    def check_five(self):
        for x in range(self.__col):
            for y in range(self.__row):
                if self.__board[x][y] == 0:
                    continue
                # check left
                if (self.__check_all_list(self.__board[x][y], self.__board[x][y:y+5:1])
                        and y + 5 <= self.__row):
                    return True
                # check bottom 
                if (self.__check_all_list(self.__board[x][y], [i[y] for i in self.__board[5:5+5:1]])
                        and x + 5 <= self.__col):
                    return True
                if (self.__check_all_list(self.__board[x][y], self.__get_upper_left([x, y], 5))
                        and x - 5 <= self.__col):
                    return True
                if (self.__check_all_list(self.__board[x][y], self.__get_bottom_left([x, y], 5))
                        and x + 5 <= self.__col):
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
