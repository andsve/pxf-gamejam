#!/usr/bin/env python
import pygame

class GameObject:
    def __init__(self, pos, sprite):
        Sprite.__init__(self)
        self.pos = pos
        self.sprite = sprite
        
    def update(self):
        pass
    
    def draw(self, canvas):
        canvas.blit(self.sprite, self.pos)