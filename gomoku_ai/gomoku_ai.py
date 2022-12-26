import gomoku_ai.base as base
import copy

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        self.minint = -2147483648

    def __create_state(self, current, position, player):
        tmp = copy.deepcopy(current)
        x, y = position[0], position[1]
        tmp[x][y] = player
        return tmp

    def __get_winner(self, value):
        if value == 1:
            return "Player win!"
        else:
            return "Computer win!"

    def __evaluate_board(self, next_state):
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if self._check_connected(next_state, x, y, 5):
                    return 10000
                if self._check_connected(next_state, x, y, 4):
                    return 1000
                if self._check_connected(next_state, x, y, 3):
                    return 100
                if self._check_connected(next_state, x, y, 2):
                    return 10
        return 1

    def Next_step(self):
        state = "None"
        best_value = self.minint
        position = []
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if self._check_connected(self._board, x, y, 5):
                    state = self.__get_winner(self._board[x][y])
                    return state

        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (self._board[x][y] != 0):
                    continue
                next_state = self.__create_state(self._board, [x, y], 1)
                value = self.__evaluate_board(next_state)
                if value > best_value:
                    best_value = value
                    position = [x, y]
                    state = position

        return state