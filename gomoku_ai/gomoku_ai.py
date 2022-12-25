import gomoku_ai.base as base
import copy

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        self.minint = -2147483648
        self.__evaluate_table = self.__set_evaluate_table()

    def __set_evaluate_table(self):
        return {
            ('live', 5) : 10000, ('death', 5) : 10000, ('close', 5) : 10000,
            ('live', 4) : 1000, ('death', 4) : 100, ('close', 5) : 0,
            ('live', 3) : 10, ('death', 3) : 1, ('close', 3) : 0,
            ('live', 2) : 2, ('death', 1) : 1, ('close', 2) : 0,
            ('live', 1) : 1, ('death', 1) : 1, ('close', 1) : 0,
        }

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
                result = self._check_connected(next_state, x, y, 5)
                if result:
                    return self.__evaluate_table[(result, 5)]
                result = self._check_connected(next_state, x, y, 4)
                if result:
                    return self.__evaluate_table[(result, 4)]
                result = self._check_connected(next_state, x, y, 3)
                if result:
                    return self.__evaluate_table[(result, 3)]
                result = self._check_connected(next_state, x, y, 2)
                if result:
                    return self.__evaluate_table[(result, 2)]
                result = self._check_connected(next_state, x, y, 1)
                if result:
                    return self.__evaluate_table[(result, 1)]

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
                    state = best_value

        return state