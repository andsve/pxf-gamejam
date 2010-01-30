import sys, pygame
from pygame.locals import *

import player
import stage
import gameobject
import util
import camera
import animation
import billboard

import pymunk as pm
# lol enums
CNONE,CRED,CBLUE,CGREEN = range(4)
PDIR_RIGHT,PDIR_LEFT = range(2)

vel_epsilon = 0.05

class Game:
    def __init__(self, size):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        self.is_running = True

        # physics
        pm.init_pymunk()
        self.space = pm.Space() #3
        self.space.gravity = (0.0, 300.0)
        self.space.resize_static_hash()
        self.space.resize_active_hash()

        # collisions between different colors
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_RED, gameobject.OBJECT_TYPE_GREEN, None)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_GREEN, gameobject.OBJECT_TYPE_RED, None)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_GREEN, gameobject.OBJECT_TYPE_BLUE, None)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_BLUE, gameobject.OBJECT_TYPE_GREEN, None)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_RED, gameobject.OBJECT_TYPE_BLUE, None)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_BLUE, gameobject.OBJECT_TYPE_RED, None)

        # collisions between
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_PLAYER, gameobject.OBJECT_TYPE_RED, self.handle_collision, self.screen)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_PLAYER, gameobject.OBJECT_TYPE_GREEN, self.handle_collision, self.screen)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_PLAYER, gameobject.OBJECT_TYPE_BLUE, self.handle_collision, self.screen)
        self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_PLAYER, gameobject.OBJECT_TYPE_BW, self.handle_collision, self.screen)
        #self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_RED, gameobject.OBJECT_TYPE_PLAYER, self.handle_collision, self.screen)
        #self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_GREEN, gameobject.OBJECT_TYPE_PLAYER, self.handle_collision, self.screen)
        #self.space.add_collisionpair_func(gameobject.OBJECT_TYPE_BLUE, gameobject.OBJECT_TYPE_PLAYER, self.handle_collision, self.screen)


        # music:
        self.bg_music = util.load_sound("data/channel_panic!-theme.ogg")
        self.bg_music_playing = False

        # game settings
        self.player = player.Player(util.vec2(100,20), self.space)
        #print(self.player.object_type)
        self.camera = camera.Camera(util.vec2(30,25),size)
        self.current_stage = None
        # set color key to black
        #self.screen.set_colorkey(pygame.Color(0,0,0))
        pygame.key.set_repeat(1, 20)

        self.active_color = CRED


    def handle_collision(self, shapea, shapeb, contacts, normal_coef, surface):
        #self.player.in_air = False
        for c in contacts:
            in_air = True
            if (c.normal.y > 0 and c.normal.x < 0.1 and c.normal.x > -0.1):
                in_air = False

            if (shapea.collision_type == gameobject.OBJECT_TYPE_BW or shapeb.collision_type == gameobject.OBJECT_TYPE_BW):
                self.player.in_air = in_air
                return True;

            if (self.active_color == CRED):
                if (shapea.collision_type == gameobject.OBJECT_TYPE_RED or shapeb.collision_type == gameobject.OBJECT_TYPE_RED):
                    self.player.in_air = in_air
                    return True;
            elif (self.active_color == CGREEN):
                if (shapea.collision_type == gameobject.OBJECT_TYPE_GREEN or shapeb.collision_type == gameobject.OBJECT_TYPE_GREEN):
                    self.player.in_air = in_air
                    return True;
            elif (self.active_color == CBLUE):
                if (shapea.collision_type == gameobject.OBJECT_TYPE_BLUE or shapeb.collision_type == gameobject.OBJECT_TYPE_BLUE):
                    self.player.in_air = in_air
                    return True;

        return False

    def update_title(self):
        pygame.display.set_caption("Channel Panic! (%.2f FPS)" % (self.clock.get_fps()))

    def set_level(self, stage):
        self.current_stage = stage

    def handle_input(self, event):
        if event.type == KEYUP and event.key in (K_LEFT, K_RIGHT):
            self.player.stop_hammer_time = True

        #switch colors
        if event.key == K_1:
            self.active_color = self.player.toggle_color(CRED)
        if event.key == K_2:
            self.active_color = self.player.toggle_color(CGREEN)
        if event.key == K_3:
            self.active_color = self.player.toggle_color(CBLUE)

        if event.key == K_RETURN:
            self.anim_test.play_animation()

    def game_input(self):
        if pygame.key.get_pressed()[K_UP]:
            #self.player.vel.y = -3
            #self.in_air = True
            if (not self.player.in_air):
                self.player.body.apply_impulse((0,-1080))
            pass

        if pygame.key.get_pressed()[K_LEFT]:
                self.player.stop_hammer_time = False
            #if (len(self.physics.get_colliding_objects(self.physics.player)) > 0):
                self.player.look_dir = 1
                self.player.has_changed = True
                #if (-self.player.body._get_velocity().x < 80.0):
                if (self.player.in_air):
                    self.player.body.apply_impulse((-50,0))
                else:
                    self.player.body.apply_impulse((-100,0)) #_set_velocity((-80, 0))
                #self.player.vel.y = 0.04

        if pygame.key.get_pressed()[K_RIGHT]:
                self.player.stop_hammer_time = False
            #if (len(self.physics.get_colliding_objects(self.physics.player)) > 0)
                self.player.look_dir = 0
                self.player.has_changed = True
                if (self.player.in_air):
                    self.player.body.apply_impulse((50,0))
                else:
                    self.player.body.apply_impulse((100,0)) #_set_velocity((-80, 0))
                #self.player.vel.x += 0.9
                #self.player.vel.y = 0.04

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
        self.set_level(stage.Stage1(self.camera, self.space))

        while self.is_running:
            # update time
            self.dt_last_frame = self.clock.tick(60)

            # event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.is_running = False
                elif event.type in (KEYDOWN, KEYUP):
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
            self.space.step(1/60.0)

            # update game objects
            for object in self.current_stage.tiles:
                #object.update(self.camera.pos)
                object.update(self.camera.get_pos())

            # update camera
            self.camera.set_lookat(util.vec2(self.player.body.position.x, self.player.body.position.y))
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
