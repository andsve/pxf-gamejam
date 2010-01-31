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
        self.body, self.shape = gameobject.create_ball(space, (pos.x, pos.y), 8, 6)
        space.add(self.body, self.shape)
        self.shape.collision_type = gameobject.OBJECT_TYPE_PLAYER
        #self.shape.collision_type = gameobject.OBJECT_TYPE_PLAYER
        self.stop_hammer_time = False
        self.in_air = True
        self.is_pushing = False

        self.animations = {}
        self.active_color = game.CBLUE
        
        #load animations
        animation_freq = 4
        
        red_player_push_left = animation.new_animation("data/red_guy_push","png",1,animation_freq,[0,1])
        red_player_push_right = animation.new_animation("data/red_guy_push_r","png",1,animation_freq,[0,1])
        
        red_player_walk_left = animation.new_animation("data/red_guy_walk","png",1,animation_freq,[0,1])
        red_player_walk_right = animation.new_animation("data/red_guy_walk_r","png",1,animation_freq,[0,1])

        green_player_walk_left = animation.new_animation("data/green_guy_walk","png",1,animation_freq,[0,1])
        green_player_walk_right = animation.new_animation("data/green_guy_walk_r","png",1,animation_freq,[0,1])
        
        green_player_push_left = animation.new_animation("data/green_guy_push","png",1,animation_freq,[0,1])
        green_player_push_right = animation.new_animation("data/green_guy_push_r","png",1,animation_freq,[0,1])

        blue_player_walk_left = animation.new_animation("data/blue_guy_walk","png",1,animation_freq,[0,1])
        blue_player_walk_right = animation.new_animation("data/blue_guy_walk_r","png",1,animation_freq,[0,1])
        
        blue_player_push_left = animation.new_animation("data/blue_guy_push","png",1,animation_freq,[0,1])
        blue_player_push_right = animation.new_animation("data/blue_guy_push_r","png",1,animation_freq,[0,1])

        #player_walk_left.play()
        self.image = None
        
        # red player animations:
        self.animations["red_player_walk_left"] = red_player_walk_left
        self.animations["red_player_walk_right"] = red_player_walk_right
        
        self.animations["red_player_push_left"] = red_player_push_left
        self.animations["red_player_push_right"] = red_player_push_right

        # green player animations:
        self.animations["green_player_walk_left"] = green_player_walk_left
        self.animations["green_player_walk_right"] = green_player_walk_right
        
        self.animations["green_player_push_left"] = green_player_push_left
        self.animations["green_player_push_right"] = green_player_push_right

        # blue player animations:
        self.animations["blue_player_walk_left"] = blue_player_walk_left
        self.animations["blue_player_walk_right"] = blue_player_walk_right
        
        self.animations["blue_player_push_left"] = blue_player_push_left
        self.animations["blue_player_push_right"] = blue_player_push_right

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

        if self.stop_hammer_time:
            if -1.5 < self.body.velocity.x < 1.5:
                self.body.velocity.x = 0
            elif self.body.velocity.x > 0:
                aoeu = 4
                self.body.velocity.x -= aoeu
            elif self.body.velocity.x < 0:
                aoeu = 4
                self.body.velocity.x += aoeu
        else:
            max_speed = 160
            if self.body.velocity.x > max_speed:
                self.body.velocity.x = max_speed
            elif self.body.velocity.x < -max_speed:
                self.body.velocity.x = -max_speed


    # move this elsewhere
    def toggle_color(self,color):
        self.active_color = color
        self.has_changed  = True
        return color

    def determine_lookdir(self,color_str,action_str):
        # right
        if self.look_dir == game.PDIR_RIGHT:
            return color_str + "_player_" + action_str + "_right"
        else:
            return color_str + "_player_" + action_str + "_left"

    def set_animation(self):
        vel = self.body._get_velocity()
        _play = True

        if abs(vel.x) <= game.vel_epsilon:
            if not self.has_changed:
                self.current_animation.stop()
            _play = False
        
        if abs(vel.x) <= game.vel_epsilon:
            self.current_animation.stop()
            
        action = ""
        if self.is_pushing:
            action = "push"
        else:
            action = "walk"

        if self.has_changed:
            new_animation = None

            if self.active_color == game.CNONE:
                new_animation = self.animations[self.determine_lookdir("bw","walk")]
            elif self.active_color == game.CRED:
                    new_animation = self.animations[self.determine_lookdir("red",action)]
            elif self.active_color == game.CGREEN:                
                new_animation = self.animations[self.determine_lookdir("green",action)]
            elif self.active_color == game.CBLUE:
                new_animation = self.animations[self.determine_lookdir("blue",action)]

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
        pos = self.draw_pos.get()
        canvas.blit(self.current_animation.sprite.image, (pos[0], pos[1]-2), None, pygame.BLEND_MAX)

        # allways show "body"
        #canvas.blit(body_image, self.draw_pos.get(), None, pygame.BLEND_RGB_ADD)
