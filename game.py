import sys, pygame
from pygame.locals import *

import player
import stage
import gameobject
import util
import camera
import physics

class Game:
    def __init__(self, size):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        self.is_running = True
        # music:
        self.bg_music = util.load_sound("data/channel_panic!-theme.ogg")
        self.bg_music_playing = False

        # load assets
        # anim test
        test = util.name_sequence("data/anim_test","png",4)
        seq = util.get_sequence(test,[0,1,2,3,4])
        self.dt_last_frame = self.clock.tick()

        self.anim_test = player.AnimatedGameObject(util.vec2(50,0),seq,5)
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

        self.physics.add_dynamic(self.player)

    def handle_input(self, event):
        if event.key == K_UP:
            self.player.vel.y = -3

        if event.key == K_LEFT:
            self.player.look_dir = 1
            self.player.move(-1.0, 0)

        if event.key == K_RIGHT:
            self.player.look_dir = 0
            self.player.move(1.0, 0)

        if event.key == K_RETURN:
            self.anim_test.play()

            #pass
        if event.key == K_SPACE:
            if not self.bg_music_playing:
                self.bg_music.play(1)
                self.bg_music_playing = True
            else:
                self.bg_music.stop()
                self.bg_music_playing = False
        if event.key == K_ESCAPE:
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

            self.screen.fill([0,0,0])

            # update animation
            self.anim_test.update(self.dt_last_frame)
            self.anim_test.draw(self.screen)

            # update player
            self.player.update(self.camera.get_pos())
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
