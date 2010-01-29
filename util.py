#!/usr/bin/env python
import pygame.mixer
#import os.path


def load_sound(name):
    try:
        print 'poop'
        sound = pygame.mixer.Sound(name)
    except pygame.error, message:
        print 'Cannot load sound'
        raise message
    return sound
        

