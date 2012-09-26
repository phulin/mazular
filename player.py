import pygame

class Player:
    clock = pygame.time.Clock()
    position = [0, 0]
    #color = (255, 255, 255)
    direction = "FRONT"
    number = 0
    turn_time = 300
    time_till_move = turn_time
    power_points = 0
    
    def __init__(self, position, number, direction):
        self.position = position
        self.number = number
        self.direction = direction
    def up(self, maze):
        self.direction = "BACK"
        print self.time_till_move - self.clock.get_time()
        if not maze.horiz_walls[self.position[0]][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[0] = self.position[0] - 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
    def down(self, maze):
        self.direction = "FRONT"
        print self.time_till_move - self.clock.get_time()
        if not maze.horiz_walls[self.position[0]+1][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[0] = self.position[0] + 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()   
    def left(self, maze):
        self.direction = "LEFT"
        print self.time_till_move - self.clock.get_time()
        if not maze.vert_walls[self.position[0]][self.position[1]] and self.clock.get_time()>self.time_till_move:
            self.position[1] = self.position[1] - 1
            self.time_till_move = self.turn_time
        else:
            self.time_till_move = self.time_till_move - self.clock.get_time()
        self.clock.tick()
    def right(self, maze):
        self.direction = "RIGHT"
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
