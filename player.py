#!/usr/bin/env python
import pygame
import gameobject
import util

class Player(gameobject.GameObject):
    def __init__(self, pos):
        self.pos = pos
        self.look_dir = 0 # 0 = right, 1 = left
        self.bw_image = pygame.image.load("data/bw_player16.png")
        self.red_image = pygame.image.load("data/red_player16.png")
        self.green_image = pygame.image.load("data/green_player16.png")
        self.blue_image = pygame.image.load("data/blue_player16.png")

        self.bw_image_r = pygame.image.load("data/bw_player16_r.png")
        self.red_image_r = pygame.image.load("data/red_player16_r.png")
        self.green_image_r = pygame.image.load("data/green_player16_r.png")
        self.blue_image_r = pygame.image.load("data/blue_player16_r.png")
        #gameobject.GameObject.__init__(self, pos, util.load_sprite("data/blue_block16.png"))

    def update(self):
        pass

    def draw(self, canvas):
        if (self.look_dir == 0):
            # looking right
            # find correct color
            body_image = self.bw_image
            cloth_image = self.red_image
        else:
            # looking left
            # find correct color
            body_image = self.bw_image_r
            cloth_image = self.red_image_r

        #gameobject.GameObject.draw(self, canvas)
        canvas.blit(cloth_image, self.pos.get(), None, pygame.BLEND_MAX)

        # allways show "body"
        canvas.blit(body_image, self.pos.get(), None, pygame.BLEND_MAX)
