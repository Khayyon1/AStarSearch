
def generateGrid(n):
    return [[0 for col in range(n)] for row in range(n)]


def initializeNodes(graph):
    '''
        Convert 2D array into 2D array of Nodes with attributes needed
        to implement A* Search Algorithm
    '''
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes