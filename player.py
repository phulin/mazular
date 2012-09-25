import pygame

class Player:
    clock = pygame.time.Clock()
    position = [0, 0]
    color = (255, 255, 255)
    turn_time = 2000
    time_till_move = turn_time
    
    def __init__(self, position, color):
        self.position = position
        self.color = color
    def up(self, maze):
        print self.time_till_move - self.clock.get_time()
        if not maze.horiz_walls[self.position[0]][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[0] = self.position[0] - 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
    def down(self, maze):
        print self.time_till_move - self.clock.get_time()
        if not maze.horiz_walls[self.position[0]+1][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[0] = self.position[0] + 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()   
    def left(self, maze):
        print self.time_till_move - self.clock.get_time()
        if not maze.vert_walls[self.position[0]][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[1] = self.position[1] - 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
    def right(self, maze):
        print self.time_till_move - self.clock.get_time()
        if not maze.vert_walls[self.position[0]][self.position[1]+1] and self.clock.get_time()>self.time_till_move:
            self.position[1] = self.position[1] + 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
##    vert_wall_left = (self.position[0], self.position[1])
##    vert_wall_right = (self.position[0], self.position[1]+1)
##    horiz_wall_top = (self.position[0], self.position[1])
##    horiz_wall_bottom = (self.position[0]+1, self.position[1])
