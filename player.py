#!/usr/bin/env python
import pygame
import gameobject
import util
import animation

class Player(gameobject.GameObject):
    def __init__(self, pos, space):
        gameobject.GameObject.__init__(self, pos, util.to_sprite(util.load_image("data/bw_player16.png")), space, 10.0)
        space.add(self.body, self.shape)
        #self.image = pygame.image.load("data/bw_guy_walk0.png")
        self.animations = {}

        #create animations
        player_walk_left = animation.new_animation("data/bw_guy_walk","png",1,8,[0,1])
        player_walk_right = animation.new_animation("data/bw_guy_walk_r","png",1,8,[0,1])
        
        #player_walk_left.play()
        self.image = player_walk_left.sprite.image
        
        self.animations["player_walk_left"] = player_walk_left
        self.animations["player_walk_right"] = player_walk_right
        
        self.current_animation = player_walk_left
        
        self.look_dir = 0 # 0 = right, 1 = left
        self.bw_image = pygame.image.load("data/bw_player16.png")
        self.red_image = pygame.image.load("data/red_player16.png")
        self.green_image = pygame.image.load("data/green_player16.png")
        self.blue_image = pygame.image.load("data/blue_player16.png")

        self.bw_image_r = pygame.image.load("data/bw_player16_r.png")
        self.red_image_r = pygame.image.load("data/red_player16_r.png")
        self.green_image_r = pygame.image.load("data/green_player16_r.png")
        self.blue_image_r = pygame.image.load("data/blue_player16_r.png")

    def update(self, camera_pos,dt):
        gameobject.GameObject.update(self, camera_pos)
        for anim in self.animations.keys():
            self.animations[anim].update(dt)
    
    def set_color()

    def draw(self, canvas):
        if (self.look_dir == 0):
            # looking right
            # find correct color
            body_image = self.bw_image
            cloth_image = self.red_image
            
            if not self.current_animation.playing:
                self.current_animation.play()
            self.current_animation = self.animations["player_walk_right"]
        else:
            # looking left
            # find correct color
            body_image = self.bw_image_r
            cloth_image = self.red_image_r
            
            if not self.current_animation.playing:
                self.current_animation.play()
            self.current_animation = self.animations["player_walk_left"]

        #gameobject.GameObject.draw(self, canvas)
        #canvas.blit(cloth_image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        #canvas.blit(self.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
        self.current_animation.draw(canvas,self.draw_pos.get())

        # allways show "body"
        #canvas.blit(body_image, self.draw_pos.get(), None, pygame.BLEND_RGB_ADD)
