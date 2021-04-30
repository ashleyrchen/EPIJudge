import collections
import copy
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
Position = collections.namedtuple('Position', ('Coordinate', 'Path'))
MOVES = [(1, 0), (0, 1), (0, -1), (-1, 0),]


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
# ------MY SOLUTION,  O(|V| + |E|) time, O(|V|) space, 
# cleaned up by reading the textbook, notably, you do not need to keep a 
# "visited" set as you can just set squares to BLACK, also, you do not need 
# to store paths to each vertex as that is redundant, just figure out if 
# if you will be able to get to the exit, and if you are, then leave the 
# vertex in the path, and if not, delete it 

    def is_valid_coordinate(c: Coordinate):
        return (0 <= c.x < len(maze) and 0 <= c.y < len(maze[0]) 
                        and maze[c.x][c.y] == WHITE)

    def get_neighbors(c: Coordinate,) -> List[Coordinate]: 
        result = []
        for (d_x, d_y) in MOVES:
            pc = Coordinate(c.x + d_x, c.y + d_y)
            if is_valid_coordinate(pc):
                result.append(pc)
        return result
    
    def step(p: Coordinate):
        # step executes O(|V|) times
        path.append(p)
        maze[p.x][p.y] = BLACK
        if p == e:
            return path
        # the aggregate number of neighbors is O(|E|), hence, this (in aggregate) takes O(|E|) time
        if any(map(step, get_neighbors(p))): 
            return True
        del path[-1]
        return False

    path = []
    step(s)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    maze = [[1, 0], [0, 0]]
    s = Coordinate(1, 0)
    e = Coordinate(0, 1)

    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))