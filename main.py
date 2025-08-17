import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids 0.1.0")

    #Creating Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
     
    #Creating Containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    #Creating player start position and containers
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    #Infinite "While" loop for gameplay
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Updating items in Updatables container
        for item in updatable:
            item.update(dt)
        
        #Detecting collision with player and asteroids, ending game if collision detected
        for item in asteroids:
            if item.collision(player) == True:
                print("Game Over!")
                sys.exit()
        
        #Drawing items in Drawables container
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()  
        screen.fill("black")
        
        #setting Framerate at 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()