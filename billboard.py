#!/usr/bin/env python
import util
import pygame

class Billboard:
    def __init__(self,name,pos,animated = False):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.is_animated = animated
        self.pos = pos
    
    def draw(self,cam_pos):
        if not self.is_animated:
            canvas.blit(self.image, (self.pos[0]-cam_pos[0],self.pos[1]-cam_pos[1]), None, pygame.BLEND_MAX)
        pass
    
    def update():
        pass