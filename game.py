import sys, pygame

class Game:
    def __init__(self, size):
        self.is_running = True
        
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface() 
        pygame.display.set_caption("Epic Adventure")


    def run(self):
        while self.is_running:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    
            # update game
                    
            
            # swap buffers
            pygame.display.flip()
            
if __name__ == '__main__':
    g = Game((320, 240))
    g.run()