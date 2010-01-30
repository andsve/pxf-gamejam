import util
import pygame

class Physics:
    def __init__(self):
        self.gravity = 0.4
        self.damp = 0.3
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
            if o.dynamic == False:
                o.sprite.rect.move_ip(o.delta_move.x, o.delta_move.y)
                o.delta_move.set(0, 0)
            else:
                old_rect = o.sprite.rect.copy()
                o.sprite.rect.move_ip(o.delta_move.x + o.vel.x, o.delta_move.y + o.vel.y)
                o.delta_move.set(0, 0)
                o.vel.set(o.vel.x, o.vel.y + self.gravity)
                if o.vel.x > 0.001:
                    o.vel.x -= self.damp
                if o.vel.x < 0.001:
                    o.vel.x += self.damp

                if o.vel.y > 5: o.vel.y = 5
                if o.vel.x > 5: o.vel.x = 5
                if o.vel.y < -5: o.vel.y = -5
                if o.vel.x < -5: o.vel.x = -5

                # Check collisions
                for co in self.objects:
                    if not o is co:
                        if pygame.sprite.collide_rect(o.sprite, co.sprite):
                            o.sprite.rect = old_rect
