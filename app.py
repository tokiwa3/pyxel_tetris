# -*- coding: utf-8 -*-

import pyxel


class App:
    def __init__(self):
        pyxel.init(128,160,caption="テトリス")
        self.move = Move()
        self.board = Position()
        self.board.position[19][5] = 2
        self.board.position[19][8] = 7

        pyxel.load('tetris.pyxres')
        pyxel.run(self.update, self.draw)



    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()
        self.board.draw_block()
        self.move.draw_block()

    def tilemap_draw(self):
        base_x = 0
        base_y = 0
        num = 0
        u = 0
        v = 0
        w = 16
        h = 20
        pyxel.bltm(base_x,base_y,num,u,v,w,h)


class Position:
    def __init__(self):
        self.position =  [[0 for x in range(10)] for y in range(20)]
    
    def draw_block(self):
        for y in range(20):
            for x in range(10):
                if self.position[y][x] != 0:
                    pyxel.blt((x * 8) + 24, y * 8, 0, 8 * (self.position[y][x] - 1), 0, 8, 8) 


class Move(Position):
    def __init__(self):
        super().__init__()
        self.position[0][4] = 2
        self.position[0][5] = 2
        self.position[1][4] = 2
        self.position[1][5] = 2



class TetriMino:
    def __init__(self):
        pass

if __name__ == "__main__":
    App()
