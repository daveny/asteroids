# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    # initialize pygame
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, shots, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

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
        
        for thing in asteroids:
            if thing.collide(player):
                print("Game over!")
                exit()
            for shot in shots:
                if thing.collide(shot):
                    thing.split()
                    shot.kill()
        
        
        # update the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()