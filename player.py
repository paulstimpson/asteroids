from circleshape import CircleShape
from constants import *
import pygame
from shot import *

class Player(CircleShape,pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.shot_timer=0
       

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE] and self.shot_timer<=0:
            self.shoot()
            self.shot_timer=PLAYER_SHOT_COOLDOWN
        self.shot_timer-=dt

    def rotate(self,dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_x_origin=forward.x*PLAYER_RADIUS
        shot_y_origin=forward.y*PLAYER_RADIUS
        shot = Shot(self.position.x+shot_x_origin, self.position.y+shot_y_origin)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot