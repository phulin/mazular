class Player:
    position = [0, 0]
    color = (255, 255, 255)

    def __init__(self, position, color):
        self.position = position
        self.color = color
    def up(self, maze):
        if not maze.horiz_walls[self.position[0]][self.position[1]]:
            self.position[0] = self.position[0] - 1
    def down(self, maze):
        if not maze.horiz_walls[self.position[0]+1][self.position[1]]:
            self.position[0] = self.position[0] + 1
    def left(self, maze):
        if not maze.vert_walls[self.position[0]][self.position[1]]:
            self.position[1] = self.position[1] - 1
    def right(self, maze):
        if not maze.vert_walls[self.position[0]][self.position[1]+1]:
            self.position[1] = self.position[1] + 1
##    vert_wall_left = (self.position[0], self.position[1])
##    vert_wall_right = (self.position[0], self.position[1]+1)
##    horiz_wall_top = (self.position[0], self.position[1])
##    horiz_wall_bottom = (self.position[0]+1, self.position[1])
