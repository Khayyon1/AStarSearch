from distance_metrics import distance
from helpers import graph_helper, node_helper

# Helper Functions
calculateManhattanDistance = distance.calculateManhattanDistance
calculateEuclideanDistance = distance.calculateEuclideanDistance
generateGrid = graph_helper.generateGrid
initializeNodes = graph_helper.initializeNodes
getNeighboringNodes = node_helper.getNeighboringNodes
reconstructPath = node_helper.reconstructPath


def AStartSearch(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    
    # Get the startNode and endNode from nodes grid
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    #initialize the startNode's scores
    # startNode is equal to itself so the distance from start
    # is 0
    startNode.g_score = 0
    startNode.h_score = calculateManhattanDistance(startNode, endNode)

    # add startNode to an list/queue 
    queue = [startNode]
    visited = []

    while queue:
        queue.sort(key=lambda node: node.g_score)
        currentNode = queue.pop(0)

        # The algorithm reached the end
        if currentNode == endNode:
            break

        neighbors = getNeighboringNodes(currentNode, nodes)

        for neighbor in neighbors:
            # If the neighbor was already visited
            if neighbor.value == 1:
                continue

            # Check if new g-score is less than neighbor g-score
            # only continue processing if neighbor's g-score is less 
            # than our current g-score
            provisionalDistanceToNeighbor = currentNode.g_score + 1
            if provisionalDistanceToNeighbor >= neighbor.g_score:
                continue

            neighbor.cameFrom = currentNode
            neighbor.g_score = provisionalDistanceToNeighbor
            neighbor.h_score = provisionalDistanceToNeighbor + calculateManhattanDistance(neighbor, endNode)

            if neighbor not in visited:
                queue.append(neighbor)
            else:
                queue.append(neighbor)
        visited.append(currentNode)
    return reconstructPath(endNode)

if __name__ == '__main__':
    GRID_SIZE = 10
    graph = generateGrid(GRID_SIZE)
    startRow, startCol = 0, 0
    endRow, endCol = 8, 8

    AStartSearch(startRow, startCol, endRow, endCol, graph)