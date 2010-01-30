import sys, pygame
from pygame.locals import *

import player
import stage
import gameobject
import util
import camera
import physics
import animation

# lol enums
CNONE,CRED,CBLUE,CGREEN = range(4)
PDIR_RIGHT,PDIR_LEFT = range(2)

class Game:
    def __init__(self, size):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        # load assets
        # music:
        self.bg_music = util.load_sound("data/channel_panic!-theme.ogg")
        self.bg_music_playing = False
        
        # game settings
        self.active_color = CNONE
        self.player = player.Player(util.vec2(4,25))
        self.camera = camera.Camera(util.vec2(2,25),size)
        self.current_stage = None
        self.physics = physics.Physics()
        # set color key to black
        #self.screen.set_colorkey(pygame.Color(0,0,0))
        pygame.key.set_repeat(1, 20)

    def update_title(self):
        pygame.display.set_caption("Channel Panic! (%.2f FPS)" % (self.clock.get_fps()))

    def set_level(self, stage):
        self.physics.reset()
        self.current_stage = stage

        for o in self.current_stage.game_objects:
            self.physics.add_dynamic(o)

        for o in self.current_stage.tiles:
            self.physics.add_static(o)

        self.physics.add_player(self.player)

    def handle_input(self, event):
        #switch colors
        if event.key == K_1:
            self.player.toggle_color(CRED)
        if event.key == K_2:
            self.player.toggle_color(CGREEN)
        if event.key == K_3:
            self.player.toggle_color(CBLUE)
        
        if event.key == K_RETURN:
            self.anim_test.play_animation()
            
    def game_input(self):        
        if pygame.key.get_pressed()[K_UP]:
            self.player.vel.y = -3
            self.in_air = True

        if pygame.key.get_pressed()[K_LEFT]:
            self.player.look_dir = 1
            self.player.vel.x -= 0.9
            self.player.vel.y = 0.04

        if pygame.key.get_pressed()[K_RIGHT]:
            self.player.look_dir = 0
            self.player.vel.x += 0.9
            self.player.vel.y = 0.04

        if pygame.key.get_pressed()[K_SPACE]:
            if self.bg_music_playing:
                self.bg_music.stop()
                self.bg_music_playing = False
            else:
                self.bg_music.play(1)
                self.bg_music_playing = True

        if pygame.key.get_pressed()[K_ESCAPE]:
            self.is_running = False


    def run(self):
        self.set_level(stage.Stage1(self.camera))

        while self.is_running:
            # update time
            self.dt_last_frame = self.clock.tick(25)

            # event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.is_running = False
                elif event.type == KEYDOWN:
                    self.handle_input(event)

            # handle game input
            self.game_input()

            self.screen.fill([0,0,0])

            # update animation
            #self.anim_test.update(self.dt_last_frame)
            #self.anim_test.draw(self.screen)

            # update player
            self.player.update(self.camera.get_pos(),self.dt_last_frame)
            self.player.draw(self.screen)

            # update physics
            self.physics.step()

            # update game objects
            for object in self.current_stage.tiles:
                #object.update(self.camera.pos)
                object.update(self.camera.get_pos())

            # update camera
            self.camera.set_lookat(util.vec2(self.player.sprite.rect.left, self.player.sprite.rect.right))
            self.camera.update()

            # update game
            self.current_stage.draw(self.screen)

            # fps limit
            #3self.clock.tick(25)
            self.update_title()
            # swap buffers
            pygame.display.flip()

if __name__ == '__main__':
    g = Game((320, 240))
    g.run()
