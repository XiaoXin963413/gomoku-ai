﻿#=====================================================================
# Gomoku
#=====================================================================
import pygame # class 0, c0
from Chessboard import Chessboard # class 2, c2

class Gomoku():# class 1, c1

    def __init__(self):
        pygame.init() #c0
        self.screen = pygame.display.set_mode((800, 600)) # c0
        pygame.display.set_caption("五子棋")
        self.clock = pygame.time.Clock()
        self.font=pygame.font.Font(r"C:\Windows\Fonts\consola.ttf",24)
        self.going = True
        self.chessboard = Chessboard() # c2

    def loop(self): # looping, not idle
        while self.going:
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.going = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.chessboard.handle_key_event(e) # c2

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))

        self.chessboard.draw(self.screen)
        if self.chessboard.game_over:
            self.screen.blit(self.font.render("{0} Win".format("Black" if self.chessboard.winner=='b' else "White"), True, (0, 0, 0)), (500, 10))

        pygame.display.update()
#=====================================================================


#=====================================================================
# Chessboard
#=====================================================================
import pygame# c0

class Chessboard: # c2

    def __init__(self):
        self.grid_size = 26
        self.start_x, self.start_y = 30, 50
        self.edge_size = self.grid_size / 2
        self.grid_count = 19
        self.piece = 'b'
        self.winner = None
        self.game_over = False

        self.grid = []
        for i in range(self.grid_count):
            self.grid.append(list("." * self.grid_count))

    def handle_key_event(self, e):
        origin_x = self.start_x - self.edge_size
        origin_y = self.start_y - self.edge_size
        size = (self.grid_count - 1) * self.grid_size + self.edge_size*2
        pos = e.pos
        if origin_x<=pos[0]<=origin_x+size and origin_y<=pos[1]<=origin_y+size:
            if not self.game_over:
                x = pos[0] - origin_x
                y = pos[1] - origin_y
                r = int(y // self.grid_size)
                c = int(x // self.grid_size)
                if self.set_piece(r, c): # 不好的作法，焦點模糊
                    self.check_win(r, c)

    def set_piece(self, r, c):
        if self.grid[r][c] == '.':
            self.grid[r][c] = self.piece
            if self.piece == 'b':
                self.piece = 'w'
            else:
                self.piece = 'b'
            return True
        return False


    def check_win(self, r, c):
        n_count = self.get_continuous_count(r, c, -1, 0)
        s_count = self.get_continuous_count(r, c, 1, 0)

        e_count = self.get_continuous_count(r, c, 0, 1)
        w_count = self.get_continuous_count(r, c, 0, -1)

        se_count = self.get_continuous_count(r, c, 1, 1)
        nw_count = self.get_continuous_count(r, c, -1, -1)

        ne_count = self.get_continuous_count(r, c, -1, 1)
        sw_count = self.get_continuous_count(r, c, 1, -1)

        if (n_count+s_count+1>=5) or (e_count+w_count+1>=5) or \
                (se_count+nw_count+1>=5) or (ne_count+sw_count+1>=5):
            self.winner = self.grid[r][c]
            self.game_over = True

    def get_continuous_count(self, r, c, dr, dc):
        piece = self.grid[r][c]
        result = 0
        i = 1
        while True:
            new_r = r + dr * i
            new_c = c + dc * i
            if 0 <= new_r < self.grid_count and \
                    0 <= new_c < self.grid_count:
                if self.grid[new_r][new_c] == piece:
                    result += 1
                else:
                    break
            else:
                break
            i += 1
        return result


    def draw(self, screen):
        # 棋盤底色
        pygame.draw.rect(screen, (185, 122, 87),
            [
            self.start_x - self.edge_size,
            self.start_y - self.edge_size,
            (self.grid_count - 1) * self.grid_size + self.edge_size * 2,
            (self.grid_count - 1) * self.grid_size + self.edge_size * 2],
            0)

        for r in range(self.grid_count):
            y = self.start_y + r * self.grid_size
            pygame.draw.line(screen, (0, 0, 0),
                [self.start_x, y],
                [self.start_x + self.grid_size * (self.grid_count - 1),
                y], 2)

        for c in range(self.grid_count):
            x = self.start_x + c * self.grid_size
            pygame.draw.line(screen, (0, 0, 0),
                [x, self.start_y],
                [x, self.start_y+self.grid_size*(self.grid_count-1)],
                2)

        for r in range(self.grid_count):
            for c in range(self.grid_count):
                piece = self.grid[r][c]
                if piece != '.':
                    if piece == 'b':
                        color = (0, 0, 0)
                    else:
                        color = (255, 255, 255)
                    x = self.start_x + c * self.grid_size
                    y = self.start_y + r * self.grid_size
                    pygame.draw.circle(screen, color, [x, y],
                        self.grid_size // 2) # smaller
#=====================================================================


#=====================================================================
#game = Gomoku()
#game.loop()
#=====================================================================
