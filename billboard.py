#!/usr/bin/env python
import util
import pygame
import gameobject
import animation

class GuiTimerBar():
    def __init__(self,pos,finish_time,time_until_play = 0.0):
        self.map_time = finish_time
        self.draw_pos = pos
        self.empty_timer = util.load_image("data/timer_empty0.png")
        self.blue_timer = util.load_image("data/timer_blue0.png")
        self.green_timer = util.load_image("data/timer_green0.png")
        self.red_timer = util.load_image("data/timer_red0.png")
        self.stopwatch = util.load_image("data/stopwatch0.png")
        
        self.red_animation = animation.new_animation("data/timer_red","png",1,8,[0,1])
        
        self.timer_finish = finish_time
        self.time_until_finish = self.map_time
        self.time_until_play = time_until_play
        self.timer_on = True
        self.has_stopped = False
        self.rect = self.empty_timer.get_rect()
        self.wait_until_play = False
        
    def start(self):
        self.timer_on = True
        self.time_until_finish = self.map_time
        
    def stop(self):
        self.timer_on = False
        self.has_stopped = True
        
    def reset(self,time_until_play = 0.0, play = True):
        self.has_stopped = False
        
        if time_until_play > 0.0:
            self.wait_until_play = True
            self.time_until_play = time_until_play
        
        if play:
            self.start()
        
    def update(self,dt):
        if self.timer_on:
            if self.wait_until_play:
                if self.time_until_play <= 0:
                    self.wait_until_play = False
                else:
                    self.time_until_play -= dt * 0.001
            else:
                if self.time_until_finish <= 0:
                    self.timer_on = False
                    self.has_stopped = True
                else:
                    if self.time_until_finish <= 0.25*self.map_time:
                        self.red_animation.update(dt)
                    self.time_until_finish -= dt*0.001
    
    def draw(self,canvas):
        # third param = blit rect or whatever
        draw_rect = self.rect.copy()
        draw_rect.width -= draw_rect.width * (1-(self.time_until_finish/self.map_time))
        canvas.blit(self.empty_timer, self.draw_pos.get(), None)
        canvas.blit(self.stopwatch, (self.draw_pos.x+self.rect.width,self.draw_pos.y), None)
        
        if (self.time_until_finish <= 0.7*self.map_time) and (self.time_until_finish >= 0.25*self.map_time):
            canvas.blit(self.green_timer, self.draw_pos.get(), draw_rect)
        elif self.time_until_finish <= 0.25*self.map_time:
            self.red_animation.play()
            self.red_animation.draw(canvas,self.draw_pos.get(),True,draw_rect)
        else:
            canvas.blit(self.blue_timer, self.draw_pos.get(), draw_rect)
            
        
            
        
        

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
    def __init__(self,name,pos,speed,repeat = False,animated = False,blend = False):
        self.image = util.load_image(name)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.is_animated = animated
        self.pos = pos
        self.draw_pos = util.vec2(0,0)
        self.speed = speed
        self.inv_speed = speed/100.
        self.repeat = repeat
        self.offset = 320
        self.last_frame_pos = 0
        self.blend = blend

    def draw(self,canvas):
        if not self.is_animated:
            if self.repeat:
                if self.draw_pos.x < -320:
                    self.draw_pos.x += 320

                for x in range(0, 6):
                    if self.blend:
                        canvas.blit(self.image, (-1000 + self.draw_pos.x + 320*x,self.draw_pos.y), None,pygame.BLEND_MAX)
                    else:
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
                         self.pos.y-cam_pos.y*self.inv_speed*0.2)

        self.draw_pos.x * dt
        self.draw_pos.y * dt

        self.draw_pos.set(int(self.draw_pos.x),int(self.draw_pos.y))
        
        if self.draw_pos.y <= 240-self.height:
            self.draw_pos.y = self.pos.y
        
        #print self.pos.y,self.draw_pos.y,self.height

        #print self.draw_pos

        outside = self.outside(self.draw_pos)


    def outside(self,pos):
        if pos.x < -self.width:
            return True
        if pos.x > self.width:
            return True
