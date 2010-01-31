#!/usr/bin/env python
import util
import pygame

class Billboard:
    def __init__(self,name,pos,speed,repeat = False,animated = False):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.is_animated = animated
        self.pos = pos
        self.draw_pos = util.vec2(0,0)
        self.speed = speed
        self.inv_speed = speed/10.
        self.repeat = repeat
    
    def draw(self,canvas):
        if not self.is_animated:
            if self.repeat:
                canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
                canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        pass
    
    def update(self,cam_pos,dt):        
        self.draw_pos.set(self.pos[0]-cam_pos.x*self.inv_speed,
                         self.pos[1]-cam_pos.y*self.inv_speed)
        self.pos[0] * dt
        self.pos[1] * dt
        
        #print self.draw_pos
        
        if self.draw_pos.x < -320:
            self.draw_pos.x = -320
            
        if self.draw_pos.x > 320:
            self.draw_pos.x = 320
        
        #print self.draw_pos.x 