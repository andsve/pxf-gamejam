#!/usr/bin/env python
import pygame
import util

class GameObject:
    def __init__(self, pos, sprite):
        self.pos = pos # position in pixels
        self.vel = util.vec2(0, 0) # velocity in pixels/frame
        self.sprite = sprite
        self.draw_pos = util.vec2(0,0)
        
    def update_physics(self, objects, physics):
        old_values = (self.pos, self.vel)
        self.pos += self.vel
        self.vel += physics.gravity
        new_values = self.pos, self.vel
        return (old_values, new_values)
        
        
    def update(self):
        pass
    
    def draw(self, canvas):
        #canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_MAX)
        canvas.blit(self.sprite.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        draw_pos = util.vec2(0,0)
        
        
class StaticBlock(GameObject):
    def __init__(self, pos, sprite):
        GameObject.__init__(self, pos, sprite)
        

    def update(self,camera_pos):
        print camera_pos.get()
        self.draw_pos = self.pos - camera_pos
        pass