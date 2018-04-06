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


class Solver:
    def __init__(self):
        pass

    def bfs(self):
        pass

    def dfs(self):
        pass

    def ast(self):
        pass


class Node:
    def __init__(self, initialConf):
        if initialConf is not None:
            self.board = [[0] * 3 for i in xrange(3)]
            for i in xrange(3):
                self.board[i] = initialConf[0 + i * 3:3 * (i + 1)]
                for row in range(0, 3):
                    for col in range(0, 3):
                        if self.board[row][col] == 0:
                            self.x = row
                            self.y = col
                            break
            tmpColMoves = []
            tmpRowMoves = []
            if self.x > 0:
                tmpRowMoves.append("U")
            if self.x < 2:
                tmpRowMoves.append("D")
            if self.y > 0:
                tmpColMoves.append("L")
            if self.y < 2:
                tmpColMoves.append("R")

            self.allowedMoves = tmpColMoves + tmpRowMoves

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
    def __init__(self):
        pass


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
    print(ob1 != ob2)
    print ob1.getAllowedMoves()
    print ob2.getAllowedMoves()
