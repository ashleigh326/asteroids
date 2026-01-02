import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for d in drawable:
            d.draw(screen)
            
        updatable.update(dt)

        for a in asteroids:
            if player.collides_with(a) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collides_with(a) == True:
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
                    
        pygame.display.flip()

        dt = timer.tick(60) / 1000
    



if __name__ == "__main__":
    main()
