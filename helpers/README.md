# Helpers
This is a directory that contains helpers methods group by the functions that they assist in the A* Search. This can be classes, generate new graphs and grids and etc.

# What's in the 'bax'?
* graph/ - Directory containing helper methods for the graph
    * graph_helper.py - contains the following functions:
        * generateGrid(n) - Generates an N by N grid of 0s
        * initializeNodes(graph) - it turns the 2D array of integers into a 2D array of Nodes
        
* node/ - Directory containing helper methods for the Node
    * node_helper.py - contains the following functions:
        * getNeighboringNodes(node, nodes) - Get the neighboring nodes of the currentNode (i.e. node). Currently design to get at most four neighbors
        * reconstructPath(endNode: Node) - Generates the path taken from the endNode back to start using the Node class's cameFrom attribute.
