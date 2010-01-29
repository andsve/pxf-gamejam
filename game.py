import sys, pygame
from pygame.locals import *

import player
import stage
import gameobject
import util
import camera

class Game:
    def __init__(self, size):       
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.bg_music = util.load_sound("data/Test.ogg")
        self.current_stage = stage.Stage1()
        #self.player = Player()
        #self.camera = Camera(self.player.pos)

    def update_title(self):
        pygame.display.set_caption("Epic Adventure (%.2f FPS)" % (self.clock.get_fps()))

    def handle_input(self, event):
        if event.key == K_SPACE:
            self.bg_music.play()
        if event.key == K_ESCAPE:
            self.is_running = False

    def run(self):
        while self.is_running:
            # event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.is_running = False
                elif event.type == KEYDOWN:
                    self.handle_input(event)
                    
            # update game
            self.current_stage.draw(self.screen,(0,0))
            
            # fps limit
            self.clock.tick(60)
            self.update_title()
            # swap buffers
            pygame.display.flip()
            
if __name__ == '__main__':
    g = Game((320, 240))
    g.run()