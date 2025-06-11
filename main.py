# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *






def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups & Containers:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    # Instantiate the player & Asteroid field
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # -----------------------------------------------
    # Game Loop:
    # -----------------------------------------------
    while True:
        # Closes the game on exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Check for collisions
        for object in asteroids:
            if object.check_collision(player):
                print("Game Over !")
                sys.exit()
            
            for shot in shots:
                if object.check_collision(shot):
                    shot.kill()
                    object.split()

        # fills the screen with black. 
        screen.fill("black")

        # Update & draw all objects
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        # Update the screen. 
        pygame.display.flip()

        # Control FPS by delaying the next iteration. 
        # Saves the actual time in miliseconds. 
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()