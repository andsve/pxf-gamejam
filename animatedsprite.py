#!/usr/bin/env python
import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames):
        Sprite.__init__(self)
        self.frames = frames
        self.index = 0
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.active = False
        
    def update(self, *args):
        if self.active:
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
            self.rect = self.image.get_rect(center=self.rect.center)
        
        
