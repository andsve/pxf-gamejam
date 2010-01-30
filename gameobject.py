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
 OBJECT_TYPE_RED,
 OBJECT_TYPE_GREEN,
 OBJECT_TYPE_BLUE,
 OBJECT_TYPE_BW,
 OBJECT_TYPE_SPLOSION) = range(7)

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
#        self.draw_pos.set(self.pos.x - camera_pos.x, self.pos.y - camera_pos.y)
        pass

class SplosionBlock(GameObject):
    def __init__(self, pos, space, color_type):
        t_sprite = util.to_sprite(util.load_image("data/red_block16.png"))
        GameObject.__init__(self, pos, t_sprite, space, OBJECT_TYPE_SPLOSION, pm.inf)
        self.body, self.shape = create_ball(self, (pos.x, pos.y), mass=1.0, radius=2.0)
        self.shape.collision_type = OBJECT_TYPE_SPLOSION
        space.add(self.body, self.shape)
        self.area = (0,0,16,16) # make this random!
        self.body.apply_impulse((random.randint(-100, 100), random.randint(-200, 200))) # make this also random!

    def update(self, camera_pos):
        GameObject.update(self, camera_pos)

    def draw(self, canvas):
        canvas.blit(self.sprite.image, self.draw_pos.get(), None, pygame.BLEND_MAX)
