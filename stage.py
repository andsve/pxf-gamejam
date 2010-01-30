#!/usr/bin/env python
import pygame
import util

class Stage:
    def __init__(self):
        self.tiles = []
        self.game_objects = []
        
    def load(self):
        pass
    
    def collide(self,rect):
        pass
        
    def draw(self,canvas):
        for tile in self.tiles:
            #discard items that should not be drawn
            if self.collide(tile.sprite.rect):
                tile.draw(canvas)
            
class Stage1(Stage):
    def __init__(self,camera_rect):
        Stage.__init__(self)
        self.load()
        self.camera_rect = camera_rect
    
    def collide(self,rect):
        return self.camera_rect.colliderect(rect)
        
    def load(self):
        import gameobject
        green_sprite = util.load_sprite("data/red_block16.png")
        green_sprite2 = util.load_sprite("data/green_block16.png")
        blue_sprite = util.load_sprite("data/blue_block16.png")
        self.tiles.append(gameobject.StaticBlock((0, 0), green_sprite))
        self.tiles.append(gameobject.StaticBlock((310, -10), green_sprite2))
        self.tiles.append(gameobject.StaticBlock((0, 0), blue_sprite))

        
        
            