#!/usr/bin/env python
import util
import pygame

class Billboard:
    def __init__(self,name,pos,speed,animated = False):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.is_animated = animated
        self.pos = pos
        self.draw_pos = None
        self.speed = speed
        self.inv_speed = speed/10.
    
    def draw(self,canvas):
        if not self.is_animated:
            canvas.blit(self.image, self.draw_pos, None, pygame.BLEND_MAX)
        pass
    
    def update(self,cam_pos,dt):        
        self.draw_pos = (self.pos[0]-cam_pos.x*self.inv_speed,
                         self.pos[1]-cam_pos.y*self.inv_speed)
        self.pos[0] * dt
        self.pos[1] * dt
        
        #print self.draw_pos
        
        if self.draw_pos[0] < 0:
            print "hknk"
        
        pass