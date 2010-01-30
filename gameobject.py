#!/usr/bin/env python
import pygame
import util

class GameObject:
    def __init__(self, pos, sprite):
        self.pos = pos # position in pixels
        self.dir = util.vec2(0, 0) # direction
        self.vel = util.vec2(0, 0) # velocity in pixels/frame
        self.sprite = sprite   
        
    def update(self):
        pass
    
    def draw(self, canvas):
        canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_MAX)
        
        
class StaticBlock(GameObject):
    def __init__(self, pos, sprite):
        GameObject.__init__(self, pos, sprite)
        

    def update(self):
        pass