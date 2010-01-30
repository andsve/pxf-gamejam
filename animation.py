#!/usr/bin/env python
import pygame
import util

class Animation():
    def __init__(self,frames,freq):
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
                self.current += 1
                self._next_update %= self._period
                self.current %= len(self.frames)
                self.sprite.image = self.frames[self.current]
                self.sprite.rect = self.sprite.image.get_rect(center=self.sprite.rect.center)
                #self.current += int(self._next_update/self._period)

    def draw(self,canvas,pos):
        canvas.blit(self.sprite.image, pos, None, pygame.BLEND_MAX)
        pass
        
    def play(self):
        #self.current = 0
        self.playing = True
    
    def stop(self):
        self.current = 0
        self.playing = False
    
    def pause(self):
        pass
    
def new_animation(basename, ext, num, freq, sequence, num_digits=1, offset=0):
    frame_names = util.name_sequence(basename,ext,num,num_digits,offset)
    frames = util.get_sequence(frame_names,sequence)
    return Animation(frames,freq)
