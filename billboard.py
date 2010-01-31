#!/usr/bin/env python
import util
import pygame
import gameobject

class GuiKeys():
    def __init__(self,pos,offset = 16):
        #load imgs
        self._default = util.load_image("data/bw_key0.png")
        self._red = util.load_image("data/red_key0.png")
        self._green = util.load_image("data/green_key0.png")
        self._blue = util.load_image("data/blue_key0.png")

        self.red = self._default
        self.green = self._default
        self.blue = self._default

        self.offset = offset
        self.draw_pos = pos

    def draw(self,canvas):
        # draw keys at relative positions
        canvas.blit(self.red, self.draw_pos.get(), None)
        canvas.blit(self.green, (self.draw_pos.x+self.offset,self.draw_pos.y), None)
        canvas.blit(self.blue, (self.draw_pos.x+self.offset*2,self.draw_pos.y), None)

    def update(self,toggle_key):
        # only call update when a key has been picked up
        if toggle_key == gameobject.OBJECT_TYPE_KEY_RED:
            self.red = self._red
        elif toggle_key == gameobject.OBJECT_TYPE_KEY_GREEN:
            self.green = self._green
        elif toggle_key == gameobject.OBJECT_TYPE_KEY_BLUE:
            self.blue = self._blue
        else:
            print "unknown key type"

    def reset(self):
        self.red = self._default
        self.green = self._default
        self.blue = self._default

class Billboard:
    def __init__(self,name,pos,speed,repeat = False,animated = False):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.is_animated = animated
        self.pos = pos
        self.draw_pos = util.vec2(0,0)
        self.speed = speed
        self.inv_speed = speed/40.
        self.repeat = repeat
        self.offset = 320
        self.last_frame_pos = 0

    def draw(self,canvas):
        if not self.is_animated:
            if self.repeat:
                if self.draw_pos.x < -320:
                    self.draw_pos.x += 320

                for x in range(0, 6):
                    canvas.blit(self.image, (-1000 + self.draw_pos.x + 320*x,self.draw_pos.y), None)


                """
                if self.outside(self.draw_pos):
                    self.draw_pos.x -= 320
                    canvas.blit(self.image, (self.draw_pos.x,self.draw_pos.y), None)
                    #canvas.blit(self.image, (self.draw_pos.x,self.draw_pos.y), None)
                    print self.draw_pos.get()
                else:
                    canvas.blit(self.image, (self.draw_pos.x,self.draw_pos.y), None)
                    #canvas.blit(self.image, (self.draw_pos.x,self.draw_pos.y), None)
                """
                #canvas.blit(self.image, self.draw_pos.get(), None)
                #canvas.blit(self.image, (self.draw_pos.x+self.offset,self.draw_pos.y), None)
        pass

    def update(self,cam_pos,dt):
        self.draw_pos.set(self.pos.x-cam_pos.x*self.inv_speed,
                         self.pos.y-cam_pos.y*self.inv_speed)

        self.draw_pos.x * dt
        self.draw_pos.y * dt

        self.draw_pos.set(int(self.draw_pos.x),self.pos.y)

        #print self.draw_pos

        outside = self.outside(self.draw_pos)


    def outside(self,pos):
        if pos.x < -self.width:
            return True
        if pos.x > self.width:
            return True
