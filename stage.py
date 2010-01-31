from __future__ import with_statement
import pygame
import util
import gameobject
import animation

STAGE_INTRO = 1
STAGE_1 = 2
STAGE_2 = 3
STAGE_3 = 4
STAGE_5 = 5
STAGE_6 = 6

class Stage:
    def __init__(self, player, space):
        self.tiles = []
        self.player = player
        self.game_objects = []
        self.info_blocks = []
        self.splosion_objects = []
        self.keys = { gameobject.OBJECT_TYPE_KEY_RED : False,
                     gameobject.OBJECT_TYPE_KEY_GREEN : False,
                     gameobject.OBJECT_TYPE_KEY_BLUE : False }

    def finished(self):
        return (self.keys[gameobject.OBJECT_TYPE_KEY_RED] and self.keys[gameobject.OBJECT_TYPE_KEY_GREEN] and self.keys[gameobject.OBJECT_TYPE_KEY_BLUE])

    def load(self, filepath, space):
        import sys
        #goal
        doorblock = util.load_image("data/entity_door0.png")

        # standard blocks
        rblock = util.load_image("data/red_block16.png")
        gblock = util.load_image("data/green_block16.png")
        bblock = util.load_image("data/blue_block16.png")
        wblock = util.load_image("data/bw_block16.png")
        #keys
        rkblock = util.load_image("data/red_key0.png")
        gkblock = util.load_image("data/green_key0.png")
        bkblock = util.load_image("data/blue_key0.png")
        # movable
        r_movableblock = util.load_image("data/red_movable_block0.png")
        g_movableblock = util.load_image("data/green_movable_block0.png")
        b_movableblock = util.load_image("data/blue_movable_block0.png")

        with open(filepath) as f:
            data = f.readlines()

        xoffset = 7
        yoffset = 3

        for rnum, row in enumerate(data):
            for cnum, col in enumerate(row):
                movable = False
                if   col == '1':
                    block = r_movableblock
                    movable = True
                    type = gameobject.OBJECT_TYPE_RED
                elif   col == '2':
                    block = g_movableblock
                    movable = True
                    type = gameobject.OBJECT_TYPE_GREEN
                elif   col == '3':
                    block = b_movableblock
                    movable = True
                    type = gameobject.OBJECT_TYPE_BLUE
                elif   col == 'R':
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
                elif col == 'X':
                    block = rkblock
                    type = gameobject.OBJECT_TYPE_KEY_RED
                elif col == 'Y':
                    block = gkblock
                    type = gameobject.OBJECT_TYPE_KEY_GREEN
                elif col == 'Z':
                    block = bkblock
                    type = gameobject.OBJECT_TYPE_KEY_BLUE
                elif col == 'D':
                    block = doorblock
                    type = gameobject.OBJECT_TYPE_GOAL
                    self.doorpos = (cnum * 16 - xoffset * 16, rnum * 16 - yoffset * 16)
                elif col == 'P':
                    self.player.body.position = (cnum * 16 - xoffset * 16, rnum * 16 - yoffset * 16)
                    continue
                else: continue
                pos = util.vec2(cnum * 16 - xoffset * 16, rnum * 16 - yoffset * 16)
                if (movable):
                    go = gameobject.MovableBlock(pos, util.to_sprite(block), space, type)
                    self.game_objects.append(go)
                else:
                    go = gameobject.StaticBlock(pos, util.to_sprite(block), space, type)
                    self.tiles.append(go)


    def collide(self,rect):
        return rect.colliderect(self.camera.rect)

    def draw(self,canvas):
        for tile in self.tiles:
            #discard items that should not be drawn
            if self.collide(tile.sprite.rect):
                tile.draw(canvas)
            else:
                #print tile.pos
                pass
        for splosion in self.splosion_objects:
            splosion.draw(canvas)
        for obj in self.game_objects:
            obj.draw(canvas)
        for inf in self.info_blocks:
            inf.draw(canvas)

class IntroStage(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/intro_level.txt", space)
        self.camera = camera
        info1 = gameobject.InfoBlock(util.vec2(16,16), util.to_sprite(util.load_image("data/red_block16.png")), space)
        self.info_blocks.append(info1)

class Stage1(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/level1.txt", space)
        self.camera = camera

class Stage2(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/stage2.txt", space)
        self.camera = camera

class Stage3(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/stage3.txt", space)
        self.camera = camera
        self.keys[gameobject.OBJECT_TYPE_KEY_GREEN] = True
        self.keys[gameobject.OBJECT_TYPE_KEY_BLUE] = True

class Stage5(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/stage5.txt", space)
        self.keys[gameobject.OBJECT_TYPE_KEY_GREEN] = True
        self.keys[gameobject.OBJECT_TYPE_KEY_BLUE] = True
        self.camera = camera

class Stage6(Stage):
    def __init__(self,camera, player, space):
        Stage.__init__(self, player, space)
        self.load("data/stage6.txt", space)
        self.camera = camera
