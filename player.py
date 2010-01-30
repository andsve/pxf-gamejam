#!/usr/bin/env python
import pygame
import gameobject
import util

class AnimatedGameObject(gameobject.GameObject):
    def __init__(self,pos,frames,freq):
        self.pos = pos
        self.current = 0
        self.playing = False
        self.frames = frames
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = frames[0]
        self.sprite.rect = self.sprite.image.get_rect()
        # timing:
        self._next_update = 0
        self._period = 1000./freq
        self._inv_period = freq/1000
        self._start_time = 0
        self._frames_len = len(self.frames)
        self._paused_time = 0

    def update(self, t):
        if self.playing:
            self._next_update += t
            if self._next_update >= self._period:
                self.current += int(self._next_update/self._period)
                self._next_update %= self._period
                self.current %= len(self.frames)
                self.sprite.image = self.frames[self.current]
                self.sprite.rect = self.sprite.image.get_rect(center=self.sprite.rect.center)

    def draw(self,canvas):
        canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_MAX)

    def play(self):
        if self.playing:
            self.playing = False
        else:
            self.current = 0
            self.playing = True

    def stop(self):
        self.current = 0
        self.playing = False

    def pause(self):
        pass

class Player(gameobject.GameObject):
    def __init__(self, pos):
        gameobject.GameObject.__init__(self, pos, util.to_sprite(util.load_image("data/bw_player16.png")))
        self.look_dir = 0 # 0 = right, 1 = left
        self.bw_image = pygame.image.load("data/bw_player16.png")
        self.red_image = pygame.image.load("data/red_player16.png")
        self.green_image = pygame.image.load("data/green_player16.png")
        self.blue_image = pygame.image.load("data/blue_player16.png")

        self.bw_image_r = pygame.image.load("data/bw_player16_r.png")
        self.red_image_r = pygame.image.load("data/red_player16_r.png")
        self.green_image_r = pygame.image.load("data/green_player16_r.png")
        self.blue_image_r = pygame.image.load("data/blue_player16_r.png")

    def update(self, camera_pos):
        gameobject.GameObject.update(self, camera_pos)

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
        canvas.blit(cloth_image, self.draw_pos.get(), None, pygame.BLEND_MAX)

        # allways show "body"
        canvas.blit(body_image, self.draw_pos.get(), None, pygame.BLEND_RGB_ADD)
