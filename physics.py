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
                old_rect = o.sprite.rect.copy()
                o.move(o.vel.x, o.vel.y)
                o.vel.set(o.vel.x, o.vel.y + self.gravity)
                if o.vel.y > 5: o.vel.y = 5
                if o.vel.x > 5: o.vel.x = 5

                # Check collisions
                for co in self.objects:
                    if not o is co:
                        if pygame.sprite.collide_rect(o.sprite, co.sprite):
                            o.sprite.rect = old_rect
