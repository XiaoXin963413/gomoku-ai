import random
import asyncio
import numpy as np


class BaseBoard():
    def Set_board(self, board):
        self._board = board
        self._BOARD_SIZE = len(board)
        self.__live_state = {0: "close", 1: "death", 2: "alive"}

    def _print_chessborad(self, board):
        print("    ", end="")
        for i in range(len(board)):
            print(i, end=" ")
        print()

        for index, i in enumerate(board):
            for j in range(0, len(i)):
                if j == 0:
                    print(index, "[ ", end="")
                print(i[j], end=" ")
                if j == len(i) - 1:
                    print("]", end="")
            print()

    def _game_over(self, borad):
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (borad[x][y] == 0):
                    continue
                if self._check_connected(borad, [x, y], 5):
                    return True
        return False

    def __check_alive(self, board, x, y, direction, num):
        state = 0
        if direction == (0, 1):
            if y+num < len(board):
                if board[x][y+num] == 0:
                    state += 1
            if y-1 >= 0:
                if board[x][y-1] == 0:
                    state += 1
            return self.__live_state[state]
        if direction == (1, 0):
            if x+num < len(board):
                if board[x+num][y] == 0:
                    state += 1
            if x-1 >= 0:
                if board[x-1][y] == 0:
                    state += 1
            return self.__live_state[state]
        if direction == (1, 1):
            if x+num < len(board) and y+num < len(board):
                if board[x+num][y+num] == 0:
                    state += 1
            if x-1 >= 0 and y-1 >= 0:
                if board[x-1][y-1] == 0:
                    state += 1
            return self.__live_state[state]
        if direction == (-1, 1):
            if x-num >= 0 and y+num < len(board):
                if board[x-num][y+num] == 0:
                    state += 1
            if x+1 < len(board) and y-1 >= 0:
                if board[x+1][y-1] == 0:
                    state += 1
            return self.__live_state[state]

    def __check_line(self, board, x, y, direction, origin):
        dx, dy = direction[0], direction[1]
        count = 1
        while True:
            x += dx
            y += dy
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                break
            if board[x][y] != origin:
                break
            count += 1
        return count

    def _check_connected(self, board, position, num):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        x, y = position[0], position[1]
        origin = board[x][y]
        for direction in directions:
            count = self.__check_line(board, x, y, direction, origin)
            if count == num:
                return self.__check_alive(board, x, y, direction, num)
        return False

    def _check_single_chess(self, board, x, y, role):
        if (x+1 < self._BOARD_SIZE and y+1 < self._BOARD_SIZE and x-1 >= 0 and y-1 >= 0):
            if (board[x][y+1] == board[x+1][y] == board[x][y-1] == board[x+1][y] ==
                    board[x+1][y+1] == board[x-1][y+1] == board[x+1][y-1] == board[x-1][y-1] == role):
                return 'alive'
            return 'death'
        else:
            return 'close'
