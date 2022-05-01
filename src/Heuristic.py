import logging
from enum import IntEnum
from abc import ABC

log = logging.getLogger()

class HeuristicType(IntEnum):
    MisplacedTile = 2
    EuclideanDistance = 3

class Heuristic(ABC):
    def evaluate(problem):
        pass

class MisplacedTile(Heuristic):
    def evaluate(problem):
        print("Using Misplaced Tile Heuristic")

class EuclideanDistance(Heuristic):
    def evaluate(problem):
        print("Using Euclidean Distance Heuristic")