import gomoku_socket.client as gs
import gomoku_game.chess as ch


def print_chessborad(chseeborad):
    print("    ", end = "")
    for i in range(len(chseeborad)):
        print(i, end = " ")
    print()

    for index, i in enumerate(chseeborad):
        for j in range(0, len(i)):
            if j == 0:
                print(index , "[ ", end="")
            print(i[j], end=" ")
            if j == len(i) - 1:
                print("]", end="")
        print()


if __name__ == '__main__':

    chess = ch.GomokuGame(10, 10)
    client = gs.GomokuClient()

    print_chessborad(chess.get_chessboard())
    while True:

        x, y = 10, 10
        while x > 9 or not(isinstance(x, int)):
            x = int(input("Please input x:"))
        while y > 9 or not(isinstance(y, int)):
            y = int(input("Please input y:"))

        chess.set_chessboard(x, y)

        print('\033c', end='')
        print_chessborad(chess.get_chessboard())

        data = {'chess_record': chess.get_chessboard()}
        client.connect()
        client.send_data(data)
        data = client.recv_data()

        chess.set_chessboard_com(data['move'][0], data['move'][1])

        print('\033c', end='')
        print("this score:", data['score'], "move:", data['move'])
        print_chessborad(chess.get_chessboard())
    
