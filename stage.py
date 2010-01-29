#!/usr/bin/env python
import pygame

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
        self.tiles.append(gameobject.GameObject((0, 0), pygame.image.load("data/green_block16.png")))
        self.tiles.append(gameobject.GameObject((0, 0), pygame.image.load("data/red_block16.png")))
        
        
            