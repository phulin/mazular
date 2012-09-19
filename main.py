import pygame
import sys
from maze import maze_from_file
from player import Player
from pygame.locals import *

pygame.init()

BG_COLOR = (0, 0, 0)
PLAYER_COLORS = [(255, 0, 0), (0, 0, 255)]
SQ_SIZE = 100 # pixel size of each square
MAZE = maze_from_file("maze.txt")
SURFACE = pygame.display.set_mode((SQ_SIZE * MAZE.width(),
                                   SQ_SIZE * MAZE.height()))
PLAYERS = [Player(MAZE.starting_locations[i], PLAYER_COLORS[i])
           for i in range(len(MAZE.starting_locations))]

pygame.display.set_caption('Mazular')

# TODO(phulin): make ticks so we don't use all the CPU!
while True:
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            sys.exit()

    SURFACE.fill(BG_COLOR)
    for player in PLAYERS:
        position = player.position
        screen_position = (int(SQ_SIZE * (position[1] + 0.5)),
                           int(SQ_SIZE * (position[0] + 0.5)))
        pygame.draw.circle(SURFACE, player.color, screen_position, int(SQ_SIZE * 0.3))

    pygame.display.update()
