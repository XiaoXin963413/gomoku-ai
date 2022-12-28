import gomoku_ai.base as base
import copy

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        self.minint = -2147483648
        self.__player = 0
        self.__evaluate_table = self.__set_evaluate_table()

    def __set_evaluate_table(self):
        return {
            ('live', 5) : 100000, ('death', 5) : 100000, ('close', 5) : 100000,
            ('live', 4) : 10000, ('death', 4) : 1000, ('close', 4) : 0,
            ('live', 3) : 1000, ('death', 3) : 100, ('close', 3) : 0,
            ('live', 2) : 100, ('death', 2) : 10, ('close', 2) : 0,
            ('live', 1) : 10, ('death', 1) : 1, ('close', 1) : 0,
        }

    def __piece_chess(self, current, position, player):
        tmp = copy.deepcopy(current)
        x, y = position[0], position[1]
        tmp[x][y] = player
        return tmp

    def __get_winner(self, value):
        if value == 1:
            return "Player win!"
        else:
            return "Computer win!"

    def __evaluate_board(self, next_state, player):
        value = 0
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (next_state[x][y] != player):
                    continue
                result = self._check_connected(next_state, x, y, 5)
                if result:
                    value = value + self.__evaluate_table[(result, 5)]
                result = self._check_connected(next_state, x, y, 4)
                if result:
                    value = value + self.__evaluate_table[(result, 4)]
                result = self._check_connected(next_state, x, y, 3)
                if result:
                    value = value + self.__evaluate_table[(result, 3)]
                result = self._check_connected(next_state, x, y, 2)
                if result:
                    value = value + self.__evaluate_table[(result, 2)]
                result = self._check_single_chess(next_state, x, y)
                if result:
                    value = value + self.__evaluate_table[(result, 1)]
        return value

    def Next_step(self, player):
        best_value = self.minint
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if self._check_connected(self._board, x, y, 5):
                    return self.__get_winner(self._board[x][y])

        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (self._board[x][y] != 0):
                    continue
                next_state = self.__piece_chess(self._board, [x, y], player)
                value = self.__evaluate_board(next_state, player)
                if value > best_value:
                    best_value = value
                    position = [x, y]

        return position

    # def getBestMove(self, depth):
    #   _, bestPosition = self.minimax(self._board, depth, -0, 0, False)
    #   return bestPosition


    # def minimax(self, broad, depth, alpha, beta, layer):
    #     if depth == 0 or self._check_win(broad):
    #         print(self.__evaluate_board(broad, 1) if layer else self.__evaluate_board(broad, 2), None)
    #         return self.__evaluate_board(broad, 1) if layer else self.__evaluate_board(broad, 2), None

    #     if layer:
    #         bestValue = self.minint
    #         for x in range(self._BOARD_SIZE):
    #             for y in range(self._BOARD_SIZE):
    #                 if (self._board[x][y] != 0):
    #                     continue
    #                 new_state = self.__piece_chess(self._board, [x, y], 1)
    #                 value, _ = self.minimax(new_state, depth - 1, alpha, beta, False)
    #                 if value > bestValue:
    #                     bestValue = value
    #                     bestPosition = [x, y]
    #                 alpha = max(alpha, value)
    #                 if alpha >= beta:
    #                     break
    #                 return bestValue, bestPosition
    #     else:
    #         bestValue = self.minint
    #         for x in range(self._BOARD_SIZE):
    #             for y in range(self._BOARD_SIZE):
    #                 if (self._board[x][y] != 0):
    #                     continue
    #                 new_state = self.__piece_chess(self._board, [x, y], 2)
    #                 value, _ = self.minimax(new_state, depth - 1, alpha, beta, True)
    #                 if value > bestValue:
    #                     bestValue = value
    #                     bestPosition = [x, y]
    #                 alpha = max(alpha, value)
    #                 if alpha >= beta:
    #                     break
    #                 return bestValue, bestPosition