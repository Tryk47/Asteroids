# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *






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

    # Instantiate the player
    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
    )

    # Game Loop:
    while True:
        # Closes the game on exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills the screen with black. 
        screen.fill("black")

        # update player rotation
        player.update(dt)

        # draw the player
        player.draw(screen)



        # Update the screen. 
        pygame.display.flip()

        # Control FPS by delaying the next iteration. 
        # Saves the actual time in miliseconds. 
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()