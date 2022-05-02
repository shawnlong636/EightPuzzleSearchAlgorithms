import logging
from enum import IntEnum
from src.Problem import State
from abc import ABC
from math import floor
from math import sqrt

log = logging.getLogger(__name__)

class HeuristicType(IntEnum):
    MisplacedTile = 2
    EuclideanDistance = 3

class Heuristic(ABC):
    def evaluate(self, state: State, goal: State):
        pass

class MisplacedTile(Heuristic):
    def evaluate(self, state: State, goal: State):
        stateTiles = list(state.getRepresentation())
        goalTiles = list(goal.getRepresentation())
        misplacedCnt = 0
        for stateTile, goalTile in zip(stateTiles, goalTiles):
            if stateTile != goalTile:
                misplacedCnt += 1
        return misplacedCnt

class EuclideanDistance(Heuristic):
    def evaluate(self, state: State, goal: State):
        stateArray = list(map(float, state.getRepresentation()))
        # log.debug(f"State: {stateArray}")
        goalArray = list(map(float, goal.getRepresentation()))
        # log.debug(f"Goal: {goalArray}")
        
        rowCnt = len(state.get2DArrayRepresentation())
        colCnt = len(state.get2DArrayRepresentation()[0])
        
        x = lambda index: float(index % colCnt)
        y = lambda index: float(floor(index / colCnt))

        sum = 0.0

        for stateIndex, goalIndex in zip(stateArray, goalArray):
            if stateIndex != goalIndex:
                x_state = x(stateIndex)
                y_state = y(stateIndex)

                x_goal = x(goalIndex)
                y_goal = y(goalIndex)
                # log.debug(f"x_goal - x_state: {x_goal - x_state} | y_goal - y_state: {y_goal - y_state}")
                # log.debug(f"Evaluation: {sqrt(((x_state - x_goal) ** 2) + ((y_goal - y_state) ** 2))}")

                sum += sqrt(((x_state - x_goal) ** 2) + ((y_goal - y_state) ** 2))
        
        return sum
        


            
        