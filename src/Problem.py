import logging
from abc import ABC
import copy

log = logging.getLogger(__name__)

class State:
    def __init__(self, values):
        # Technically, values can be abstracted into anything
        # All that matters is that they represent a state of
        # the problem that is being solved, and that operations
        # can be performed in the generate step of the problem
        # to create all of the available next steps
        self.values = values

    def getRepresentation(self):
        return tuple([value for row in self.values for value in row])
    
    def printValueArray(self):
        for row in self.values:
            for value in row:
                if value == 0:
                    print(f"  ",end="")
                else:
                    print(f"{value} ", end ="")
            print("")
    def get2DArrayRepresentation(self):
        return self.values
    
    def __eq__(self, other):
        if isinstance(other, State):
            return self.values == other.values
        return NotImplemented
    def __lt__(self, other):
        # Arbitrary comparison needed for heappush to work properly with (int, object) types
        # When two pairs have the same first value of the pair, it compares the second.
        # but if two items in the queue have the same distance, it doesn't matter which
        # is returned
        return True

class Problem(ABC):
    def __init__(self, initial: State, goal: State):
        self.initial: State = initial
        self.goal: State = goal

    def generate(self, state: State) -> [State]:
        pass

class PuzzleProblem(Problem):

    def generate(self, puzzle: State) -> [State]:
        puzzle_vals = puzzle.values

        row_cnt = len(puzzle_vals)
        # log.debug(puzzle)
        col_cnt = len(puzzle_vals[0])
        
        states = []
        for i, row in enumerate(puzzle_vals):
            for j, value in enumerate(row):
                if value == 0:
                    # Slide from Above to blank
                    if (i - 1) >= 0:
                        puzzle_copy = copy.deepcopy(puzzle_vals)
                        puzzle_copy[i][j], puzzle_copy[i-1][j] = puzzle_copy[i-1][j], puzzle_copy[i][j]
                        states.append(State(puzzle_copy))

                    # Slide from below to blank
                    if (i+1) < row_cnt:
                        puzzle_copy = copy.deepcopy(puzzle_vals)
                        puzzle_copy[i][j], puzzle_copy[i+1][j] = puzzle_copy[i+1][j], puzzle_copy[i][j]
                        states.append(State(puzzle_copy))

                    # Slide from left to blank
                    if (j - 1) >= 0:
                        puzzle_copy = copy.deepcopy(puzzle_vals)
                        puzzle_copy[i][j], puzzle_copy[i][j - 1] = puzzle_copy[i][j - 1], puzzle_copy[i][j]
                        states.append(State(puzzle_copy))

                    # Slide from right to blank
                    if (j + 1) < col_cnt:
                        puzzle_copy = copy.deepcopy(puzzle_vals)
                        puzzle_copy[i][j], puzzle_copy[i][j + 1] = puzzle_copy[i][j + 1], puzzle_copy[i][j]
                        states.append(State(puzzle_copy))
        return states
