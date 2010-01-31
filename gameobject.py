#!/usr/bin/env python
import pygame
import util
import pymunk as pm
import random

def create_ball(self, pos, mass=1.0, radius=8.0):
    moment = pm.moment_for_circle(mass, radius, 0.0, pm.Vec2d(0,0))
    ball_body = pm.Body(mass, moment)
    ball_body.position = pm.Vec2d(pos)
    ball_shape = pm.Circle(ball_body, radius, pm.Vec2d(0,0))
    ball_shape.friction = 1.5
    #ball_shape.collision_type = COLLTYPE_DEFAULT
    #self.space.add(ball_body, ball_shape)
    # return ball_shape
    return ball_body, ball_shape

def create_poly(space, points, mass = -5.0, pos = (0,0)):
    moment = pm.moment_for_poly(mass, points, pm.Vec2d(0,0))
    #moment = 1000
    body = pm.Body(mass, moment)
    body.position = pm.Vec2d(pos)

    shape = pm.Poly(body, points, pm.Vec2d(0,0))
    shape.friction = 0.5
    #shape.collision_type = 0
    #space.add(body, shape)
    #space.add_static(shape)
    return body, shape

def create_box(space, pos, size = 10, mass = 5.0):
    box_points = map(pm.Vec2d, [(-size, -size), (-size, size), (size,size), (size, -size)])
    return create_poly(space, box_points, mass = mass, pos = pos)

(OBJECT_TYPE_FAIL,
 OBJECT_TYPE_PLAYER,
 OBJECT_TYPE_KEY_RED,
 OBJECT_TYPE_KEY_GREEN,
 OBJECT_TYPE_KEY_BLUE,
 OBJECT_TYPE_RED,
 OBJECT_TYPE_GREEN,
 OBJECT_TYPE_BLUE,
 OBJECT_TYPE_SPLOSION,
 OBJECT_TYPE_BW,
 OBJECT_TYPE_ALL) = range(11)

class GameObject:
    def __init__(self, pos, sprite, space, obj_type, mass = 5.0):
        self.draw_pos = util.vec2(0, 0)
        self.sprite = sprite
        #self.move(pos.x, pos.y)


        self.object_type = obj_type
        #self.shape.collision_type = obj_type

    def move(self, x, y):
        pass
       #self.sprite.rect.move_ip(x, y)
       #self.delta_move.x += x
       #self.delta_move.y += y

    def update(self, camera_pos):
        self.draw_pos = util.vec2(self.body.position.x - camera_pos.x, self.body.position.y - camera_pos.y)#util.vec2(self.sprite.rect.left - camera_pos.x, self.sprite.rect.top - camera_pos.y)

    def draw(self, canvas):
        #canvas.blit(self.sprite.image, self.pos.get(), None, pygame.BLEND_MAX)
        if self.object_type == OBJECT_TYPE_BW:
            canvas.blit(self.sprite.image, self.draw_pos.get(), None)
        else:
            canvas.blit(self.sprite.image, self.draw_pos.get(), None, pygame.BLEND_MAX)



class StaticBlock(GameObject):
    def __init__(self, pos, sprite, space, obj_type):
        GameObject.__init__(self, pos, sprite, space, obj_type, pm.inf)
        self.body, self.shape = create_box(space, (pos.x, pos.y), 8, pm.inf)
        self.shape.collision_type = obj_type
        space.add_static(self.shape)
        #self.shape.collision_type = 1

    def update(self, camera_pos):
        GameObject.update(self, camera_pos)
        pass

class MovableBlock(GameObject):
    def __init__(self, pos, sprite, space, obj_type):
        GameObject.__init__(self, pos, sprite, space, obj_type, pm.inf)
        self.body, self.shape = create_box(space, (pos.x, pos.y), 8, pm.inf)
        self.shape.collision_type = obj_type
        space.add(self.body, self.shape)
        #self.shape.collision_type = 1

    def update(self, camera_pos):
        GameObject.update(self, camera_pos)
        pass


splosion_red = util.to_sprite(util.load_image("data/red_explosion.png"))
splosion_green = util.to_sprite(util.load_image("data/green_explosion.png"))
splosion_blue = util.to_sprite(util.load_image("data/blue_explosion.png"))

class SplosionBlock(GameObject):
    def __init__(self, pos, space, color_type):
        if color_type == OBJECT_TYPE_RED:
            t_sprite = splosion_red
        elif color_type == OBJECT_TYPE_GREEN:
            t_sprite = splosion_green
        else:
            t_sprite = splosion_blue
        GameObject.__init__(self, pos, t_sprite, space, OBJECT_TYPE_SPLOSION, pm.inf)
        self.body, self.shape = create_ball(self, (pos.x, pos.y), mass=0.6, radius=0.1)
        self.shape.collision_type = OBJECT_TYPE_SPLOSION
        space.add(self.body, self.shape)

        self.frame_id = random.randint(0, 7)
        tx = self.frame_id % 4
        ty = int(self.frame_id / 4)
        self.area = (tx * 4,tx * 4,4,4) # make this random!

        self.body.apply_impulse((random.randint(-100, 100), random.randint(-200, 0))) # make this also random!

    def update(self, camera_pos):
        GameObject.update(self, camera_pos)

    def draw(self, canvas):
        canvas.blit(self.sprite.image, (self.draw_pos.x, self.draw_pos.y + 4), self.area, pygame.BLEND_MAX)
