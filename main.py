import pygame
import sys
from maze import maze_from_file
from player import Player
from pygame.locals import *

pygame.init()


BG_COLOR = (0, 0, 0)
PLAYER_COLORS = [(255, 0, 0), (0, 0, 255)]
SQ_SIZE = 100 # pixel size of each square
WALL_HEIGHT = 10
WALL_WIDTH = SQ_SIZE
MAZE = maze_from_file("maze.txt")
SURFACE = pygame.display.set_mode((SQ_SIZE * 2*MAZE.width(),
																	 SQ_SIZE * 2*MAZE.height()))
PLAYERS = [Player(MAZE.starting_locations[i], PLAYER_COLORS[i])
					 for i in range(len(MAZE.starting_locations))]

pygame.display.set_caption('Mazular')
#load whole sprite, select coordinates for right one
#unsure if you all want to keep it this way or crop out the actual tile
wall_sprite = pygame.image.load("art/wallfloortiles.png")
wall_texture = wall_sprite.subsurface( 445, 12, 150, 150)
wall_vertical_texture = pygame.transform.scale( wall_texture, (WALL_HEIGHT, WALL_WIDTH))
wall_horizontal_texture = pygame.transform.rotate(wall_vertical_texture, 90)

# TODO(phulin): make ticks so we don't use all the CPU!
while True:
		for event in pygame.event.get():
				if event.type is QUIT:
						pygame.quit()
						sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()

		SURFACE.fill(BG_COLOR)
		for player in PLAYERS:
				position = player.position
				# IMPORTANT: MAZE and pygame use reversed coordinates, so we have to flip here.
				screen_position = (int(SQ_SIZE * (position[1] + 0.5)),
													 int(SQ_SIZE * (position[0] + 0.5)))
				pygame.draw.circle(SURFACE, player.color, screen_position, int(SQ_SIZE * 0.3))

		#logic that draws the walls
		for i in range(MAZE.height()):
			for j in range(MAZE.width()):
				if (MAZE.walls(i,j)[MAZE.TOP]) :
					SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
				if (MAZE.walls(i,j)[MAZE.BOTTOM]) :
					SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,(i+1)*SQ_SIZE,0,0))
				if (MAZE.walls(i,j)[MAZE.RIGHT]) :
					SURFACE.blit(wall_vertical_texture, ((j+1)*SQ_SIZE,i*SQ_SIZE,0,0))
				if (MAZE.walls(i,j)[MAZE.LEFT]) :
					SURFACE.blit(wall_vertical_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))

		pygame.display.update()
