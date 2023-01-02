import gomoku_socket.client as gs
import gomoku_game.chess as ch
import sys


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
    borad_size = 10
    borad = ch.GomokuGame(borad_size)
    client = gs.GomokuClient()

    print_chessborad(borad.get_board())
    first = int(input("Who are first? (1):COM (2):Player"))
    while True:
        
        if first == 1:
            first = 2
            pass
        else:
            x, y = borad_size, borad_size
            while x >= borad_size or not(isinstance(x, int)):
                x = int(input("Please input x:"))
            while y >= borad_size or not(isinstance(y, int)):
                y = int(input("Please input y:"))
            borad.set_board(x, y)

        print('\033c', end='')
        print_chessborad(borad.get_board())

        if borad.Check_win(borad.get_board()):
            if borad.Continue():
                print('\033c', end='')
                print_chessborad(borad.get_board())
                first = int(input("Who are first? (1):COM (2):Player"))
                pass
            else:
                sys.exit(0)
        else:
            data = {'chess_record': borad.get_board()}
            client.connect()
            client.send_data(data)
            data = client.recv_data()
            borad.set_board_com(data['move'][0], data['move'][1])

            print('\033c', end='')
            print_chessborad(borad.get_board())

            if borad.Check_win(borad.get_board()):
                if borad.Continue():
                    print('\033c', end='')
                    print_chessborad(borad.get_board())
                    first = int(input("Who are first? (1):COM (2):Player"))
                    pass
                else:
                    sys.exit(0)
    
