# Distance Metrics
This folder contains the methods used to generate the H-Scores for the nodes in the A* Search function.

## What is the H-score?
H-score, in this context, stands for the <em>Heuristic Score</em>. The heuristic or measure being used in this project to determine what decisions are considered good decisions.

## What is included in this folder?
### distance_metrics/distance.py
It contains two functions:
* calculateManhattanDistance
* calculateEuclideanDistance
We can use these for our H-Score calculation step in A* Search