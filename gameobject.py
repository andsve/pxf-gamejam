#!/usr/bin/env python
import pygame
import util

class GameObject:
    def __init__(self, pos, sprite):
        self.pos = util.vec2(0, 0) # position in pixels
        self.vel = util.vec2(0, 0) # velocity in pixels/frame
        self.sprite = sprite
        
    def update_physics(self, objects, physics):
        old_values = (self.pos, self.vel)
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.vel.y += physics.gravity.x
        
        
    def update(self):
        pass
    
    def draw(self, canvas):
        canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_ADD)
        
        
class StaticBlock(GameObject):
    def __init__(self, pos, sprite):
        GameObject.__init__(self, pos, sprite)
        

    def update(self):
        pass