import random
import asyncio
import numpy as np


class BaseBoard():
    def set_board(self, board):
        self._board = board
        self.__col = len(board)
        self.__row = len(board)

    def _get_boardsize(self):
        return len(self._board)

    def __get_left(self, position, num):
        x, y = position[0], position[1]
        return self._board[x][y:y+num:1]

    def __get_upper_left(self, position, num):
        x, y = position[0], position[1]
        if (x - num) > self.__col or (y + num) > self.__row:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(self._board[x+i][y+j])
            i, j = i - 1, j + 1
        return list

    def __get_bottom_left(self, position, num):
        x, y = position[0], position[1]
        if (x + num) > self.__col or (y + num) > self.__row:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(self._board[x+i][y+j])
            i, j = i + 1, j + 1
        return list

    def __check_line(self, position, list, num):
        # print(list)
        x, y = position[0], position[1]
        var = self._board[x][y]
        if (list == []):
            return False
        if (list.count(var) != num):
            return False
        if (list.count(0) == 1):
            return list.index(0)
        return False

    def __get_connect_point(self, list):
        return list.index(0)

    def __check_all_list(self, var, list):
        if (list == []):
            return False
        return all(x == var and x is not True for x in list)

    # 檢查是否有五子連線
    def check_five(self, x, y):
        if self._board[x][y] == 0:
            return False
        # check left
        if (self.__check_all_list(self._board[x][y], self.__get_left([x, y], 5))
                and y + 5 <= self.__row):
            return True
        # check bottom
        if (self.__check_all_list(self._board[x][y], [i[y] for i in self._board[5:y+5:1]])
                and x + 5 <= self.__col):
            return True
        if (self.__check_all_list(self._board[x][y], self.__get_upper_left([x, y], 5))
                and x - 5 <= self.__col):
            return True
        if (self.__check_all_list(self._board[x][y], self.__get_bottom_left([x, y], 5))
                and x + 5 <= self.__col):
            return True
        return False

    # 檢查是否有四子可連線成五子
    def check_four(self, x, y):
        if self._board[x][y] == 0:
            return False
        # check left
        if self.__check_line([x, y], self._board[x][y:y+5:1], 4):
            # return [x, y + self.__get_connect_point([i[y] for i in self._board[x:x+5:1]])]
            print(self._board[x][y:y+5:1])
            return self.__get_connect_point(self._board[x][y:y+5:1])
        # check bottom
        if self.__check_line([x, y], [i[y] for i in self._board[x:x+5:1]], 4):
            return [x + self.__get_connect_point([i[y] for i in self._board[x:x+5:1]]), y]

        # check upper left
        if self.__check_line([x, y], self.__get_upper_left([x, y], 5), 4):
            return [x + self.__get_connect_point([i[y] for i in self._board[x:x+5:1]]), y]
        # check bottom left
        if self.__check_line([x, y], self.__get_bottom_left([x, y], 5), 4):
            return [x + self.__get_connect_point([i[y] for i in self._board[x:x+5:1]]), y]
        return False
