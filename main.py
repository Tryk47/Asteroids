# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *






def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize PyGame
    pygame.init()

    # create a Clock to keep time and FPS
    clock = pygame.time.Clock()
    dt = 0

    # set up the display 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Groups & Containers:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)


    # Instantiate the player & Asteroid field
    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
    )

    asteroid_field = AsteroidField()

    # -----------------------------------------------
    # Game Loop:
    # -----------------------------------------------
    while True:
        # Closes the game on exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills the screen with black. 
        screen.fill("black")

        # Update & draw all objects
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)


        # Check for collisions
        for object in asteroids:
            if object.check_collision(player):
                print("Game Over !")
                return


        # Update the screen. 
        pygame.display.flip()

        # Control FPS by delaying the next iteration. 
        # Saves the actual time in miliseconds. 
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()