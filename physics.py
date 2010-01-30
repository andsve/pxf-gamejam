import util
import pygame

class Physics:
    def __init__(self):
        self.gravity = 0.4
        self.damp = 0.3
        self.player = None
        self.reset()

    def reset(self):
        self.objects = []

    def add_dynamic(self, obj):
        obj.dynamic = True
        self.objects.append(obj)

    def add_static(self, obj):
        obj.dynamic = False
        self.objects.append(obj)

    def add_player(self, player):
        player.dynamic = True
        self.player = player
        self.objects.append(player)

    def get_colliding_objects(self, obj):
        c = []
        for o in self.objects:
            if obj is not o and obj.sprite.rect.colliderect(o.sprite.rect):
                c.append(o)
        return c

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
                """
                player_collisions = self.get_colliding_objects(self.player)
                if len(player_collisions) > 0:
                    r = None
                    diff = 100000000
                    for c in player_collisions[1:]:
                        a = c.sprite.rect.top - self.player.sprite.rect.top
                        if a < diff:
                            diff = a
                            r = c
                    self.player.sprite.rect.move_ip(0, -diff)
                """
                # Check collisions
                for co in self.objects:
                    if not o is co:# and o is not self.player:
                        if pygame.sprite.collide_rect(o.sprite, co.sprite):
                            o.sprite.rect = old_rect
