#!/usr/bin/env python
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
        red_sprite = util.load_image("data/red_block16.png")
        green_sprite = util.load_image("data/green_block16.png")
        blue_sprite = util.load_image("data/blue_block16.png")
        self.tiles.append(gameobject.StaticBlock(util.vec2(0, 0), util.to_sprite(red_sprite), space, gameobject.OBJECT_TYPE_RED))
        self.tiles.append(gameobject.StaticBlock(util.vec2(310, -10), util.to_sprite(green_sprite), space, gameobject.OBJECT_TYPE_GREEN))
        self.tiles.append(gameobject.StaticBlock(util.vec2(0, 0), util.to_sprite(blue_sprite), space, gameobject.OBJECT_TYPE_BLUE))

        self.tiles.append(gameobject.StaticBlock(util.vec2(0, 50), util.to_sprite(blue_sprite), space, gameobject.OBJECT_TYPE_BLUE))
        self.tiles.append(gameobject.StaticBlock(util.vec2(16, 50), util.to_sprite(blue_sprite), space, gameobject.OBJECT_TYPE_BLUE))
        self.tiles.append(gameobject.StaticBlock(util.vec2(32, 34), util.to_sprite(blue_sprite), space, gameobject.OBJECT_TYPE_BLUE))
