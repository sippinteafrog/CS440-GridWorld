def start(algorithm):
    switcher = {
        0: bfs,
        1: dls,
        2: a2,
        3: a3,
        4: a4
    }

    algo = switcher.get(algorithm, 'Invalid Number')
    return algo()


def bfs():
    return 'bfs0'


def dls():
    return startStateY


def a2():
    return 'a2'


def a3():
    return 'a3'


def a4():
    return 'a4'


if __name__ == '__main__':
    file = open('a1/problem.txt', 'r')
    mazeSize = file.readline()
    mazeSize = mazeSize.rstrip('\n')

    startState = file.readline()
    startStateSplit = startState.split()
    startStateX = startStateSplit[0]
    startStateY = startStateSplit[1]

    goalState = file.readline()
    goalStateSplit = goalState.split()
    goalStateX = goalStateSplit[0]
    goalStateY = goalStateSplit[1]

    algorithm = file.readline()
    algorithm = algorithm.rstrip('\n')

    mazeNumber = file.readline()
    mazeNumber = mazeNumber.rstrip('\n')

    file.close()

    MazeNumberFile = 'a1/mazes/maze_' + mazeNumber + '.txt'
    openMaze = open(MazeNumberFile)

    print(start(int(algorithm)))
