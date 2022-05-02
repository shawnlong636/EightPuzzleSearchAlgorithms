import unittest
import logging
from src.Problem import PuzzleProblem
from src.Problem import State

class TestSample(unittest.TestCase):
    def test_generate(self):
        initial = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        goal = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        puzzle = PuzzleProblem(initial, goal)

        expectedStates = [
            [[1, 2, 3], [4, 5, 0], [7, 8, 6]],
            [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        ]

        generatedStates = puzzle.generate(initial)
        self.assertEqual(len(generatedStates), len(expectedStates))

        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)
        
        middleState = State([[1,2,3], [4,0,5], [6, 7, 8]])

        generatedStates = puzzle.generate(middleState)
        expectedStates = [
            [[1,0,3], [4,2,5], [6, 7, 8]],
            [[1,2,3], [4,7,5], [6, 0, 8]],
            [[1,2,3], [0,4,5], [6, 7, 8]],
            [[1,2,3], [4,5,0], [6, 7, 8]]
        ]

        self.assertEqual(len(generatedStates), len(expectedStates))
        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)
        
        topCornerState = State([[0,1,2],[3,4,5],[6,7,8]])
        generatedStates = puzzle.generate(topCornerState)
        expectedStates = [
            [[1,0,2],[3,4,5],[6,7,8]],
            [[3,1,2],[0,4,5],[6,7,8]]
        ]

        self.assertEqual(len(generatedStates), len(expectedStates))
        for state in generatedStates:
            self.assertIn(state.getRepresentation(), expectedStates)
    def test_UniformCostSearch(self):
        initial_states = 

if __name__ == "__main__":
    unittest.main()