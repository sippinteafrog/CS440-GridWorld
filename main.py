# import algo1
import time
import timeit
from math import sqrt
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
    goalStateX = goalStateSplit[0]
    goalStateY = goalStateSplit[1]

    startStateX = startStateSplit[0]
    startStateY = startStateSplit[1]

    if startStateSplit == goalStateSplit:
        print('Start state is the goal state')
        return False

    if maze[startStateX][startStateY] == 1 or maze[goalStateX][goalStateY] == 1:
        print('Start state or goal state is a wall. Please ensure start and goal state is not black.')
        return False

    cost = 0
    frontier = []
    openList = []
    solution = []
    path = []
    closedList = []
    candidates = []
    expand = []
    node = []

    frontier.append(startStateSplit)
    maze[startStateX][startStateY] = 2

    i = 0

    while len(frontier) > 0:
        node = frontier.pop(0)

        if node == goalStateSplit:
            openList.append(goalStateX)
            openList.append(goalStateY)
            path.append(openList.copy())
            openList.clear()

            while maze[goalStateX][goalStateY] != 2:

                # LEFT
                if goalStateX != mazeSize and goalStateY - 1 != mazeSize and goalStateY != -1 and goalStateY - 1 != -1:
                    if maze[goalStateX][goalStateY - 1] == i - 1:
                        openList.append(goalStateX)
                        openList.append(goalStateY - 1)
                        path.append(openList.copy())
                        cost += 1
                        goalStateY -= 1

                # RIGHT
                if goalStateX != mazeSize and goalStateY + 1 != mazeSize and goalStateX != -1 and goalStateY + 1 != -1:
                    if maze[goalStateX][goalStateY + 1] == i - 1:
                        openList.append(goalStateX)
                        openList.append(goalStateY + 1)
                        path.append(openList.copy())
                        cost += 1
                        goalStateY += 1

                # UP
                if goalStateX - 1 != mazeSize and goalStateY != mazeSize and goalStateX - 1 != -1 and goalStateY != -1:
                    if maze[goalStateX - 1][goalStateY] == i - 1:
                        openList.append(goalStateX - 1)
                        openList.append(goalStateY)
                        path.append(openList.copy())
                        cost += 2
                        goalStateX -= 1

                # DOWN
                if goalStateX + 1 != mazeSize and goalStateY != mazeSize and goalStateX + 1 != -1 and goalStateY != -1:
                    if maze[goalStateX + 1][goalStateY] == i - 1:
                        openList.append(goalStateX + 1)
                        openList.append(goalStateY)
                        path.append(openList.copy())
                        cost += 2
                        goalStateX += 1

                i -= 1
                openList.clear()

            path.reverse()

            solution.append(path)
            solution.append(cost)

            return solution

        closedList.append(node.copy())

        i = maze[node[0]][node[1]] + 1

        # LEFT y-axis
        if node[0] != -1 and node[1] - 1 != -1 and node[0] != mazeSize and node[1] - 1 != mazeSize:
            if maze[node[0]][node[1] - 1] == 0:
                expand.append(node[0])
                expand.append(node[1] - 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0:
                expand.append(node[0])
                expand.append(node[1] + 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0:
                expand.append(node[0] - 1)
                expand.append(node[1])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0:
                expand.append(node[0] + 1)
                expand.append(node[1])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        for c in candidates:
            if c not in closedList and c not in frontier:
                frontier.append(c.copy())

        candidates.clear()

    return False


def dls(maze, startStateSplit, goalStateSplit, mazeSize):
    goalStateX = goalStateSplit[0]
    goalStateY = goalStateSplit[1]

    startStateX = startStateSplit[0]
    startStateY = startStateSplit[1]

    if startStateSplit == goalStateSplit:
        print('Start state is the goal state')
        return False

    if maze[startStateX][startStateY] == 1 or maze[goalStateX][goalStateY] == 1:
        print('Start state or goal state is a wall. Please ensure start and goal state is not black.')
        return False

    cost = 0
    l = 8
    frontier = []
    openList = []
    solution = []
    path = []
    closedList = []
    candidates = []
    expand = []
    node = []

    frontier.append(startStateSplit)
    maze[startStateX][startStateY] = 2

    i = 0

    while len(frontier) > 0:
        node = frontier.pop()

        if node == goalStateSplit:
            openList.append(goalStateX)
            openList.append(goalStateY)
            path.append(openList.copy())
            openList.clear()

            while maze[goalStateX][goalStateY] != 2:

                # LEFT
                if goalStateX != mazeSize and goalStateY - 1 != mazeSize and goalStateY != -1 and goalStateY - 1 != -1:
                    if maze[goalStateX][goalStateY - 1] == i - 1:
                        openList.append(goalStateX)
                        openList.append(goalStateY - 1)
                        path.append(openList.copy())
                        cost += 1
                        goalStateY -= 1

                # RIGHT
                if goalStateX != mazeSize and goalStateY + 1 != mazeSize and goalStateX != -1 and goalStateY + 1 != -1:
                    if maze[goalStateX][goalStateY + 1] == i - 1:
                        openList.append(goalStateX)
                        openList.append(goalStateY + 1)
                        path.append(openList.copy())
                        cost += 1
                        goalStateY += 1

                # UP
                if goalStateX - 1 != mazeSize and goalStateY != mazeSize and goalStateX - 1 != -1 and goalStateY != -1:
                    if maze[goalStateX - 1][goalStateY] == i - 1:
                        openList.append(goalStateX - 1)
                        openList.append(goalStateY)
                        path.append(openList.copy())
                        cost += 2
                        goalStateX -= 1

                # DOWN
                if goalStateX + 1 != mazeSize and goalStateY != mazeSize and goalStateX + 1 != -1 and goalStateY != -1:
                    if maze[goalStateX + 1][goalStateY] == i - 1:
                        openList.append(goalStateX + 1)
                        openList.append(goalStateY)
                        path.append(openList.copy())
                        cost += 2
                        goalStateX += 1

                i -= 1
                openList.clear()

            path.reverse()

            solution.append(path)
            solution.append(cost)

            return solution

        closedList.append(node.copy())

        i = maze[node[0]][node[1]] + 1

        # LEFT y-axis
        if node[0] != -1 and node[1] - 1 != -1 and node[0] != mazeSize and node[1] - 1 != mazeSize:
            if maze[node[0]][node[1] - 1] == 0 and node[0] < l:
                expand.append(node[0])
                expand.append(node[1] - 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0 and node[0] < l:
                expand.append(node[0])
                expand.append(node[1] + 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0 and node[0] < l:
                expand.append(node[0] - 1)
                expand.append(node[1])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0 and node[0] < l:
                expand.append(node[0] + 1)
                expand.append(node[1])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        for c in candidates:
            if c not in closedList and c not in frontier:
                frontier.append(c.copy())

        candidates.clear()

    return False



def a2():
    # if startStateSplit == goalStateSplit:
    #     print('Start state is the goal state')
    #     return -1
    #
    # if maze[startStateX][startStateY] == 1 or maze[goalStateX][goalStateY] == 1:
    #     print('Start state or goal state is a wall. Please ensure start and goal state is not black.')
    #     return -1

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
    startStateSplit[0] = int(startStateSplit[0])
    startStateSplit[1] = int(startStateSplit[1])
    startStateX = startStateSplit[0]
    startStateY = startStateSplit[1]

    goalState = file.readline()
    goalStateSplit = goalState.split()
    goalStateSplit[0] = int(goalStateSplit[0])
    goalStateSplit[1] = int(goalStateSplit[1])
    goalStateX = goalStateSplit[0]
    goalStateY = goalStateSplit[1]

    algorithm = file.readline()
    algorithm = int(algorithm.rstrip('\n'))

    mazeNumber = file.readline()
    mazeNumber = mazeNumber.rstrip('\n')

    file.close()

    # MazeNumberFile = 'a1/mazes/maze_' + mazeNumber + '.txt'
    MazeNumberFile = 'a1/example_9x9.txt'
    openMaze = open(MazeNumberFile)

    maze = text2Maze(mazeSize, openMaze)
    printMaze = [x[:] for x in maze]

    startTime = time.time() * 1000
    solution = start(algorithm, maze, startStateSplit, goalStateSplit, mazeSize)
    end = time.time() * 1000

    if not solution:
        print('Path Not Found!')

    else:
        # Save the found path and cost
        path = solution[0]
        cost = solution[1]

        print(end - startTime)

        print("\n----------Path----------")
        print(path)
        print('\n----------Length of path----------')
        print(len(path))

        print("\n----------Cost----------")
        print(cost)

        print("\n----------Path Found----------\n")

        pathCopy = path
        while len(pathCopy) != 0:
            printMaze[pathCopy[0][0]][pathCopy[0][1]] = '+'
            pathCopy.pop(0)

        np.set_printoptions(threshold=np.inf)
        print(np.matrix(printMaze))
