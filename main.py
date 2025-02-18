# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    updateables=pygame.sprite.Group()
    drawables=pygame.sprite.Group()
    Player.containers=(updateables,drawables)
    asteroids=pygame.sprite.Group()
    Asteroid.containers=(updateables,drawables,asteroids)
    AsteroidField.containers=(updateables)
    asteroidfield=AsteroidField()
    shots=pygame.sprite.Group()
    Shot.containers=(updateables,drawables,shots)

    dt=0
    player_1=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if player_1.collides_with(asteroid):
                print("Game over!")
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        dt=clock.tick(60)/1000

if __name__ == "__main__":
    main()
