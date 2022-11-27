import gomoku_socket.client as gs
import gomoku_game.chess as ch

def print_chessborad(chseeborad):
    for i in chseeborad:
        for j in range(0, len(i)):
            if j == 0:
                print("[ ", end="")
            print(i[j], end=" ")
            if j == 18:
                print("]", end="")
        print()

if __name__ == '__main__':

    chess = ch.GomokuGame()
    client = gs.GomokuClient()

    chess.randon_chessborad()
    data = {'chess_record':chess.get_chessboard()}
    client.connect()

    client.send_data(data)
    data = client.recv_data()

    print_chessborad(data['chess_record'])