import logging
from enum import IntEnum
from src.Problem import State
from abc import ABC

log = logging.getLogger()

class HeuristicType(IntEnum):
    MisplacedTile = 2
    EuclideanDistance = 3

class Heuristic(ABC):
    def evaluate(state: State):
        pass

class MisplacedTile(Heuristic):
    def evaluate(state: State):
        print("Using Misplaced Tile Heuristic")

class EuclideanDistance(Heuristic):
    def evaluate(state: State):
        print("Using Euclidean Distance Heuristic")