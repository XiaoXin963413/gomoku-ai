import gomoku_ai.base as base
import copy

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        self.minint = -2147483648
        self.maxint = 2147483648
        self.__evaluate_table = self.__set_evaluate_table()
        self.__search_range = {'normal':[-1, 0, 1], 'hard':[-2, -1, 0, 1, 2]}
        self.__difficulty = self.Set_difficulty()
        self.__inv_player = {1:2, 2:1}
        self.__count = 0

    def Get_count(self):
        return self.__count

    def Set_difficulty(self, config='normal'):
        return self.__search_range[config]

    def __set_evaluate_table(self):
        return {
            ('alive', 5) : 100000, ('death', 5) : 100000, ('close', 5) : 100000,
            ('alive', 4) : 10000, ('death', 4) : 5000, ('close', 4) : 0,
            ('alive', 3) : 1000, ('death', 3) : 500, ('close', 3) : 0,
            ('alive', 2) : 100, ('death', 2) : 50, ('close', 2) : 0,
            ('alive', 1) : 10, ('death', 1) : 5, ('close', 1) : 0,
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
                for num in range(5, 1, -1):
                    result = self._check_connected(board, [x, y], num)
                    if result:
                        value += self.__evaluate_table[(result, num)]
                        continue
                result = self._check_single_chess(board, x, y, self.__inv_player[role])
                if result:
                    value += self.__evaluate_table[(result, 1)]
                    continue
        return value

    def __evaluate_board(self, board):
        return self.__evaluate_role(board, 2) - self.__evaluate_role(board, 1)

    # def __get_possible_moves(self, board):
    #     possible_moves = []
    #     for x in range(self._BOARD_SIZE):
    #         for y in range(self._BOARD_SIZE):
    #             if board[x][y] != 0:
    #                 continue
    #             possible_moves.append((x, y))
    #     return possible_moves

    def __get_possible_moves(self, board):
        possible_moves = {}
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if board[i][j] == 0:
                    continue
                for x in self.__difficulty:
                    for y in self.__difficulty:
                        if x == 0 and y == 0:
                            continue
                        if i + x >= 0 and i + x < self._BOARD_SIZE and j + y >= 0 and j + y < self._BOARD_SIZE and board[i + x][j + y] == 0:
                            possible_moves[(i + x, j + y)] = True
        return list(possible_moves.keys())

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        self.__count += 1
        if depth == 0 or self._game_over(board):
            value = self.__evaluate_board(board)
            return value, None, board

        if maximizingPlayer:
            max_score = self.minint
            best_move = None
            if depth == 4:
                print(self.__get_possible_moves(board))
            for move in self.__get_possible_moves(board):
                next_board = self.__piece_chess(board, [move[0], move[1]], 2)
                score, _, last_board = self.minimax(next_board, depth-1, alpha, beta, False)
                if score > max_score:
                    max_score = score
                    best_move =  move
                    best_board = last_board
                alpha = max(alpha, max_score)
                if beta < alpha:
                    break # beta cut-off
            return max_score, best_move, best_board

        else:
            min_score = self.maxint
            best_move = None
            for move in self.__get_possible_moves(board):
                next_board = self.__piece_chess(board, [move[0], move[1]], 1)
                score, _, last_board = self.minimax(next_board, depth-1, alpha, beta, True)
                if score < min_score:
                    min_score = score
                    best_move =  move
                    best_board = last_board
                beta = min(beta, min_score)
                if beta < alpha:
                    break # alpha cut-off
            return min_score, best_move, best_board
