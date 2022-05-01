from enum import IntEnum
from abc import ABC
import logging
from src import Heuristic

log = logging.getLogger()

class AlgorithmType(IntEnum):
    UniformCostSearch = 1
    AStar_MisplacedTile = 2
    AStar_EuclideanDistance = 3

# Search Algorithm Abstract Class
class SearchAlgorithm(ABC):
    def search(self):
        pass

class Fetcher:
    def get(self, algorithm: AlgorithmType) -> SearchAlgorithm:
        if algorithm == AlgorithmType.UniformCostSearch:
            return UniformCostSearch()
        elif algorithm == AlgorithmType.AStar_MisplacedTile:
            return AStar(Heuristic.MisplacedTile())
        elif algorithm == AlgorithmType.AStar_EuclideanDistance:
            return AStar(Heuristic.EuclideanDistance())

class UniformCostSearch(SearchAlgorithm):
    def search(self):
        print("Searching using Uniform Cost Search")

class AStar(SearchAlgorithm):
    def __init__(self, heuristic: Heuristic.Heuristic):
        self.heuristic = heuristic
    
    def search(self):
        print("Searching using A*")
        self.heuristic.evaluate()
    
