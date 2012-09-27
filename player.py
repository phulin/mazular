from maze import Maze
from creature import Creature
from shadow import Shadow
import pygame

class Player(Creature):
    def summon_shadow(self, position, direction, maze):
        if self.power_points > 0:
            shadow = Shadow(position, self.number, direction, 'shadow')
            maze.CREATURES.append(shadow)
            self.power_points -= 1
        
