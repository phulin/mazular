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
    def dispel_shadow(self, maze):
        if self.power_points > 1:
            for i in range(len(MAZE.CREATURES))[2:]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        if MAZE.CREATURES[i].position[0] == self.position[0]+j and MAZE.CREATURES[i].position[2] == self.position[2]+k:
                            pass
