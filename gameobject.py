#!/usr/bin/env python
import pygame
import util

class GameObject:
    def __init__(self, pos, sprite):
        self.dir = util.vec2(0, 0) # direction
        self.vel = util.vec2(0, 0) # velocity in pixels/frame
        self.delta_move = util.vec2(0, 0)
        self.draw_pos = util.vec2(0, 0)
        self.sprite = sprite
        self.move(pos.x, pos.y)

    def move(self, x, y):
       # self.sprite.rect.move_ip(x, y)
       self.delta_move.x += x
       self.delta_move.y += y

    def update(self):
        pass

    def draw(self, canvas):
        #canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_MAX)
        canvas.blit(self.sprite.image, self.sprite.rect, None, pygame.BLEND_MAX)

class StaticBlock(GameObject):
    def __init__(self, pos, sprite):
        GameObject.__init__(self, pos, sprite)

    def update(self,camera_pos):
        GameObject.update(self)
#        self.draw_pos.set(self.pos.x - camera_pos.x, self.pos.y - camera_pos.y)
        pass