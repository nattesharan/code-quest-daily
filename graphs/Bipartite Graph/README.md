# Bipartite Graph Algorithm

## Introduction
A bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets, \( U \) and \( V \), such that every edge connects a vertex in \( U \) to one in \( V \). This property means that there are no edges between vertices within the same set. Bipartite graphs are used in various applications such as job assignments, matching problems, and network flow problems.

## Algorithm Overview
To check if a graph is bipartite, we can use Breadth-First Search (BFS) or Depth-First Search (DFS) to try to color the graph using two colors. If we can color the graph in such a way that no two adjacent vertices have the same color, then the graph is bipartite.

### Breadth-First Search (BFS) Approach
1. Initialize a color array to store the color assigned to each vertex. Use -1 to indicate that no color is assigned.
2. For each unvisited vertex, perform the following steps:
   - Assign an initial color (e.g., 0) to the vertex.
   - Use a queue to perform BFS, starting from the vertex.
   - For each vertex, assign the opposite color to its adjacent vertices.
   - If an adjacent vertex has the same color as the current vertex, the graph is not bipartite.
3. If all vertices are colored successfully without conflicts, the graph is bipartite.

### Depth-First Search (DFS) Approach
1. Initialize a color array to store the color assigned to each vertex. Use -1 to indicate that no color is assigned.
2. For each unvisited vertex, perform the following steps:
   - Use a stack or recursion to perform DFS, starting from the vertex.
   - For each vertex, assign the opposite color to its adjacent vertices.
   - If an adjacent vertex has the same color as the current vertex, the graph is not bipartite.
3. If all vertices are colored successfully without conflicts, the graph is bipartite.

## Problem Description
Given an undirected graph, determine if it is bipartite. The graph is represented by \( V \) vertices and \( E \) edges.

### Example
**Example 1:**
Input: [[1], [0, 2], [1]]

Ourput: 1

Explanation: The given graph can be colored in two colors so, it is a bipartite graph.
