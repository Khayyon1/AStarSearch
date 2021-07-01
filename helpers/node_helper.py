
def getNeighboringNodes(node, nodes):
    neighbors = []

    numRow = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRow - 1:
        neighbors.append(nodes[row + 1][col])
    if row > 0:
        neighbors.append(nodes[row - 1][col])
    if col < numCols - 1:
        neighbors.append(nodes[row][col + 1])
    if col > 0:
        neighbors.append(nodes[row][col - 1])
    # print(neighbors)
    return neighbors

def reconstructPath(endNode):
    if not endNode.cameFrom:
        return []
    currentNode = endNode
    path = []

    while currentNode:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom
    print(path[::-1])
    return path[::-1]
