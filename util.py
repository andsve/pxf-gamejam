#!/usr/bin/env python
import pygame.mixer
import pygame
import animatedsprite
#import os.path

class vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

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
