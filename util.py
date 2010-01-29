#!/usr/bin/env python
import pygame.mixer
#import os.path


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
        

