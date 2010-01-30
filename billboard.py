#!/usr/bin/env python
import util
import pygame

class Billboard:
    def __init__(self,name,static = True):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.is_static = static
    
    def draw(self):
        pass
    
    def update():
        pass