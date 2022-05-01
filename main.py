import unittest
import sys
import logging
import test
import collections
from src import CommandLineDriver

def main():
    arguments = sys.argv[1:]
    accepted_arguments = ["--test,", "-t", "--continue", "-c"]

    if len(arguments) == 0:
        executeCLI()

    # Check valid arguments
    for argument in arguments:
        if not(argument == "--test" or argument == "--continue" \
                or argument == "-c" or argument == "-t"):
                printInvalidArgument(argument)
                exit(1)
    
    # Execute Tests
    if "--test" in arguments or "-t" in arguments:
        executeUnitTests()

    # Execute CLI
    if "--continue" in arguments or "-c" in arguments:
        executeCLI()

    
def printInvalidArgument(argument: str):
    print(f"Command {argument} not recognized. Please enter --test / -t to run tests and --continue / -c to continue program execution after tests")

def executeCLI():
    cli = CommandLineDriver.CLI()
    cli.run()

def executeUnitTests():
    loader = unittest.TestLoader()
    suite = loader.discover('./test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()