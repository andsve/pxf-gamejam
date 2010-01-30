#!/usr/bin/env python
import pygame
import gameobject
import util
import animation
import game

class Player(gameobject.GameObject):
    def __init__(self, pos, space):
        gameobject.GameObject.__init__(self, pos, util.to_sprite(util.load_image("data/bw_player16.png")), space, 10.0)
        space.add(self.body, self.shape)
        self.shape.collision_type = 2

        #self.image = pygame.image.load("data/bw_guy_walk0.png")
        self.animations = {}
        self.active_color = game.CNONE
        #create animations        animation_freq = 8
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
        
        self.current_animation = bw_player_walk_left
        self.look_dir = game.PDIR_LEFT

    def update(self, camera_pos,dt):
        gameobject.GameObject.update(self, camera_pos)
        self.in_air = True
        #for anim in self.animations.keys():
        #   self.animations[anim].update(dt)
        self.current_animation.update(dt)
    def toggle_color(self,color):        self.current_animation.stop()
        if self.active_color == color:
            self.active_color = game.CNONE
            self.current_animation = self.animations[self.determine_lookdir("bw")]
        else:
            self.active_color = color

            if color == game.CRED:
                self.current_animation = self.animations[self.determine_lookdir("red")]
            elif color == game.CGREEN:
                self.current_animation = self.animations[self.determine_lookdir("green")]
            elif color == game.CBLUE:
                self.current_animation = self.animations[self.determine_lookdir("blue")]
        self.current_animation.play()
    
    def determine_lookdir(self,color_str):
        # right
        if self.look_dir == game.PDIR_RIGHT:
            return color_str + "_player_walk_right"
        else:
            return color_str + "_player_walk_left"
    def draw(self, canvas):
        #gameobject.GameObject.draw(self, canvas)
        #canvas.blit(cloth_image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        self.current_animation.draw(canvas,self.draw_pos.get())

        # allways show "body"
        #canvas.blit(body_image, self.draw_pos.get(), None, pygame.BLEND_RGB_ADD)
