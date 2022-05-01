import logging
from enum import IntEnum
from sys import stdin

# Global Function
input = stdin.readline

class AlgorithmType(IntEnum):
    UniformCostSearch = 1
    AStar_MisplacedTile = 2
    AStar_EuclideanDistance = 3

class CLI:
    # CLI Attributes
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    log = logging.getLogger()
    puzzle_side_len = 3

    def run(self):
        self.header()
        print("Welcome to the Eight Puzzle Solver!")
        print("Type 1 to use a default puzzle or 2 to enter your own puzle." )

        option = self.selectOption()

        if option == 1:
            self.log.debug("Running default puzzle")
        else:
            self.log.debug("Running Custom Puzzle")
            self.puzzle = self.getPuzzle()
        
        algorithm = self.selectAlgorithm()


    def header(self):
        title = """   _____      __  __    ___              __      ____     __            
  / __(____ _/ / / /_  / _ \__ ________ / ___   / _____  / _  _____ ____
 / _// / _ `/ _ / __/ / ___/ // /_ /_ // / -_) _\ \/ _ \/ | |/ / -_/ __/
/___/_/\_, /_//_\__/ /_/   \_,_//__/__/_/\__/ /___/\___/_/|___/\__/_/   
------/___/-----------------------------------------------------------
BY SHAWN LONG (SID: 862154223)
        """
        print(title)

    def selectOption(self) -> int:
        try:
            val = int(input())
        except:
            val = 3
            while not (val == 1 or val == 2):
                print("Invalid selection. Please enter either 1 or 2, or q to quit")
                try:
                    val = input()
                    if str(val).strip() == "q":
                        print("Exiting program")
                        exit()
                    val = int(val)
                except Exception as e:
                    self.log.debug(f"CAUGHT ERROR: {e}")
        return val
    
    def getPuzzle(self) -> [[int]]:
        
        print("Enter your puzzle, use a zero to represent the blank")
        print(f"(Each row should be of length {self.puzzle_side_len})")

        validInput = False

        while not validInput:
            try:
                rows = []
                row = []
                for rowNumber in range(1, self.puzzle_side_len+1):
                    print(f"Enter row {rowNumber}, use space between the numbers\n")
                    row = list(map(int, input().split(" ")))
                    rows.append(row)
                validInput = True
                for row in rows: 
                    if len(row) != self.puzzle_side_len: 
                        raise Exception(f"Len of {row} != {self.puzzle_side_len}")

            except Exception as e:
                validInput = False
                self.log.debug(f"CAUGHT ERROR: {e}")
                print("Invalid input entered. To try again, type y")
                if str(input()).strip() != "y":
                    exit()
        self.log.debug(f"Final Puzzle: {rows}")
        return rows

    def selectAlgorithm(self) -> AlgorithmType:
        print("Enter your choice of algorithm")
        print("\t(1) UniformCostSearch")
        print("\t(2) A* with the Misplaced Tile Heuristic")
        print("\t(3) A* with the Euclidean Distance Heuristic")

        try:
            acceptedValues = list(range(1, len(list(AlgorithmType))+1))
            val = int(input())
            self.log.debug(f"Accepted Values: {acceptedValues}")
            if not val in acceptedValues:
                raise Exception(f"Value {val} not in accepted values")
        except Exception as e:
            self.log.debug(f"CAUGHT ERROR: {e}")
            val = 999
            while not val in acceptedValues: 
                print("Invalid input. Please try again or type q to quit")
                val = str(input()).strip()
                if val == "q":
                    print("Exiting Application")
                    exit()
                try:
                    val = int(val)
                except Exception as e:
                    self.log.debug(f"CAUGHT ERROR: {e}")
                    pass
        try:
            alg = AlgorithmType(val)
            self.log.debug(f"Chosen Algorithm: {alg.name}")
            return alg
        except Exception as e:
            log.debug(f"CAUGHT ERROR: {e}")
            log.debug(f"Undefined Behavior Occured, Exiting Application")
            exit()
            

if __name__ == '__main__':
    cli = CLI()
    cli.run()