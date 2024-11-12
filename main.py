# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame, sys
from player import *
from circleshape import *
from constants import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	new_clock = pygame.time.Clock()
	dt = 0	

	shots_group = pygame.sprite.Group()

	while True:
		dt = new_clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for sprite in updatable:
			if isinstance(sprite, Player):
				sprite.update(dt, shots_group)
			else: 
				sprite.update(dt)
		for sprite in asteroids:
			if sprite.collision(player):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.split()
		screen.fill((0,0,0))
		for sprite in drawable:
			sprite.draw(screen)
		
		pygame.display.flip()

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()	