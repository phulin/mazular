from maze import Maze
import pygame

class Creature:
    clock = clock = pygame.time.Clock()
    position = [0, 0]
    #color = (255, 255, 255)
    direction = Maze.BOTTOM
    number = 0
    turn_time = 300
    time_till_move = turn_time
    power_points = 10
    name = ''
    
    def __init__(self, position, number, direction, name):
        self.position = position
        self.number = number
        self.direction = direction
        self.name = name
        self.clock = pygame.time.Clock()
        
    def move(self, maze, direction):
        self.direction = direction
        if self.clock.get_time() > self.time_till_move and not maze.walls(*self.position)[direction] and not self.collision(maze.CREATURES,direction):
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
#Colision detection between players            
    def collision(self, creatures, direction):
        for c in creatures:
            if c.position==self.sqr_in_front(direction): 
                return True
        return False
    def sqr_in_front(self, direction):
        if direction == Maze.TOP:
            return [self.position[0] - 1,self.position[1]]
        elif direction == Maze.RIGHT:
            return [self.position[0],self.position[1]+1]
        elif direction == Maze.BOTTOM:
            return [self.position[0] + 1,self.position[1]]
        elif direction == Maze.LEFT:
            return [self.position[0],self.position[1]-1]
