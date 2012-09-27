from maze import Maze
import pygame

class Player:
    clock = pygame.time.Clock()
    position = [0, 0]
    #color = (255, 255, 255)
    direction = Maze.BOTTOM
    number = 0
    turn_time = 3
    time_till_move = turn_time
    power_points = 0
    
    def __init__(self, position, number, direction):
        self.position = position
        self.number = number
        self.direction = direction

    def move(self, maze, direction):
        self.direction = direction
        if self.clock.get_time() > self.time_till_move and not maze.walls(*self.position)[direction]:
            if direction == Maze.TOP:
                self.position[0] -= 1
            elif direction == Maze.RIGHT:
                self.position[1] += 1
            elif direction == Maze.BOTTOM:
                self.position[0] += 1
            elif direction == Maze.LEFT:
                self.position[1] -= 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
