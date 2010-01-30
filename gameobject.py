#!/usr/bin/env python
import pygame
import util
import pymunk as pm

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

aoeaoea,OBJECT_TYPE_PLAYER,OBJECT_TYPE_RED,OBJECT_TYPE_GREEN,OBJECT_TYPE_BLUE = range(5)

class GameObject:
    def __init__(self, pos, sprite, space, obj_type, mass = 5.0):
        self.draw_pos = util.vec2(0, 0)
        self.sprite = sprite
        #self.move(pos.x, pos.y)
        self.body, self.shape = create_box(space, (pos.x, pos.y), 8, mass)

        self.object_type = obj_type
        self.shape.collision_type = obj_type

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
        space.add_static(self.shape)
        #self.shape.collision_type = 1

    def update(self, camera_pos):
        GameObject.update(self, camera_pos)
#        self.draw_pos.set(self.pos.x - camera_pos.x, self.pos.y - camera_pos.y)
        pass
