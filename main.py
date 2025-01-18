# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player

def main():
    print("Starting asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    # initialize pygame
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # create a window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)
    

    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        for thing in updatable:
            thing.update(dt)

        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)
        
        # update the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()