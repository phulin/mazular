import pygame
import sys
from maze import *
from maze import draw_maze
from player import Player
from pygame.locals import *

pygame.init()


BG_COLOR = (0, 0, 0)
PLAYER_COLORS = [(255, 0, 0), (0, 0, 255)]
SQ_SIZE = 50 # pixel size of each square
#PLAYER_SPRITES = [pygame.image.load(os.path.join('art', 'bla.png')),pygame.image.load(os.path.join('art', 'bla.png'))]
player_sprite = pygame.image.load("art/royalghost.png")
p1_right = pygame.transform.scale(player_sprite.subsurface(7,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
p1_front = pygame.transform.scale(player_sprite.subsurface(7,261,175,190),(SQ_SIZE-10,SQ_SIZE-10))
p1_left = pygame.transform.scale(player_sprite.subsurface(471,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
p1_back = pygame.transform.scale(player_sprite.subsurface(519,261,175,190),(SQ_SIZE-10,SQ_SIZE-10))
p2_right = pygame.transform.scale(player_sprite.subsurface(231,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
p2_front = pygame.transform.scale(player_sprite.subsurface(264,261,175,190),(SQ_SIZE-10,SQ_SIZE-10))
p2_left = pygame.transform.scale(player_sprite.subsurface(695,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
p2_back = pygame.transform.scale(player_sprite.subsurface(759,261,175,190),(SQ_SIZE-10,SQ_SIZE-10))
PLAYER_SPRITES=[[p1_front,p1_back,p1_left,p1_right],[p2_front,p2_back,p2_left,p2_right]]
WALL_HEIGHT = 10
WALL_WIDTH = SQ_SIZE + WALL_HEIGHT
MAZE = maze_from_file("bigmaze.txt")
SURFACE = pygame.display.set_mode((SQ_SIZE * MAZE.width()+SQ_SIZE/10, SQ_SIZE * MAZE.height()+SQ_SIZE/10))
PLAYERS = [Player([x for x in MAZE.starting_locations[i]], i, Maze.BOTTOM)
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
fog_sprite = pygame.image.load("art/wallfloortiles.png")
#fog_texture = fog_sprite.subsurface(733,238,190,190)
fog_texture = fog_sprite.subsurface(15,238,180,180)
fog_texture = pygame.transform.scale(fog_texture,(SQ_SIZE,SQ_SIZE));
floor_sprite = pygame.image.load("art/wallfloortiles.png")
floor_texture = fog_sprite.subsurface(15,15,180,180)
floor_texture = pygame.transform.scale(floor_texture,(SQ_SIZE+WALL_HEIGHT,SQ_SIZE+WALL_HEIGHT));

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
					p1_keymap = {
							pygame.K_UP: Maze.TOP,
							pygame.K_DOWN: Maze.BOTTOM,
							pygame.K_LEFT: Maze.LEFT,
							pygame.K_RIGHT: Maze.RIGHT
					}
					p2_keymap = {
							pygame.K_w: Maze.TOP,
							pygame.K_s: Maze.BOTTOM,
							pygame.K_a: Maze.LEFT,
							pygame.K_d: Maze.RIGHT
					}
					if event.key in p1_keymap:
						PLAYERS[0].move(MAZE, p1_keymap[event.key])
					elif event.key in p2_keymap:
						PLAYERS[1].move(MAZE, p2_keymap[event.key])
		#SURFACE.fill(BG_COLOR)
		for i in range(MAZE.height()+1):
			for j in range(MAZE.width()+1):
				SURFACE.blit(fog_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
		draw_maze_floor(SQ_SIZE,MAZE,SURFACE,PLAYERS,floor_texture)
		draw_maze(SQ_SIZE,MAZE,SURFACE,PLAYERS,wall_vertical_texture,wall_horizontal_texture)
		for player in PLAYERS:
				position = player.position
				# IMPORTANT: MAZE and pygame use reversed coordinates, so we have to flip here.
				screen_position = (int(SQ_SIZE * (position[1] + 0.2)), int(SQ_SIZE * (position[0] + 0.2)))
				#pygame.draw.circle(SURFACE, player.color, screen_position, int(SQ_SIZE * 0.3))
				if player.direction==Maze.BOTTOM:
					index = 0
				elif player.direction==Maze.TOP:
					index = 1
				elif player.direction==Maze.LEFT:
					index = 2
				elif player.direction==Maze.RIGHT:
					index = 3
				else:
					index=0
				SURFACE.blit(PLAYER_SPRITES[player.number][index],screen_position)

		pygame.display.update()
                

		#logic that draws the walls
		'''
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
		'''
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

def draw_maze(SQ_SIZE,MAZE,SURFACE,PLAYERS,wall_vertical_texture,wall_horizontal_texture):
	draw_maze_single_player(PLAYERS[0]);
	draw_maze_single_player(PLAYERS[1]);
	pygame.display.update()

def draw_maze_single_player(SQ_SIZE,MAZE,SURFACE,PLAYERS,wall_vertical_texture,wall_horizontal_texture):
        for i in range(player.position[0] - SQ_SIZE*4, player.position[0] + SQ_SIZE*4):
            for j in range(player.position[1] - SQ_SIZE*4, player.position[1] + SQ_SIZE*4):
		if(i >=0 and j >=0):    
			if (MAZE.walls(i,j)[MAZE.TOP]) :
				SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
			if (MAZE.walls(i,j)[MAZE.BOTTOM]) :
				SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,(i+1)*SQ_SIZE,0,0))
			if (MAZE.walls(i,j)[MAZE.RIGHT]) :
				SURFACE.blit(wall_vertical_texture, ((j+1)*SQ_SIZE,i*SQ_SIZE,0,0))
			if (MAZE.walls(i,j)[MAZE.LEFT]) :
				SURFACE.blit(wall_vertical_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
