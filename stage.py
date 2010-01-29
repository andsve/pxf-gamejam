#!/usr/bin/env python
import pygame
import util

class Stage:
    def __init__(self):
        self.tiles = []
        self.game_objects = []
        
    def load(self):
        pass
        
    def draw(self,canvas,camera_pos):
        for tile in self.tiles:
            #discard items that should not be drawn
            tile.draw(canvas)
            
class Stage1(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.load()
        
    def load(self):
        import gameobject
        green_sprite = util.load_sprite("data/red_block16.png")
        blue_sprite = util.load_sprite("data/blue_block16.png")
        self.tiles.append(gameobject.StaticBlock((0, 0), green_sprite))
        self.tiles.append(gameobject.StaticBlock((0, 0), blue_sprite))

        
        
            