#!/usr/bin/env python
import pygame
import gameobject
import util
import animation
import game
import pymunk as pm

"""def create_ball(self, pos, mass=1.0, radius=8.0):
    moment = pm.moment_for_circle(mass, radius, 0.0, pm.Vec2d(0,0))
    ball_body = pm.Body(mass, moment)
    ball_body.position = pm.Vec2d(pos)
    ball_shape = pm.Circle(ball_body, radius, pm.Vec2d(0,0))
    ball_shape.friction = 1.5
    #ball_shape.collision_type = COLLTYPE_DEFAULT
    #self.space.add(ball_body, ball_shape)
    # return ball_shape
    return ball_body, ball_shape"""

class Player(gameobject.GameObject):
    def __init__(self, pos, space):
        gameobject.GameObject.__init__(self, pos, util.to_sprite(util.load_image("data/bw_player16.png")), space, gameobject.OBJECT_TYPE_PLAYER, 10.0)
        self.body, self.shape = gameobject.create_ball(space, (pos.x, pos.y), 8, 8)
        space.add(self.body, self.shape)
        self.shape.collision_type = gameobject.OBJECT_TYPE_PLAYER
        #self.shape.collision_type = gameobject.OBJECT_TYPE_PLAYER

        #self.image = pygame.image.load("data/bw_guy_walk0.png")
        self.animations = {}
        self.active_color = game.CBLUE
        #create animations
        animation_freq = 4
        bw_player_walk_left = animation.new_animation("data/bw_guy_walk","png",1,animation_freq,[0,1])
        bw_player_walk_right = animation.new_animation("data/bw_guy_walk_r","png",1,animation_freq,[0,1])

        red_player_walk_left = animation.new_animation("data/red_guy_walk","png",1,animation_freq,[0,1])
        red_player_walk_right = animation.new_animation("data/red_guy_walk_r","png",1,animation_freq,[0,1])

        green_player_walk_left = animation.new_animation("data/green_guy_walk","png",1,animation_freq,[0,1])
        green_player_walk_right = animation.new_animation("data/green_guy_walk_r","png",1,animation_freq,[0,1])

        blue_player_walk_left = animation.new_animation("data/blue_guy_walk","png",1,animation_freq,[0,1])
        blue_player_walk_right = animation.new_animation("data/blue_guy_walk_r","png",1,animation_freq,[0,1])

        #player_walk_left.play()
        self.image = bw_player_walk_left.sprite.image

        self.animations["bw_player_walk_left"] = bw_player_walk_left
        self.animations["bw_player_walk_right"] = bw_player_walk_right

        self.animations["red_player_walk_left"] = red_player_walk_left
        self.animations["red_player_walk_right"] = red_player_walk_right

        self.animations["green_player_walk_left"] = green_player_walk_left
        self.animations["green_player_walk_right"] = green_player_walk_right

        self.animations["blue_player_walk_left"] = blue_player_walk_left
        self.animations["blue_player_walk_right"] = blue_player_walk_right

        self.current_animation = red_player_walk_left
        self.look_dir = game.PDIR_LEFT
        self.active_color = game.CRED
        self.has_changed = True

    def update(self, camera_pos,dt):
        gameobject.GameObject.update(self, camera_pos)
        self.in_air = True
        for anim in self.animations.keys():
           self.animations[anim].update(dt)
        self.current_animation.update(dt)

    # move this elsewhere
    def toggle_color(self,color):
        self.active_color = color
        self.has_changed  = True
        return color

    def determine_lookdir(self,color_str):
        # right
        if self.look_dir == game.PDIR_RIGHT:
            return color_str + "_player_walk_right"
        else:
            return color_str + "_player_walk_left"

    def set_animation(self):
        vel = self.body._get_velocity()
        _play = True

        if abs(vel.x) <= game.vel_epsilon:
            if not self.has_changed:
                self.current_animation.stop()
            _play = False

        if self.has_changed:
            new_animation = None

            if self.active_color == game.CNONE:
                new_animation = self.animations[self.determine_lookdir("bw")]
            elif self.active_color == game.CRED:
                new_animation = self.animations[self.determine_lookdir("red")]
            elif self.active_color == game.CGREEN:
                new_animation = self.animations[self.determine_lookdir("green")]
            elif self.active_color == game.CBLUE:
                new_animation = self.animations[self.determine_lookdir("blue")]


            self.current_animation = new_animation

            if _play:
                self.current_animation.play()
            self.has_changed = False



    def draw(self, canvas):

        self.set_animation()

        #gameobject.GameObject.draw(self, canvas)
        #canvas.blit(cloth_image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #self.current_animation.draw(canvas,self.draw_pos.get())
        canvas.blit(self.current_animation.sprite.image, self.draw_pos.get(), None, pygame.BLEND_MAX)

        # allways show "body"
        #canvas.blit(body_image, self.draw_pos.get(), None, pygame.BLEND_RGB_ADD)
