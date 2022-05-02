from enum import IntEnum
from abc import ABC
import logging
from src import Heuristic
from src import Problem
import heapq
from sys import maxsize

log = logging.getLogger(__name__)

class AlgorithmType(IntEnum):
    UniformCostSearch = 1
    AStar_MisplacedTile = 2
    AStar_EuclideanDistance = 3

# Search Algorithm Abstract Class
class SearchAlgorithm(ABC):
    def search(self, problem: Problem.Problem, maxQueueLimit):
        pass
    def printSummary(self, expandedCnt: int, maxQueueSize: int, goalDepth: int):
        print(f"To solve this problem, the search algorithm expanded a total of {expandedCnt} nodes.")
        print(f"The maximum number of nodes in the queue at any one time: {maxQueueSize}.")
        print(f"The depth of the goal node was {goalDepth}.")

class Fetcher:
    def get(self, algorithm: AlgorithmType) -> SearchAlgorithm:
        if algorithm == AlgorithmType.UniformCostSearch:
            return UniformCostSearch()
        elif algorithm == AlgorithmType.AStar_MisplacedTile:
            return AStar(Heuristic.MisplacedTile())
        elif algorithm == AlgorithmType.AStar_EuclideanDistance:
            return AStar(Heuristic.EuclideanDistance())

class UniformCostSearch(SearchAlgorithm):
    def search(self, problem: Problem.Problem, maxQueueLimit = 50000, printValues = True):
        distances = {}
        visited = set()
        queue = []

        expandedCnt = 0
        maxQueueSize = 0
        initialState = problem.initial
        heapq.heappush(queue, (0, initialState))
        distances[initialState.getRepresentation()] = 0
        if printValues:
            print()

        while len(queue) > 0 and len(queue) < maxQueueLimit:
            maxQueueSize = max(maxQueueSize, len(queue))
            
            dist , curr_state = heapq.heappop(queue)
            curr_state_rep = curr_state.getRepresentation()

            if not curr_state_rep in visited:
                visited.add(curr_state_rep)
                # log.debug(f"Current Node: {curr_state_rep}")

                if curr_state_rep == problem.goal.getRepresentation():
                    if printValues:
                        print("Goal!!!\n")
                        curr_state.printValueArray()
                        print()
                        self.printSummary(expandedCnt, maxQueueSize, distances[curr_state_rep])
                    return {"ExpandedCnt": expandedCnt, "maxQueueSize": maxQueueSize, "goalDepth": distances[curr_state_rep]}
                
                expandedStates = problem.generate(curr_state)
                expandedCnt += 1
                if printValues:
                    print(f"The best state to expand with g(n) = {dist}:")
                    curr_state.printValueArray()
                    print("\nExpanding this node...\n")

                for neighborState in expandedStates:
                    neighbor_rep = neighborState.getRepresentation()
                    # log.debug(f"Neighbor: {neighbor_rep}")
                    if not neighbor_rep in visited:
                        cur_distance = distances[curr_state_rep] + 1
                        
                        if cur_distance < distances.get(neighbor_rep, maxsize):
                            distances[neighbor_rep] = cur_distance

                            # Lookupo the idx of the neighbor if it exists in the queue, otherwise idx = None
                            idx_in_queue = next((idx for idx, pair in enumerate(queue) if pair[1] == neighbor_rep), None)
                            if not idx_in_queue == None:
                                queue[idx_in_queue] = (cur_distance, neighborState)
                                heapq.heapify(queue)
                            else:
                                heapq.heappush(queue, (cur_distance, neighborState))
        
        return {"ExpandedCnt": expandedCnt, "maxQueueSize": maxQueueSize, "goalDepth": distances.get(curr_state_rep, None)}

class AStar(SearchAlgorithm):
    def __init__(self, heuristic: Heuristic.Heuristic):
        self.heuristic = heuristic
    
    def search(self, problem: Problem.Problem, maxQueueLimit = 25000, printValues = True):
        objective_distances = {}
        heuristic_distances = {}
        visited = set()
        queue = []

        expandedCnt = 0
        maxQueueSize = 0
        initialState = problem.initial
        objective_distances[initialState.getRepresentation()] = 0
        heuristic_distances[initialState.getRepresentation()] = self.heuristic.evaluate(problem.initial, problem.goal)
        total_distance = objective_distances[initialState.getRepresentation()] + heuristic_distances[initialState.getRepresentation()]

        heapq.heappush(queue, (total_distance, initialState))
        if printValues:
            print()

        while len(queue) > 0 and len(queue) < maxQueueLimit:
            maxQueueSize = max(maxQueueSize, len(queue))
            
            dist , curr_state = heapq.heappop(queue)
            curr_state_rep = curr_state.getRepresentation()

            if not curr_state_rep in visited:
                visited.add(curr_state_rep)
                # log.debug(f"Current Node: {curr_state_rep}")

                if curr_state_rep == problem.goal.getRepresentation():
                    if printValues:
                        print("Goal!!!\n")
                        curr_state.printValueArray()
                        print()
                        self.printSummary(expandedCnt, maxQueueSize, objective_distances[curr_state_rep])
                    return {"ExpandedCnt": expandedCnt, "maxQueueSize": maxQueueSize, "goalDepth": objective_distances[curr_state_rep]}
                
                expandedStates = problem.generate(curr_state)
                expandedCnt += 1
                if printValues:
                    g_n = objective_distances[curr_state_rep]
                    h_n = heuristic_distances[curr_state_rep]

                    print("The best state to expand with g(n) = {:d} and h(n) = {:.4f}".format(g_n, h_n))
                    curr_state.printValueArray()
                    print("\nExpanding this node...\n")

                for neighborState in expandedStates:
                    neighbor_rep = neighborState.getRepresentation()
                    # log.debug(f"Neighbor: {neighbor_rep}")
                    if not neighbor_rep in visited:
                        # cur_distance = distances[curr_state_rep] + 1.0 + self.heuristic.evaluate(neighborState, problem.goal)
                        objective_distance = objective_distances[curr_state_rep] + 1
                        heuristic_distance = self.heuristic.evaluate(neighborState, problem.goal)
                        total_distance = objective_distance + heuristic_distance
                        
                        if total_distance < objective_distances.get(neighbor_rep, maxsize) + heuristic_distances.get(neighbor_rep, maxsize):
                            objective_distances[neighbor_rep] = objective_distance
                            heuristic_distances[neighbor_rep] = heuristic_distance

                            # Lookup the idx of the neighbor if it exists in the queue, otherwise idx = None
                            idx_in_queue = next((idx for idx, pair in enumerate(queue) if pair[1] == neighbor_rep), None)
                            if not idx_in_queue == None:
                                queue[idx_in_queue] = (total_distance, neighborState)
                                heapq.heapify(queue)
                            else:
                                heapq.heappush(queue, (total_distance, neighborState))
        
        return {"ExpandedCnt": expandedCnt, "maxQueueSize": maxQueueSize, "goalDepth": distances.get(curr_state_rep, None)}
