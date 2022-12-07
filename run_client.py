import gomoku_socket.client as gs
import gomoku_game.chess as ch


def print_chessborad(chseeborad):
    for i in chseeborad:
        for j in range(0, len(i)):
            if j == 0:
                print("[ ", end="")
            print(i[j], end=" ")
            if j == len(i) - 1:
                print("]", end="")
        print()


if __name__ == '__main__':

    chess = ch.GomokuGame(15, 15)
    client = gs.GomokuClient()

    # chess.randon_chessborad()
    
    # chess.set_chessboard(7,7)
    # chess.set_chessboard(7,8)
    # chess.set_chessboard(7,9)
    # chess.set_chessboard(7,10)
    # chess.set_chessboard(7,11)

    chess.set_chessboard(7,7)
    chess.set_chessboard(6,8)
    chess.set_chessboard(5,9)
    chess.set_chessboard(4,10)
    chess.set_chessboard(3,11)

    # chess.set_chessboard(7,7)
    # chess.set_chessboard(8,8)
    # chess.set_chessboard(9,9)
    # chess.set_chessboard(10,10)
    # chess.set_chessboard(11,11)

    # chess.set_chessboard(7,7)
    # chess.set_chessboard(6,6)
    # chess.set_chessboard(5,5)
    # chess.set_chessboard(4,4)
    chess.set_chessboard(3,3)
    data = {'chess_record': chess.get_chessboard()}
    client.connect()

    client.send_data(data)
    data = client.recv_data()

    print_chessborad(data['next_step'])
    print(data['game_over'])
