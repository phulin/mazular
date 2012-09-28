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

mcguff_sprite = pygame.image.load("art/mcguffs.png")
pygame.transform.scale(player_sprite.subsurface(7,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
crown_mg = pygame.transform.scale(mcguff_sprite.subsurface(32,163,56,30),(SQ_SIZE-10,SQ_SIZE-10))
sceptor_mg = pygame.transform.scale(mcguff_sprite.subsurface(148,121,70,70),(SQ_SIZE-10,SQ_SIZE-10))
dragon_right = pygame.transform.scale(mcguff_sprite.subsurface(250,147,111,88),(SQ_SIZE-10,SQ_SIZE-10))
dragon_left = pygame.transform.scale(mcguff_sprite.subsurface(377,147,111,88),(SQ_SIZE-10,SQ_SIZE-10))
dragon_front = pygame.transform.scale(mcguff_sprite.subsurface(376,252,104,80),(SQ_SIZE-10,SQ_SIZE-10))
dragon_back = pygame.transform.scale(mcguff_sprite.subsurface(240,244,104,80),(SQ_SIZE-10,SQ_SIZE-10))
body_front = pygame.transform.scale(mcguff_sprite.subsurface(16,20,88,95),(SQ_SIZE-10,SQ_SIZE-10))
body_left = pygame.transform.scale(mcguff_sprite.subsurface(137,20,80,95),(SQ_SIZE-10,SQ_SIZE-10))
body_right = pygame.transform.scale(mcguff_sprite.subsurface(232,20,80,95),(SQ_SIZE-10,SQ_SIZE-10))
body_back = pygame.transform.scale(mcguff_sprite.subsurface(328,20,90,95),(SQ_SIZE-10,SQ_SIZE-10))
mcguffs = [crown_mg,sceptor_mg, [body_front,body_back,body_left,body_right]]
dragon = [dragon_front,dragon_back,dragon_left,dragon_right]

WALL_HEIGHT = 10
WALL_WIDTH = SQ_SIZE + WALL_HEIGHT
MAZE = maze_from_file("bigmaze.txt")
SURFACE = pygame.display.set_mode((SQ_SIZE * MAZE.width()+SQ_SIZE/10, SQ_SIZE * MAZE.height()+SQ_SIZE/10))
PLAYERS = [Player([x for x in MAZE.starting_locations[i]], i, Maze.BOTTOM, 'Player ' + str(i))
					 for i in range(len(MAZE.starting_locations))]
MAZE.CREATURES = [player for player in PLAYERS]
macguffins_collected = [0,0]
mac_small = [0,0]
FONT = pygame.font.SysFont(None, 48)
SMALL_FONT = pygame.font.SysFont(None, 30)
 
pygame.key.set_repeat(1, 300)
    
pygame.display.set_caption('Mazular')
#load whole sprite, select coordinates for right one
#unsure if you all want to keep it this way or crop out the actual tile
wall_sprite = pygame.image.load("art/wallfloortiles.png")
wall_texture = wall_sprite.subsurface( 731, 12, 150, 150)
wall_vertical_texture = pygame.transform.scale( wall_texture, (WALL_HEIGHT, WALL_WIDTH))
wall_horizontal_texture = pygame.transform.rotate(wall_vertical_texture, 90)
fog_sprite = pygame.image.load("art/wallfloortiles.png")
#fog_texture = fog_sprite.subsurface(733,238,190,190)
fog_texture = fog_sprite.subsurface(15,238,180,180)
fog_texture = pygame.transform.scale(fog_texture,(SQ_SIZE,SQ_SIZE));
floor_sprite = pygame.image.load("art/wallfloortiles.png")
floor_texture = fog_sprite.subsurface(15,15,180,180)
floor_texture = pygame.transform.scale(floor_texture,(SQ_SIZE+WALL_HEIGHT,SQ_SIZE+WALL_HEIGHT));

mcguff_sprite = pygame.image.load("art/mcguffs.png")
pygame.transform.scale(player_sprite.subsurface(7,21,160,190),(SQ_SIZE-10,SQ_SIZE-10))
crown_mg = pygame.transform.scale(mcguff_sprite.subsurface(32,163,56,30),(SQ_SIZE-20,SQ_SIZE-30))
sceptor_mg = pygame.transform.scale(mcguff_sprite.subsurface(120,150,70,70),(SQ_SIZE-20,SQ_SIZE-20))
dragon_right = pygame.transform.scale(mcguff_sprite.subsurface(250,147,111,88),(SQ_SIZE-10,SQ_SIZE-10))
dragon_left = pygame.transform.scale(mcguff_sprite.subsurface(377,147,111,88),(SQ_SIZE-10,SQ_SIZE-10))
dragon_front = pygame.transform.scale(mcguff_sprite.subsurface(376,252,104,80),(SQ_SIZE-10,SQ_SIZE-10))
dragon_back = pygame.transform.scale(mcguff_sprite.subsurface(240,244,104,80),(SQ_SIZE-10,SQ_SIZE-10))
body_front = pygame.transform.scale(mcguff_sprite.subsurface(16,20,88,95),(SQ_SIZE-10,SQ_SIZE-10))
body_left = pygame.transform.scale(mcguff_sprite.subsurface(137,20,80,95),(SQ_SIZE-10,SQ_SIZE-10))
body_right = pygame.transform.scale(mcguff_sprite.subsurface(232,20,80,95),(SQ_SIZE-10,SQ_SIZE-10))
body_back = pygame.transform.scale(mcguff_sprite.subsurface(328,20,90,95),(SQ_SIZE-10,SQ_SIZE-10))
mcguffs = [crown_mg,sceptor_mg, [body_front,body_back,body_left,body_right]]
dragon = [dragon_front,dragon_back,dragon_left,dragon_right]

#half ass menu, also there are two text bits because this function 
#doesn't recognize new lines.

def load_start_menu() :
	exitMenu = True
	load_backstory = False
	load_instructions = False
	while (exitMenu ):
	    text = FONT.render("backstory", True, (102, 205, 170))
	    textRect = text.get_rect()
	    textRect.centerx = SURFACE.get_rect().centerx
	    textRect.centery = SURFACE.get_rect().centery-100
	    SURFACE.blit(text,textRect)
	    controls = FONT.render("controls description", True, (102, 205, 170))
	    textRect2 = controls.get_rect()
	    textRect2.centerx = SURFACE.get_rect().centerx
	    textRect2.centery = SURFACE.get_rect().centery
	    SURFACE.blit(controls,textRect2)
	    start = FONT.render("press any key to start", True, (102, 205, 170))
	    textRect3 = start.get_rect()
	    textRect3.centerx = SURFACE.get_rect().centerx
	    textRect3.centery = SURFACE.get_rect().centery+100
	    SURFACE.blit(start,textRect3)
	    pygame.display.update()
	    for event in pygame.event.get():
	    		if event.type == pygame.MOUSEBUTTONDOWN:
	    			if textRect.collidepoint(pygame.mouse.get_pos() ) : 
	    				load_backstory = True
	    				exitMenu = False
	    			elif textRect2.collidepoint(pygame.mouse.get_pos() ):
	    				load_instructions = True
	    				exitMenu = False
	    			elif textRect3.collidepoint(pygame.mouse.get_pos() ) :
	    				exitMenu = False
	    		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
	    				if event.key == pygame.K_m:
	    					pass
	    				else :
								exitMenu = False
	else:
			SURFACE.fill((0,0,0))
			if load_backstory:
					load_backstory_menu()
			elif load_instructions:
					load_instructions_menu()

def load_backstory_menu() :
	exitMenu = True
	load_start = False
	while (exitMenu ):
	    text = SMALL_FONT.render(" This is the story:", True, (102, 205, 170))
	    textRect = text.get_rect()
	    textRect.centerx = SURFACE.get_rect().centerx
	    textRect.centery = SURFACE.get_rect().centery-100
	    SURFACE.blit(text,textRect)
	    
	    start = SMALL_FONT.render("Press any key to start the game. Press M to return to main menu", True, (102, 205, 170))
	    textRect3 = start.get_rect()
	    textRect3.centerx = SURFACE.get_rect().centerx
	    textRect3.centery = SURFACE.get_rect().centery+100
	    SURFACE.blit(start,textRect3)
	    pygame.display.update()
	    for event in pygame.event.get():
	    		if event.type == pygame.MOUSEBUTTONDOWN and textRect3.collidepoint(pygame.mouse.get_pos() ) :
	    				exitMenu = False
	    		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
	    				if event.key == pygame.K_m:
	    					load_start = True
	    					exitMenu = False
	    				else :
								exitMenu = False
	else:
			SURFACE.fill((0,0,0))
			if load_start:
					load_start_menu()
			

def load_instructions_menu() :
	exitMenu = True
	load_start = False
	while (exitMenu ):
	    text = SMALL_FONT.render(" Left player move with WASD, right player move with arrow keys.", True, (102, 205, 170))
	    textRect = text.get_rect()
	    textRect.centerx = SURFACE.get_rect().centerx
	    textRect.centery = SURFACE.get_rect().centery-100
	    SURFACE.blit(text,textRect)
	    
	    start = SMALL_FONT.render("Press any key to start the game. Press M to return to main menu", True, (102, 205, 170))
	    textRect3 = start.get_rect()
	    textRect3.centerx = SURFACE.get_rect().centerx
	    textRect3.centery = SURFACE.get_rect().centery+100
	    SURFACE.blit(start,textRect3)
	    pygame.display.update()
	    for event in pygame.event.get():
	    		if event.type == pygame.MOUSEBUTTONDOWN and textRect3.collidepoint(pygame.mouse.get_pos() ) :
	    				exitMenu = False
	    		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
	    				if event.key == pygame.K_m:
	    					load_start = True
	    					exitMenu = False
	    				else :
								exitMenu = False
	else:
			SURFACE.fill((0,0,0))
			if load_start:
					load_start_menu()

							
load_start_menu()

while True:
		for event in pygame.event.get():
				if event.type is QUIT:
						pygame.quit()
						sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
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
#Summon Shadows
##					if event.key == pygame.K_SLASH:
##                                            PLAYERS[0].summon_shadow(PLAYERS[1].sqr_in_front(PLAYERS[1].direction),PLAYERS[1].direction, MAZE)
##                                        if event.key == pygame.K_r:
##                                            PLAYERS[1].summon_shadow(PLAYERS[0].sqr_in_front(PLAYERS[0].direction),PLAYERS[0].direction, MAZE) 

		for i in range(MAZE.height()+1):
			for j in range(MAZE.width()+1):
				SURFACE.blit(fog_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
		draw_maze_floor(SQ_SIZE,MAZE,SURFACE,PLAYERS,floor_texture)
		for player in PLAYERS:
				position = player.position
				# IMPORTANT: MAZE and pygame use reversed coordinates, so we have to flip here.
				screen_position = (int(SQ_SIZE * (position[1] + 0.2)), int(SQ_SIZE * (position[0] + 0.2)))
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
				
		for i in range(2):
			if(macguffins_collected[i] > 0 and MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] == 3):
				MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] = macguffins_collected[i] - 1
		
		draw_maze(SQ_SIZE,MAZE,SURFACE,PLAYERS,wall_vertical_texture,wall_horizontal_texture, mcguffs, mac_small)
				
                #Move and draw the shadows
                for i in range(len(MAZE.CREATURES))[2:]:
                    MAZE.CREATURES[i].navigate(MAZE)
                    position = MAZE.CREATURES[i].position
                    screen_position = (int(SQ_SIZE * (position[1] + 0.55)), int(SQ_SIZE * (position[0] + 0.6)))
                    pygame.draw.circle(SURFACE, (122,122,122), screen_position, int(SQ_SIZE * 0.3))
		pygame.display.update()
		
		
					
                #Win condition
                for i in range(2):
                    for j in range(2):
                        if MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] == str(j):
				#MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] = 3
				macguffins_collected[i] = macguffins_collected[i] + j + 1
				mcguffs[j] = pygame.transform.scale(mcguffs[j],(SQ_SIZE/4,SQ_SIZE/4))
				mac_small[j] = 25
		for i in range(2):
			if (macguffins_collected[i] == 1 and MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] != 1) :
				MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] = 3
			if (macguffins_collected[i] == 2 and MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] != 0) :
				MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] = 3
			if (macguffins_collected[i] == 3) :
				MAZE.macguffin_locations[PLAYERS[i].position[0]][PLAYERS[i].position[1]] = 3
				


		
		    
                if PLAYERS[0].position==MAZE.starting_locations[1]:
                            text = FONT.render('Purple Victory!', True, (122, 122, 122))
                            textRect = text.get_rect()
                            textRect.centerx = SURFACE.get_rect().centerx
                            textRect.centery = SURFACE.get_rect().centery
                            SURFACE.blit(text,textRect)
                            pygame.display.update()
                            break
                elif PLAYERS[1].position==MAZE.starting_locations[0]:
                            text = FONT.render('Yellow Victory!', True, (122, 122, 122))
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
