from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you

    def extensions(self):
        # TODO
        # override extensions
        # legal extensions are configurations that can be reached by swapping one
        # symbol to the left, right, above, or below "*" with "*"
        open_position = [-1,-1]
        y = 0
        while open_position[0] == -1:
            x = 0
            while open_position[1] == -1 and x < len(self.from_grid[y]):
                if self.from_grid[y][x] == '*':
                    open_position = [y,x]
            y += 1
        possible_moves = set()

        def move_left(grid,open_position):
            result = grid[:]
            y = open_position[0]
            x = open_position[1]
            result[y,x] = result[y,x + 1]
            result[y,x + 1] = "*"
            return result
        def move_right(grid):
            result = grid[:]
            y = open_position[0]
            x = open_position[1]
            result[y,x] = result[y,x - 1]
            result[y,x - 1] = "*"
        def move_up(grid):
            result = grid[:]
            y = open_position[0]
            x = open_position[1]
            result[y,x] = result[y + 1,x]
            result[y + 1,x] = "*"
        def move_down(grid):
            result = grid[:]
            y = open_position[0]
            x = open_position[1]
            result[y,x] = result[y - 1,x]
            result[y - 1,x] = "*"

        if open_position[0] != 0:
            possible_moves.add(move_down(self.from_grid,open_position))
        if open_position[0] != len(self.from_grid) - 1:
            possible_moves.add(move_up(self.from_grid,open_position))
        if open_position[1] != 0:
            possible_moves.add(move_left(self.from_grid,open_position))
        if open_position[1] != len(self.from_grid[0]) - 1:
            possible_moves.add(move_right(self.from_grid,open_position))

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
