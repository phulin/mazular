from maze import Maze
from creature import Creature
import pygame
import random
class Shadow(Creature):
    turn_time = 600
    def navigate(self,maze):
        print "go"
        n = random.randint(0,3)
        if n==0:
            self.move(maze, Maze.TOP)
        if n==1:
            self.move(maze, Maze.RIGHT)
        if n==2:
            self.move(maze, Maze.BOTTOM)
        if n==3:
            self.move(maze, Maze.LEFT)
