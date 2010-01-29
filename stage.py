#!/usr/bin/env python
import pygame
import utils

class Stage:
    def __init__(self):
        self.tiles = []
        self.game_objects = []
        
    def load(self):
        pass
        
    def draw(self, canvas):
        for tile in self.tiles:
            tile.draw(canvas)
            
class Stage1(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.load()
        
    def load(self):
        import gameobject
        green_sprite = utils.load_sprite("data/red_block16.png")
        blue_sprite = utils.load_sprite("data/blue_block16.png")
        self.tiles.append(gameobject.StaticBlock((0, 0), green_sprite))
        self.tiles.append(gameobject.StaticBlock((0, 0), blue_sprite))

        
        
            