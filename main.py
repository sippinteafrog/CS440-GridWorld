# import algo1
import numpy as np


def start(algorithm, maze, startStateSplit, goalStateSplit, mazeSize):
    switcher = {
        0: bfs,
        1: dls,
        2: a2,
        3: a3,
        4: a4
    }

    algo = switcher.get(algorithm, 'Invalid Number')

    return algo(maze, startStateSplit, goalStateSplit, mazeSize)

def text2Maze(mazeSize, openMaze):

    maze = [[0 for x in range(mazeSize)] for y in range(mazeSize)]

    i = 0
    while i != mazeSize:
        j = 0
        while j != mazeSize:
            if j == 0 and i != 0:
                line = prevLine
            else:
                readRow = openMaze.readline()
            array = readRow.split()
            spot = int(array[2])
            maze[i][j] = spot
            j += 1

        x = i
        while i == x:
            if x == mazeSize - 1:
                break
            readRow = openMaze.readline()
            array = readRow.split()
            x = int(array[0])
            prevLine = readRow

        i += 1

    return maze


def bfs(maze, startStateSplit, goalStateSplit, mazeSize):


    return 'bfs'


def dls():
    return 'dls'


def a2():
    return 'a2'


def a3():
    return 'a3'


def a4():
    return 'a4'


if __name__ == '__main__':
    file = open('a1/problem.txt', 'r')
    mazeSize = file.readline()
    mazeSize = int(mazeSize.rstrip('\n'))

    startState = file.readline()
    startStateSplit = startState.split()
    startStateX = int(startStateSplit[0])
    startStateY = int(startStateSplit[1])

    goalState = file.readline()
    goalStateSplit = goalState.split()
    goalStateX = int(goalStateSplit[0])
    goalStateY = int(goalStateSplit[1])

    algorithm = file.readline()
    algorithm = int(algorithm.rstrip('\n'))

    mazeNumber = file.readline()
    mazeNumber = mazeNumber.rstrip('\n')

    file.close()

    # MazeNumberFile = 'a1/mazes/maze_' + mazeNumber + '.txt'
    MazeNumberFile = 'a1/example_3x3.txt'
    openMaze = open(MazeNumberFile)

    maze = text2Maze(mazeSize, openMaze)

    solution = start(algorithm, maze, startStateSplit, goalStateSplit, mazeSize)

    print(solution)


