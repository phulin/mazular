import unittest
from maze import Maze

class TestMazeParsing(unittest.TestCase):
    def setUp(self):
        self.maze_repr_bad = """
        +-+-+-+
        |aaaaa|
        +-+-+-+
        """

        self.maze_repr_bad_semantic = """
        +-+-+-+
        | | |
        +-+-+-+
        """

        self.maze_repr = """
        +-+-+-+
        |   |*|
        + + + +
        |*|   |
        +-+-+-+
        """

        self.horiz_walls = [[True, True, True],
                       [False, False, False],
                       [True, True, True]]

        self.vert_walls = [[True, False, True, True],
                      [True, True, False, True]]

    def test_parse_bad(self):
        self.assertRaises(Maze.ParseError, Maze, self.maze_repr_bad)

    def test_parse_bad_semantic(self):
        self.assertRaises(Maze.SemanticError, Maze, self.maze_repr_bad_semantic)

    def test_parse(self):
        self.maze = Maze(self.maze_repr)
        self.assertEqual(self.horiz_walls, self.maze.horiz_walls)
        self.assertEqual(self.vert_walls, self.maze.vert_walls)

    def test_walls(self):
        self.maze = Maze(self.maze_repr)
        self.assertEqual([True, True, False, False], self.maze.walls(0, 1))
        self.assertEqual([False, True, True, True], self.maze.walls(1, 0))

if __name__ == '__main__':
    unittest.main()
