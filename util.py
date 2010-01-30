#!/usr/bin/env python
import pygame.mixer
import pygame
import animatedsprite
#import os.path

class vec2:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "vec2(%d, %d)" % (self.x, self.y)
        
    def __imul__(self, v):
        self.x *= v
        self.y *= v
        return self
        
    def __idiv__(self, v):
        self.x /= v
        self.y /= v
        return self
        
    def __iadd__(self, v):
        self.x += v
        self.y += v
        return self
    
    def __isub__(self, v):
        self.x -= v
        self.y -= v
        return self
    
    def __mul__(self, v):
        self.x *= v.x
        self.y *= v.y
        return self
    
    def __div__(self, v):
        self.x /= v.x
        self.y /= v.y
        return self

    def __add__(self, v):
        self.x += v.x
        self.y += v.y
        return self
    
    def __sub__(self, v):
        self.x -= v.x
        self.y -= v.y
        return self
    
    def get(self):
        return (self.x, self.y)
        
    def set(self, x, y):
        self.x = x
        self.y = y
    
def load_sound(name):
    if pygame.mixer.get_init == None:
        print 'Mixer is not initialized, load aborted.'
        return None
    try:
        sound = pygame.mixer.Sound(name)
        #sound = pygame.mixer.music.load(name)
    except pygame.error, message:
        print 'Cannot load sound'
        raise message
    return sound
        
        
def load_sprite(filename):
    image = pygame.image.load(filename)
    sprite = pygame.sprite.Sprite()
    sprite.image = image
    sprite.rect = image.get_rect()
    return sprite

