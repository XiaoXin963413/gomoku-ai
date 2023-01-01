import gomoku_ai.base as base
import copy

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        self.minint = -2147483648
        self.maxint = 2147483648
        self.__player = 0
        self.__evaluate_table = self.__set_evaluate_table()

    def __set_evaluate_table(self):
        return {
            ('alive', 5) : 100000, ('death', 5) : 100000, ('close', 5) : 100000,
            ('alive', 4) : 10000, ('death', 4) : 1000, ('close', 4) : 0,
            ('alive', 3) : 1000, ('death', 3) : 100, ('close', 3) : 0,
            ('alive', 2) : 100, ('death', 2) : 10, ('close', 2) : 0,
            ('alive', 1) : 10, ('death', 1) : 1, ('close', 1) : 0,
        }

    def __piece_chess(self, board, position, player):
        tmp = copy.deepcopy(board)
        x, y = position[0], position[1]
        tmp[x][y] = player
        return tmp

    def __evaluate_role(self, board, role):
        value = 0
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (board[x][y] != role):
                    continue
                for num in range(2, 6):
                    result = self._check_connected(board, [x, y], num)
                    if result:
                        value += self.__evaluate_table[(result, num)]
                        continue
                    result = self._check_single_chess(board, x, y)
                    if result:
                        value += self.__evaluate_table[(result, num)]
                        continue
        return value

    def __evaluate_board(self, board):
        return self.__evaluate_role(board, 2) - self.__evaluate_role(board, 1)

    def __game_over(self, borad):
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if (borad[x][y] == 0):
                    continue
                if self._check_connected(borad, [x, y], 5):
                    return True
        return False

    def __get_possible_moves(self, board):
        possible_moves = []
        for x in range(self._BOARD_SIZE):
            for y in range(self._BOARD_SIZE):
                if board[x][y] != 0:
                    continue
                possible_moves.append((x, y))
        return possible_moves

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.__game_over(board):
            value = self.__evaluate_board(board)
            return value, None

        if maximizingPlayer:
            max_eval = self.minint
            base_move = None
            for move in self.__get_possible_moves(board):
                next_board = self.__piece_chess(board, [move[0], move[1]], 1)
                eval, _ = self.minimax(next_board, depth-1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    base_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    print(alpha)
                    self._print_chessborad(next_board)
                    break # beta cut-off
            return max_eval, base_move

        else:
            minEval = self.maxint
            bestMove = None
            for move in self.__get_possible_moves(board):
                next_board = self.__piece_chess(board, [move[0], move[1]], 2)
                eval, _ = self.minimax(next_board, depth-1, alpha, beta, True)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
                beta = min(beta, eval)
                if beta <= alpha:
                    print(beta)
                    self._print_chessborad(next_board)
                    break # alpha cut-off
            return minEval, bestMove
