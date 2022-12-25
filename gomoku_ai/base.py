import random
import asyncio
import numpy as np


class BaseBoard():
    def set_board(self, board):
        self._board = board
        self._BOARD_SIZE = len(board)

    def __get_left(self, position, current, num):
        x, y = position[0], position[1]
        return current[x][y:y+num:1]

    def __get_bottom(self, position, current, num):
        x, y = position[0], position[1]
        return [i[y] for i in current[y:y+num:1]]

    def __get_upper_left(self, position, current, num):
        x, y = position[0], position[1]
        if (x - num) > self._BOARD_SIZE or (y + num) > self._BOARD_SIZE:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(current[x+i][y+j])
            i, j = i - 1, j + 1
        return list

    def __get_bottom_left(self, position, current, num):
        x, y = position[0], position[1]
        if (x + num) > self._BOARD_SIZE or (y + num) > self._BOARD_SIZE:
            return []
        i, j, list = 0, 0, []
        for _ in range(num):
            list.append(current[x+i][y+j])
            i, j = i + 1, j + 1
        return list

    def __check_all_list(self, var, list):
        if (list == []):
            return False
        return all(x == var and x is not True for x in list)

    def _print_chessborad(self, chseeborad):
        for i in chseeborad:
            for j in range(0, len(i)):
                if j == 0:
                    print("[ ", end="")
                print(i[j], end=" ")
                if j == len(i) - 1:
                    print("]", end="")
            print()

    # Check if there are number pieces connected
    def _check_connected(self, current, x, y, num):
        if current[x][y] == 0:
            return False
        # check left, bottom, upper left, bottom left
        if (self.__check_all_list(current[x][y], self.__get_left([x, y], current, num))
                and y + num <= self._BOARD_SIZE):
            return True
        if (self.__check_all_list(current[x][y], self.__get_bottom([x, y], current, num))
                and x + num <= self._BOARD_SIZE):
            return True
        if (self.__check_all_list(current[x][y], self.__get_upper_left([x, y], current, num))
                and y - num <= self._BOARD_SIZE):
            return True
        if (self.__check_all_list(current[x][y], self.__get_bottom_left([x, y], current, num))
                and y + num <= self._BOARD_SIZE):
            return True
        return False