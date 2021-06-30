import math

def calculateManhattanDistance(currentNode, endNode):
    '''
        Calculates the blocks between current and end Node (only up, down, left, and right directions)
    '''
    return abs(endNode.col - currentNode.col) + abs(endNode.row - currentNode.row)

def calculateEuclideanDistance(currentNode, endNode):
    '''
        Calculates the blocks between current and end Node (diagonals included)
    '''
    return math.sqrt((endNode.col - currentNode.col)**2 + (endNode.row - currentNode.row)**2)