import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(x, y)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.collision_check(player):
                print("Game over!")
                sys.exit()

        for item in asteroids:
                for shot in shots:
                    if shot.collision_check(item):
                        item.split(dt)
                        shot.kill()


        screen.fill(color=(0,0,0))

        for item in drawable:
            item.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000

        

main()

if __name__ == "main":
    main()