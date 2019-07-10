# -*- coding: utf-8 -*-

import pyxel
import random
import copy

FALL_FLAME = 2

class App:
    def __init__(self):
        pyxel.init(128,160,caption="テトリス")
        self.tetrimino = TetriMino()
        self.board = Board()
        self.is_gameover = False

        pyxel.load('tetris.pyxres')
        pyxel.run(self.update, self.draw)



    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or self.is_gameover == True:
            pyxel.quit()
        
        # 10フレームごとに落ちてく
        if pyxel.frame_count % FALL_FLAME == 0:
            self.tetrimino.fall_down()
            self.collision_judgement()
            
                

    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()
        self.board.draw_block()
        self.tetrimino.draw_block()

    def tilemap_draw(self):
        base_x = 0
        base_y = 0
        tm = 0
        u = 0
        v = 0
        w = 16
        h = 20
        pyxel.bltm(base_x,base_y,tm,u,v,w,h)

    def collision_judgement(self):
        # ゲームオーバー
        # y = 1で重なったらゲームオーバー
        for x in range(10):
            if self.tetrimino.position[1][x] != 0 and self.board.position[1][x] != 0:
                self.is_gameover = True
        #一番下にテトリミノが来たときボードに貼り付ける
        if self.tetrimino.position[19].count(0) != 10:
            self.paste_board()
            # またテトリミノ生成
            self.tetrimino = TetriMino()
            return
        # 真下にブロックがあるときボードに貼り付ける
        for y in range(20):
            for x in range(10):
                if self.tetrimino.position[y][x] != 0 and self.board.position[y+1][x] != 0:
                    self.paste_board()
                    # またテトリミノ生成
                    self.tetrimino = TetriMino()
                    return
                    
    def paste_board(self): 
            for y in range(20):
                for x in range(10):
                    if self.tetrimino.position[y][x] != 0:
                        self.board.position[y][x] = self.tetrimino.position[y][x] 


class Board:
    def __init__(self):
        self.position =  [[0 for x in range(10)] for y in range(20)]
    
    def draw_block(self):
        for y in range(20):
            for x in range(10):
                if self.position[y][x] != 0:
                    pyxel.blt((x * 8) + 24, y * 8, 0, 8 * (self.position[y][x] - 1), 0, 8, 8) 


class TetriMino(Board):
    def __init__(self):
        super().__init__()
        self.generate_block()

    def fall_down(self):
        #19 -> 1 まで下に一つずつずらす
        for y in reversed(range(1,20)):
            self.position[y] = self.position[y - 1]
        #0行目は0に
        self.position[0] = [0 for x in range(10)]

    def generate_block(self):
        block_type = random.randint(1,7)
        if block_type == 1:
            self.position[0][5] = 1
            self.position[1][4] = 1
            self.position[1][5] = 1
            self.position[1][6] = 1
        elif block_type == 2:
            self.position[0][4] = 2
            self.position[1][4] = 2
            self.position[1][5] = 2
            self.position[1][6] = 2
        elif block_type == 3:
            self.position[0][6] = 3
            self.position[1][4] = 3
            self.position[1][5] = 3
            self.position[1][6] = 3
        elif block_type == 4:
            self.position[0][5] = 4
            self.position[0][6] = 4
            self.position[1][4] = 4
            self.position[1][5] = 4
        elif block_type == 5:
            self.position[0][4] = 5
            self.position[0][5] = 5
            self.position[1][5] = 5
            self.position[1][6] = 5
        elif block_type == 6:
            self.position[0][4] = 6
            self.position[0][5] = 6
            self.position[1][4] = 6
            self.position[1][5] = 6
        else :
            self.position[0][3] = 7
            self.position[0][4] = 7
            self.position[0][5] = 7
            self.position[0][6] = 7


        





if __name__ == "__main__":
    App()
