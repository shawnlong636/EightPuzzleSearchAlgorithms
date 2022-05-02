import unittest
import logging
from src.Problem import PuzzleProblem
from src.Problem import State
from src.Algorithm import UniformCostSearch

log =logging.getLogger()

class TestSample(unittest.TestCase):
    def test_generate(self):
        initial = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        goal = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        puzzle = PuzzleProblem(initial, goal)

        expectedStates = [
            (1,2,3,4,5,0,7,8,6),
            (1,2,3,4,5,6,7,0,8)
        ]

        generatedStates = puzzle.generate(initial)
        self.assertEqual(len(generatedStates), len(expectedStates))

        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)
        
        middleState = State([[1,2,3], [4,0,5], [6, 7, 8]])

        generatedStates = puzzle.generate(middleState)
        expectedStates = [
            (1,0,3,4,2,5,6,7,8),
            (1,2,3,4,7,5,6,0,8),
            (1,2,3,0,4,5,6,7,8),
            (1,2,3,4,5,0,6,7,8)
        ]

        self.assertEqual(len(generatedStates), len(expectedStates))
        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)
        
        topCornerState = State([[0,1,2],[3,4,5],[6,7,8]])
        generatedStates = puzzle.generate(topCornerState)
        expectedStates = [
            (1,0,2,3,4,5,6,7,8),
            (3,1,2,0,4,5,6,7,8)
        ]

        self.assertEqual(len(generatedStates), len(expectedStates))
        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)

    def test_UniformCostSearch(self):
        initial_states = [
            State([[1,2,3],[4,5,6],[7,8,0]]), # Depth 0
            State([[1,2,3],[4,5,0],[7,8,6]]), # Depth 1
            State([[1,2,3],[4,5,6],[7,0,8]]), # Depth 1
            State([[1,2,3],[4,0,6],[7,5,8]]), # Depth 2
            State([[1,5,2],[4,0,3],[7,8,6]]), # Depth 4
            State([[2,4,3],[1,5,6],[0,7,8]]), # Depth 8
            State([[0,4,1],[7,5,2],[8,6,3]]), # Depth 12
            State([[7,4,1],[8,5,2],[0,6,3]])  # Depth 14
        ]
        depths = [0,1,1,2,4,8,12,14]
        goal = State([[1,2,3],[4,5,6],[7,8,0]])
        problems = []

        ucs = UniformCostSearch()

        for state in initial_states:
            problems.append(PuzzleProblem(state, goal))
        
        for index, problem in enumerate(problems):
            results = ucs.search(problem, printValues=False)
            log.debug(index)
            log.debug(problem.initial.getRepresentation())
            self.assertEqual(results.get("goalDepth", None), depths[index])

if __name__ == "__main__":
    unittest.main()