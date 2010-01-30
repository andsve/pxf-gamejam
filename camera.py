#!/usr/bin/env python
from pygame import Rect
import util
import math

class Camera:
    def __init__(self,pos,size):
        self.real_pos = util.vec2(pos.x, pos.y)
        self.lookat_pos = util.vec2(pos.x, pos.y)
        self.center = util.vec2(size[0] / 2.0, size[1] / 2.0)
        self.rect = Rect((0,0),size)
        self.delta_threshold = 0.5

    def update(self):
        delta = util.vec2(self.lookat_pos.x - self.real_pos.x, self.lookat_pos.y - self.real_pos.y)
        if (delta.x > self.center.x * self.delta_threshold):
            self.real_pos = util.vec2(self.real_pos.x + 3.0, self.real_pos.y)#util.vec2(self.lookat_pos.x + 1.0, self.lookat_pos.y)
        elif (-delta.x > self.center.x * self.delta_threshold):
            self.real_pos = util.vec2(self.real_pos.x - 3.0, self.real_pos.y)

        """delta = util.vec2(self.lookat_pos.x - self.real_pos.x, self.lookat_pos.y - self.real_pos.y)
        amount = math.sqrt(delta.x * delta.x + delta.y * delta.y)
        if (amount > 1.0 and amount < -1.0):
            self.real_pos = util.vec2(self.real_pos.x + delta.x / 2.0, self.real_pos.y + delta.y / 2.0)"""

    def set_lookat(self, pos):
        self.lookat_pos = util.vec2(pos.x, pos.y)

    def get_pos(self):
        return util.vec2(self.real_pos.x - self.center.x, self.real_pos.y - self.center.y)
