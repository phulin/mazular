# Maze class
# Serialized format:
# +-+-+-+
# |0  |*|
# + + + +
# |*|1 2|
# +-+-+-+

import re
#THIS CHANGES THE VIEW SIZE
offset = 1
CREATURES = []

def maze_from_file(filename):
    return Maze(open(filename).read())

def draw_maze(SQ_SIZE,MAZE,SURFACE,PLAYERS,wall_vertical_texture,wall_horizontal_texture,mcguffs, mac_small):                               
    draw_maze_single_player(SQ_SIZE,MAZE,SURFACE,PLAYERS[0],wall_vertical_texture,wall_horizontal_texture,mcguffs, mac_small);                  
    draw_maze_single_player(SQ_SIZE,MAZE,SURFACE,PLAYERS[1],wall_vertical_texture,wall_horizontal_texture,mcguffs, mac_small);                                                                                                                             
def draw_maze_floor(SQ_SIZE,MAZE,SURFACE,PLAYERS,floor_texture):
    for i in range(PLAYERS[0].position[0] - offset, PLAYERS[0].position[0] + offset + 1):
        for j in range(PLAYERS[0].position[1] - offset, PLAYERS[0].position[1] + offset + 1):       
            if(i >=0 and j >=0 and i < MAZE.height() and j < MAZE.width()):   
                SURFACE.blit(floor_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
    for i in range(PLAYERS[1].position[0] - offset, PLAYERS[1].position[0] + offset + 1):
        for j in range(PLAYERS[1].position[1] - offset, PLAYERS[1].position[1] +offset+1):       
            if(i >=0 and j >=0 and i < MAZE.height() and j < MAZE.width()):   
                SURFACE.blit(floor_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
    
def draw_maze_single_player(SQ_SIZE,MAZE,SURFACE,player,wall_vertical_texture,wall_horizontal_texture,mcguffs, mac_small):           
    macguf_regex = re.compile(r"[012]")
    for i in range(player.position[0]-offset, player.position[0] + 1+offset):
        for j in range(player.position[1]-offset, player.position[1] + 1+offset):       
            if(i >=0 and j >=0 and i < MAZE.height() and j < MAZE.width()):   
                if (MAZE.macguffin_locations[i][j] != 3) :
                    
                    if(int(MAZE.macguffin_locations[i][j]) > 5):
                        macg_temp =int( MAZE.macguffin_locations[i][j]) - 5
                        for which_guf in range(3):
                            
                            if (macg_temp - 4 >= 0):
                                SURFACE.blit(mcguffs[2], (j*SQ_SIZE+mac_small[2],i*SQ_SIZE+10+20,0,0))
                                macg_temp -= 4
                            if (macg_temp - 2 >= 0):
                                SURFACE.blit(mcguffs[1], (j*SQ_SIZE+mac_small[1],i*SQ_SIZE+10+20,0,0))
                                macg_temp -= 2
                            if (macg_temp - 1 >= 0):
                                SURFACE.blit(mcguffs[0], (j*SQ_SIZE+mac_small[0],i*SQ_SIZE+10+20,0,0))        
                    if(int(MAZE.macguffin_locations[i][j]) < 3):
                    
                        which_guf = int(MAZE.macguffin_locations[i][j])
                        SURFACE.blit(mcguffs[which_guf], (j*SQ_SIZE+10,i*SQ_SIZE+10,0,0))
                if (MAZE.walls(i,j)[MAZE.TOP]) :
                    SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
                if (MAZE.walls(i,j)[MAZE.BOTTOM]) : 
                    SURFACE.blit(wall_horizontal_texture, (j*SQ_SIZE,(i+1)*SQ_SIZE,0,0)) 
                if (MAZE.walls(i,j)[MAZE.RIGHT]) :   
                    SURFACE.blit(wall_vertical_texture, ((j+1)*SQ_SIZE,i*SQ_SIZE,0,0))
                if (MAZE.walls(i,j)[MAZE.LEFT]) :
                    SURFACE.blit(wall_vertical_texture, (j*SQ_SIZE,i*SQ_SIZE,0,0))
                    
                    
                    
                    

class Maze:
    class ParseError:
        def __init__(self, line):
            self.line = line
        def __str__(self):
            return "Parse error on line " + str(line)

    class SemanticError:
        def __init__(self, str):
            self.str = str
        def __str__(self):
            return "Semantic error in maze file: " + str

    # enum for direction support
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    horiz_regex = re.compile(r"\+([- ]\+)+$")
    vert_regex = re.compile(r"\|([ *@012][| ])+$")
    macguf_regex = re.compile(r"[012]")
    powerp_regex = re.compile(r"@")

    # Takes string representation of maze, as outlined above
    def __init__(self, maze_repr):
        maze_repr = maze_repr.strip()

        # Our internal representation includes the exterior walls of the maze.
        # Do not use these externally! Use the walls function.
        # The first coordinate gives row, the second column; both are zero-indexed.
        # NOTE THAT THIS IS THE OPPOSITE OF WHAT PYGAME USES.
        # horiz_walls is an (m + 1) x n matrix giving the locations of horizontal walls
        self.horiz_walls = []
        # vert_walls is an m x (n + 1) matrix giving the locations of vertical walls
        self.vert_walls = []
        # list of starting locations; should only contain two
        self.starting_locations = []
        

        maze_lines = maze_repr.splitlines()
        # list of macguffins; currently 3
        self.macguffin_locations = [[3 for i in range(len(maze_lines))] for j in range(len(maze_lines))]
        # power...points... really that name is horrible
        self.powerp_locations = []
       
        for line_num in range(len(maze_lines)):
            line = maze_lines[line_num].strip()
            if line_num % 2 is 0 and self.horiz_regex.match(line):
                # discard all the +'s, as we can just read the hyphens and spaces
                line = line.replace('+', '')
                self.horiz_walls.append([c == '-' for c in line])
            elif line_num % 2 is 1 and self.vert_regex.match(line):
                result = []
                for col_num in range(len(line)):
                    c = line[col_num]
                    if c is '*':
                        self.starting_locations.append([line_num / 2, col_num / 2])
                    if self.macguf_regex.match(c):
                        self.macguffin_locations[line_num/2][col_num/2] = c;
                    if self.powerp_regex.match(c):
                        self.powerp_locations.append([line_num/2,col_num/2]);
                    if col_num % 2 is 0:
                        result.append(c == '|')
                self.vert_walls.append(result)
            else:
                raise Maze.ParseError(line_num)
        m = len(self.vert_walls)
        n = len(self.horiz_walls[0])
        for walls in self.horiz_walls:
            if len(walls) is not n:
                raise Maze.SemanticError("Horizontal wall length failure")
        for walls in self.vert_walls:
            if len(walls) is not n + 1:
                raise Maze.SemanticError("Vertical wall length failure")

    # returns a list of boolean values indicating whether there is a wall at
    # each position
    # should be referenced like maze.walls(2, 2)[Maze.TOP]
    def walls(self, row, col):
        return [self.horiz_walls[row][col],
                self.vert_walls[row][col + 1],
                self.horiz_walls[row + 1][col],
                self.vert_walls[row][col]]

    # returns maze width
    def width(self):
        return len(self.horiz_walls[0])

    def height(self):
        return len(self.vert_walls)

