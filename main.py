import time
import timeit
import datetime
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


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


########################################################################################################################

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


########################################################################################################################

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
    count = 0
    while len(frontier) > 0:
        node = frontier.pop(0)

        count += 1
        # print(count)

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

########################################################################################################################


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
    l = 94
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
            if maze[node[0]][node[1] - 1] == 0 and node[0] <= l:
                expand.append(node[0])
                expand.append(node[1] - 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0 and node[0] <= l:
                expand.append(node[0])
                expand.append(node[1] + 1)
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0 and node[0] - 1 <= l:
                expand.append(node[0] - 1)
                expand.append(node[1])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0 and node[0] + 1 <= l:
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

########################################################################################################################


class PriorityQueue():

    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def isEmpty(self):
        return len(self.queue) == 0

    def delete(self):
        max = 0
        for i in range(len(self.queue)):
            item = self.queue[i]
            node = self.queue[max]
            itemCost = item[2] + item[3]
            maxCost = node[2] + node[3]
            if itemCost < maxCost:
                max = i

        item = self.queue[max]
        del self.queue[max]
        return item


def euclidean(i, j):
    x1_2 = j[0] - i[0]
    y1_2 = j[1] - i[1]
    x1_2 = abs(x1_2)
    y1_2 = abs(y1_2)
    return sqrt((x1_2 ** 2) + (y1_2 ** 2))


def manhattan(i, j):
    x1_2 = j[0] - i[0]
    y1_2 = j[1] - i[1]
    x1_2 = abs(x1_2)
    y1_2 = abs(y1_2)
    return x1_2 + y1_2


def h3(i, j):
    return min(euclidean(i, j), manhattan(i, j))


def chebyshev(i, j):
    x1_2 = j[0] - i[0]
    y1_2 = j[1] - i[1]
    x1_2 = abs(x1_2)
    y1_2 = abs(y1_2)
    return max(x1_2, y1_2)

########################################################################################################################


def a2(maze, startStateSplit, goalStateSplit, mazeSize):
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

    frontier = PriorityQueue()

    starter = []
    starter.append(startStateSplit[0])
    starter.append(startStateSplit[1])
    starter.append(euclidean(startStateSplit, goalStateSplit))
    starter.append(0)

    frontier.insert(starter)

    cost = 0
    openList = []
    solution = []
    path = []
    closedList = []
    candidates = []
    expand = []
    node = []

    maze[startStateX][startStateY] = 2

    i = 0
    count = 0
    while len(frontier.queue) > 0:
        node = frontier.delete()

        current = []
        current.append(node[0])
        current.append(node[1])

        # print(current)
        count += 1
        # print(count)

        i = maze[node[0]][node[1]] + 1

        if current == goalStateSplit:
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

        # LEFT y-axis
        if node[0] != -1 and node[1] - 1 != -1 and node[0] != mazeSize and node[1] - 1 != mazeSize:
            if maze[node[0]][node[1] - 1] == 0:
                expand.append(node[0])
                expand.append(node[1] - 1)
                expand.append(euclidean([node[0], node[1] - 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0:
                expand.append(node[0])
                expand.append(node[1] + 1)
                expand.append(euclidean([node[0], node[1] + 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0:
                expand.append(node[0] - 1)
                expand.append(node[1])
                expand.append(euclidean([node[0] - 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0:
                expand.append(node[0] + 1)
                expand.append(node[1])
                expand.append(euclidean([node[0] + 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        for c in candidates:
            if c not in closedList and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()

    return False

########################################################################################################################


def a3(maze, startStateSplit, goalStateSplit, mazeSize):
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

    frontier = PriorityQueue()

    starter = []
    starter.append(startStateSplit[0])
    starter.append(startStateSplit[1])
    starter.append(euclidean(startStateSplit, goalStateSplit))
    starter.append(0)

    frontier.insert(starter)

    cost = 0
    openList = []
    solution = []
    path = []
    closedList = []
    candidates = []
    expand = []
    node = []

    maze[startStateX][startStateY] = 2

    i = 0
    count = 0
    while len(frontier.queue) > 0:
        node = frontier.delete()

        current = []
        current.append(node[0])
        current.append(node[1])

        # print(current)
        count += 1
        # print(count)

        i = maze[node[0]][node[1]] + 1

        if current == goalStateSplit:
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

        # LEFT y-axis
        if node[0] != -1 and node[1] - 1 != -1 and node[0] != mazeSize and node[1] - 1 != mazeSize:
            if maze[node[0]][node[1] - 1] == 0:
                expand.append(node[0])
                expand.append(node[1] - 1)
                expand.append(h3([node[0], node[1] - 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0:
                expand.append(node[0])
                expand.append(node[1] + 1)
                expand.append(h3([node[0], node[1] + 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0:
                expand.append(node[0] - 1)
                expand.append(node[1])
                expand.append(h3([node[0] - 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0:
                expand.append(node[0] + 1)
                expand.append(node[1])
                expand.append(h3([node[0] + 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        for c in candidates:
            if c not in closedList and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()

    return False

########################################################################################################################


def a4(maze, startStateSplit, goalStateSplit, mazeSize):
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

    frontier = PriorityQueue()

    starter = []
    starter.append(startStateSplit[0])
    starter.append(startStateSplit[1])
    starter.append(euclidean(startStateSplit, goalStateSplit))
    starter.append(0)

    frontier.insert(starter)

    cost = 0
    openList = []
    solution = []
    path = []
    closedList = []
    candidates = []
    expand = []
    node = []

    maze[startStateX][startStateY] = 2

    i = 0
    count = 0
    while len(frontier.queue) > 0:
        node = frontier.delete()

        current = []
        current.append(node[0])
        current.append(node[1])

        # print(current)
        count += 1
        # print(count)

        i = maze[node[0]][node[1]] + 1

        if current == goalStateSplit:
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

        # LEFT y-axis
        if node[0] != -1 and node[1] - 1 != -1 and node[0] != mazeSize and node[1] - 1 != mazeSize:
            if maze[node[0]][node[1] - 1] == 0:
                expand.append(node[0])
                expand.append(node[1] - 1)
                expand.append(chebyshev([node[0], node[1] - 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # RIGHT y-axis
        if node[0] != -1 and node[1] + 1 != -1 and node[0] != mazeSize and node[1] + 1 != mazeSize:
            if maze[node[0]][node[1] + 1] == 0:
                expand.append(node[0])
                expand.append(node[1] + 1)
                expand.append(chebyshev([node[0], node[1] + 1], goalStateSplit))
                expand.append(1 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # UP x-axis
        if node[0] - 1 != -1 and node[1] != -1 and node[0] - 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] - 1][node[1]] == 0:
                expand.append(node[0] - 1)
                expand.append(node[1])
                expand.append(chebyshev([node[0] - 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        # DOWN x-axis
        if node[0] + 1 != -1 and node[1] != -1 and node[0] + 1 != mazeSize and node[1] != mazeSize:
            if maze[node[0] + 1][node[1]] == 0:
                expand.append(node[0] + 1)
                expand.append(node[1])
                expand.append(chebyshev([node[0] + 1, node[1]], goalStateSplit))
                expand.append(2 + node[3])
                candidates.append(expand.copy())
                maze[expand[0]][expand[1]] = i
                expand.clear()

        for c in candidates:
            if c not in closedList and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()

    return False

########################################################################################################################


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

    # for i in range(5):
    algorithm = 1
    costs = []
    times = []
    for j in range(101):
        if j < 10:
            mazeNumber = "00" + str(j)
        elif j < 100:
            mazeNumber = "0" + str(j)
        else:
            mazeNumber = "100"

        MazeNumberFile = 'a1/mazes/maze_' + mazeNumber + '.txt'
        openMaze = open(MazeNumberFile)

        maze = text2Maze(mazeSize, openMaze)
        printMaze = [x[:] for x in maze]

        startTime = datetime.datetime.now()
        solution = start(algorithm, maze, startStateSplit, goalStateSplit, mazeSize)
        endTime = datetime.datetime.now()

        print("Maze: " + str(mazeNumber))
        if not solution:
            print('Path Not Found!')

        else:
            path = solution[0]
            cost = solution[1]

            # print("\n----------Path----------")
            # print(path)
            #
            # contains_duplicates = any(path.count(element) > 1 for element in path)
            # print("\nDuplicates:   ", contains_duplicates)
            #
            # print('\n----------Length of path----------')
            # print(len(path))
            #
            # print("\n----------Cost----------")
            # print(cost)

            print("Path: " + str(path))
            print("Length of Path: " + str(len(path)) )
            print("Cost: " + str(cost))

            exec_time = (endTime - startTime).total_seconds() * 1000
            print("Time: " + str(exec_time) + "ms")

            costs.append(cost)
            times.append(exec_time)

            print("\n----------Path Found----------\n")
            pathCopy = path
            while len(pathCopy) != 0:
                printMaze[pathCopy[0][0]][pathCopy[0][1]] = '+'
                pathCopy.pop(0)

            print(np.matrix(printMaze))

    print("# of Paths Found: " + str(len(costs)))
    n_costs = np.array(costs)
    n_times = np.array(times)
    avg_cost = np.average(n_costs)
    avg_time = np.average(n_times)
    print("Average Cost: " + "{:.3f}".format(avg_cost))
    print("Average Time: " + "{:.3f}".format(avg_time))
    plt.plot(n_times, n_costs, "o")
    plt.title("Costs vs Time")
    plt.xlabel("Time")
    plt.ylabel("Cost")
    plt.savefig("Alg " + str(algorithm), dpi=300, bbox_inches='tight')

