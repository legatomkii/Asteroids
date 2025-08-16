import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids 0.0.9")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player) == True:
                print("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()  
        screen.fill("black")
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()