#!/usr/bin/env python
import pygame
import gameobject
import util

class Player(gameobject.GameObject):
    def __init__(self, pos):
        self.pos = pos
        self.bw_image = pygame.image.load("data/bw_player16.png")
        self.red_image = pygame.image.load("data/red_player16.png")
        self.green_image = pygame.image.load("data/green_player16.png")
        self.blue_image = pygame.image.load("data/blue_player16.png")
        #gameobject.GameObject.__init__(self, pos, util.load_sprite("data/blue_block16.png"))
    
    def update(self):
        pass
    
    def draw(self, canvas):
        #gameobject.GameObject.draw(self, canvas)
        canvas.blit(self.red_image, self.pos, None, pygame.BLEND_MAX)
        
        # allways show "body"
        canvas.blit(self.bw_image, self.pos, None, pygame.BLEND_MAX)
