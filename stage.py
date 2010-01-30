from __future__ import with_statement
import pygame
import util

class Stage:
    def __init__(self, space):
        self.tiles = []
        self.game_objects = []

    def load(self, space):
        pass

    def collide(self,rect):
        pass

    def draw(self,canvas):
        for tile in self.tiles:
            #discard items that should not be drawn
            if self.collide(tile.sprite.rect):
                tile.draw(canvas)
            else:
                #print tile.pos
                pass

class Stage1(Stage):
    def __init__(self,camera, space):
        Stage.__init__(self, space)
        self.load(space)
        self.camera = camera

    def collide(self,rect):
        return rect.colliderect(self.camera.rect)

    def load(self, space):
        import gameobject
        import sys

        rblock = util.load_image("data/red_block16.png")
        gblock = util.load_image("data/green_block16.png")
        bblock = util.load_image("data/blue_block16.png")
        wblock = util.load_image("data/bw_block16.png")

        with open("data/level1.txt") as f:
            data = f.readlines()

        for rnum, row in enumerate(data):
            for cnum, col in enumerate(row):
                if   col == 'R':
                    block = rblock
                    type = gameobject.OBJECT_TYPE_RED
                elif col == 'G':
                    block = gblock
                    type = gameobject.OBJECT_TYPE_GREEN
                elif col == 'B':
                    block = bblock
                    type = gameobject.OBJECT_TYPE_BLUE
                elif col == 'W':
                    block = wblock
                    type = gameobject.OBJECT_TYPE_BW
                else: continue
                pos = util.vec2(cnum * 16, rnum * 16)
                go = gameobject.StaticBlock(pos, util.to_sprite(block), space, type)
                self.tiles.append(go)