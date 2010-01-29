import sys, pygame

import player
import stage
import gameobject

class Game:
    def __init__(self, size):       
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.is_running = True

    def update_title(self):
        pygame.display.set_caption("Epic Adventure (%.2f FPS)" % (self.clock.get_fps()))

    def run(self):
        while self.is_running:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    
            # update game
            
            
            # fps limit
            self.clock.tick(60)
            self.update_title()
            # swap buffers
            pygame.display.flip()
            
if __name__ == '__main__':
    g = Game((320, 240))
    g.run()