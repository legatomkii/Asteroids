import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids 0.0.4")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.draw(screen) 
        pygame.display.flip()      
        screen.fill("black")
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()