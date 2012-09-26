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
SURFACE = pygame.display.set_mode((SQ_SIZE * MAZE.width()+SQ_SIZE/10, SQ_SIZE * MAZE.height()+SQ_SIZE/10))
PLAYERS = [Player([x for x in MAZE.starting_locations[i]], PLAYER_COLORS[i])
					 for i in range(len(MAZE.starting_locations))]

FONT = pygame.font.SysFont(None, 48)
pygame.key.set_repeat(1, 300)
    
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
					print "Win conditions :" + str(MAZE.starting_locations) + " Player 0: " + str(PLAYERS[0].position)
					if event.key == pygame.K_UP:
                                                PLAYERS[0].up(MAZE)
                                        if event.key == pygame.K_DOWN:
                                                PLAYERS[0].down(MAZE)
                                        if event.key == pygame.K_LEFT:
                                                PLAYERS[0].left(MAZE)
                                        if event.key == pygame.K_RIGHT:
                                                PLAYERS[0].right(MAZE)
                                        if event.key == pygame.K_w:
                                                PLAYERS[1].up(MAZE)
                                        if event.key == pygame.K_s:
                                                PLAYERS[1].down(MAZE)
                                        if event.key == pygame.K_a:
                                                PLAYERS[1].left(MAZE)
                                        if event.key == pygame.K_d:
                                                PLAYERS[1].right(MAZE)

                                       
		SURFACE.fill(BG_COLOR)
		for player in PLAYERS:
				position = player.position
				# IMPORTANT: MAZE and pygame use reversed coordinates, so we have to flip here.
				screen_position = (int(SQ_SIZE * (position[1] + 0.5)), int(SQ_SIZE * (position[0] + 0.5)))
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
                #Win condition
                if PLAYERS[0].position==MAZE.starting_locations[1]:
                            text = FONT.render('Red Victory!', True, (122, 122, 122))
                            textRect = text.get_rect()
                            textRect.centerx = SURFACE.get_rect().centerx
                            textRect.centery = SURFACE.get_rect().centery
                            SURFACE.blit(text,textRect)
                            pygame.display.update()
                            break
                elif PLAYERS[1].position==MAZE.starting_locations[0]:
                            text = FONT.render('Blue Victory!', True, (122, 122, 122))
                            textRect = text.get_rect()
                            textRect.centerx = SURFACE.get_rect().centerx
                            textRect.centery = SURFACE.get_rect().centery
                            SURFACE.blit(text,textRect)
                            pygame.display.update()
                            break
while True:		
                for event in pygame.event.get():
                            if event.type is QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
