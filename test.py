__chess_row = 10
__chess_col = 10
__chessboard = [[0 for _ in range(__chess_row)] for _ in range(__chess_col)]

__chessboard[0][9] = 1
__chessboard[1][8] = 1

def print_chessborad(chseeborad):
    # print(range(len(chseeborad[0])))
    print("     ", end="")
    for i in range(len(chseeborad)):
        print(i, end=" ")
    print()
    for i, item in enumerate(chseeborad):
        for j in range(0, len(item)):
            if j == 0:
                print(i, " [ ", end="")
            print(item[j], end=" ")
            if j == len(item) - 1:
                print("]", end="")
        print()

print_chessborad(__chessboard)

def __get_upper_left(position, current, num):
    x, y = position[0], position[1]
    if (x - num + 1) < 0 or (y + num - 1) >= 10:
        return []
    i, j, list = 0, 0, []
    for _ in range(num):
        list.append(current[x+i][y+j])
        i, j = i - 1, j + 1
    return list

print(__get_upper_left([2, 7], __chessboard, 3))