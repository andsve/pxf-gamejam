import util
import pygame

class Physics:
    def __init__(self):
        self.gravity = 0.4
        self.reset()

    def reset(self):
        self.objects = []

    def add_dynamic(self, obj):
        obj.dynamic = True
        self.objects.append(obj)

    def add_static(self, obj):
        obj.dynamic = False
        self.objects.append(obj)

    # todo: add timestep
    def step(self):
        old_values = None
        for o in self.objects:
            # Update movement
            if o.dynamic == True:
                old_values = (util.vec2(o.pos.x, o.pos.y), util.vec2(o.dir.x, o.dir.y), util.vec2(o.vel.x, o.vel.y))
                o.pos.set(o.pos.x + o.vel.x, o.pos.y + o.vel.y)
                o.vel.set(o.vel.x, o.vel.y + self.gravity)

                collided = []
                # Check collisions
                for co in self.objects:
                    if not o is co:
                        #print str(o) + " collides with " + str(co)
                        if pygame.sprite.collide_rect(o.sprite, co.sprite):
                            o.pos.y = co.pos.y - co.sprite.rect.height
