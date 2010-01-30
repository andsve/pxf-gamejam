#!/usr/bin/env python
from pygame import Rect

class Camera:
    def __init__(self,pos,size):
        self.pos = pos
        self.rect = Rect((0,0),size)
        
    def pos_add(self,val):
        pass
    
    def update(self):
        # update position
        pass