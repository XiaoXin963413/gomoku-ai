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
            ('live', 5) : 10000, ('death', 5) : 10000, ('close', 5) : 10000,
            ('live', 4) : 1000, ('death', 4) : 100, ('close', 5) : 0,
            ('live', 3) : 10, ('death', 3) : 1, ('close', 3) : 0,
            ('live', 2) : 2, ('death', 2) : 1, ('close', 2) : 0,
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
        value = self.minint
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (next_state[x][y] != self.__player):
                    continue
                result = self._check_connected(next_state, x, y, 5)
                if result:
                    if self.__evaluate_table[(result, 5)] > value:
                        value = self.__evaluate_table[(result, 5)]
                result = self._check_connected(next_state, x, y, 4)
                if result:
                    if self.__evaluate_table[(result, 4)] > value:
                        value = self.__evaluate_table[(result, 4)]
                result = self._check_connected(next_state, x, y, 3)
                if result:
                    if self.__evaluate_table[(result, 3)] > value:
                        value = self.__evaluate_table[(result, 3)]
                result = self._check_connected(next_state, x, y, 2)
                if result:
                    if self.__evaluate_table[(result, 2)] > value:
                        value = self.__evaluate_table[(result, 2)]
        return value

    def Set_player(self, value):
        self.__player = value

    def Next_step(self):
        state = "Hello"
        best_value = self.minint
        position = []
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if self._check_connected(self._board, x, y, 5):
                    state = self.__get_winner(self._board[x][y])
                    return state, None

        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (self._board[x][y] != 0):
                    continue
                next_state = self.__create_state(self._board, [x, y], self.__player)
                value = self.__evaluate_board(next_state)
                if value > best_value:
                    best_value = value
                    position = [x, y]
                    state = "Continue"

        return state, best_value

# def five_chess_AI(board, depth, alpha, beta, maximizing_player):
#       if depth == 0:
#     return evaluate_board(board)
  
#   if maximizing_player:
#     best_value = -infinity
#     for move in get_possible_moves(board):
#       new_board = make_move(board, move)
#       value = five_chess_AI(new_board, depth - 1, alpha, beta, False)
#       best_value = max(best_value, value)
#       alpha = max(alpha, value)
#       if beta <= alpha:
#         break
#     return best_value
#   else:
#     best_value = infinity
#     for move in get_possible_moves(board):
#       new_board = make_move(board, move)
#       value = five_chess_AI(new_board, depth - 1, alpha, beta, True)
#       best_value = min(best_value, value)
#       beta = min(beta, value)
#       if beta <= alpha:
#         break
#     return best_value