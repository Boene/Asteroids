import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
            
        screen.fill("black")

        for a in updatable:
            a.update(dt)

        for obj in asteroids:
            if player.coll_check(obj) == True:
                print("Game over!")
                raise SystemExit()
            for bullet in shots:
                if obj.coll_check(bullet) == True:
                    obj.split()
                    bullet.kill()

        for b in drawable:
            b.draw(screen)

        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

if __name__ =="__main__":
    main()