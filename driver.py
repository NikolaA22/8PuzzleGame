# Your's assignment is to write driver.py, which solves any 8-puzzle board when given an
# arbitrary starting configuration. The program will be executed as follows:
#
# $ python driver.py <method> <board>
#
# The method argument will be one of the following. You need to implement all three of them:
#
# bfs (Breadth-First Search)
#
# dfs (Depth-First Search)
#
# ast (A-Star Search)
#
# The board argument will be a comma-separated list of integers containing no spaces.
# For example, to use the bread-first search strategy to solve the input board
# given by the starting configuration {0,8,7,6,5,4,3,2,1},
# the program will be executed like so (with no spaces between commas):
#
# $ python driver.py bfs 0,8,7,6,5,4,3,2,1
#


#
# When executed, your program will create / write to a file called output.txt, containing the following statistics:
#
# path_to_goal: the sequence of moves taken to reach the goal
#
# cost_of_path: the number of moves taken to reach the goal
#
# nodes_expanded: the number of nodes that have been expanded
#
# search_depth: the depth within the search tree when the goal node is found
#
# max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
#
# running_time: the total running time of the search instance, reported in seconds
#
# max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss
# attribute in the resource module, reported in megabytes
import copy
import sys


class Node:
    def __init__(self, board_configuration):
        if board_configuration is not None:
            self.board = [[0] * 3 for i in xrange(3)]
            for i in xrange(3):
                self.board[i] = board_configuration[0 + i * 3:3 * (i + 1)]
                for row in range(0, 3):
                    for col in range(0, 3):
                        if self.board[row][col] == 0:
                            self.x = row
                            self.y = col
                            break
            self.allowedMoves = []
            if self.x > 0:
                self.allowedMoves.append("U")
            if self.x < 2:
                self.allowedMoves.append("D")
            if self.y > 0:
                self.allowedMoves.append("L")
            if self.y < 2:
                self.allowedMoves.append("R")

    def printBoard(self):
        print self.board

    def printZero(self):
        print self.x, self.y

    def moveUp(self):
        tmp_board = copy.deepcopy(self.board)
        tmp_val = tmp_board[self.x - 1][self.y]
        tmp_board[self.x][self.y] = tmp_val
        tmp_board[self.x - 1][self.y] = 0
        return Node([item for sublist in tmp_board for item in sublist])

    def moveDown(self):
        tmp_board = copy.deepcopy(self.board)
        tmp_val = tmp_board[self.x + 1][self.y]
        tmp_board[self.x][self.y] = tmp_val
        tmp_board[self.x + 1][self.y] = 0
        return Node([item for sublist in tmp_board for item in sublist])

    def moveLeft(self):
        tmp_board = copy.deepcopy(self.board)
        tmp_val = tmp_board[self.x][self.y - 1]
        tmp_board[self.x][self.y] = tmp_val
        tmp_board[self.x][self.y - 1] = 0
        return Node([item for sublist in tmp_board for item in sublist])

    def moveRight(self):
        tmp_board = copy.deepcopy(self.board)
        tmp_val = tmp_board[self.x][self.y + 1]
        tmp_board[self.x][self.y] = tmp_val
        tmp_board[self.x][self.y + 1] = 0
        return Node([item for sublist in tmp_board for item in sublist])

    def getZeroPosition(self):
        return self.x, self.y

    def getAllowedMoves(self):
        return self.allowedMoves

    def __eq__(self, other):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == other.board[i][j]:
                    pass
                else:
                    return False
        return True

    def __ne__(self, other):
        return not self == other


class State:
    def __init__(self, initial_conf):
        self.id = 0
        self.rootState = Node(initial_conf)
        self.currentState = self.rootState
        self.childState = None
        self.parentState = None
        self.action = None  # Keep the action that led from parent to current state
        self.added = False


class Solver:
    def __init__(self, initialState, method):
        self.state = initialState
        self.method = method
        self.goalState = Node([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.frontier = Frontier()
        self.checkId = 0

    def solve(self):  # Pass the argument here as a string: bfs, dfs, ast
        pass

    def bfs(self):
        self.frontier.frontier[self.state.id] = self.state
        self.state.added = True

        while not self.frontier.isEmpty():
            pass

    def dfs(self):
        pass

    def ast(self):
        pass

    def goalTest(self):
        return self.goalState == self.state.currentState


class Frontier:
    def __init__(self):
        self.frontier = dict()

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def isEmpty(self):
        return bool(self.frontier)


if __name__ == '__main__':
    if sys.platform == "win32":
        import psutil

        print("psutil", psutil.Process().memory_info().rss)
    else:
        # Note: if you execute Python from cygwin,
        # the sys.platform is "cygwin"
        # the grading system's sys.platform is "linux2"
        import resource

        print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    ob1 = Node([1, 4, 5, 6, 2, 0, 3, 7, 8])
    ob1.printBoard()
    ob1.printZero()
    ob2 = ob1.moveLeft()
    ob2.printBoard()
    ob2.printZero()
    print(ob1 != ob1)
    print ob1.getAllowedMoves()
    print ob2.getAllowedMoves()
    ob1.printBoard()