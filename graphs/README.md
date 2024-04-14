# Graphs

## Introduction
A graph is a non-linear data structure that consists of nodes (vertices) connected by edges. Graphs are used to represent relationships and connections between entities. They are widely used in various applications such as social networks, routing algorithms, and recommendation systems.

## Terminology
- **Vertex (Node):** Represents an entity in the graph.
- **Edge:** Represents a connection or relationship between vertices.
- **Directed Graph (Digraph):** Each edge has a direction, indicating a one-way connection.
- **Undirected Graph:** Edges have no direction, indicating a two-way connection.
- **Weighted Graph:** Edges have weights or costs associated with them.
- **Path:** A sequence of vertices connected by edges.
- **Cycle:** A path that starts and ends at the same vertex.
- **Degree:** The number of edges incident to a vertex.
- **Adjacency:** Two vertices are adjacent if there is an edge connecting them.

## Types of Graphs
1. **Directed Graph (Digraph):** Edges have a direction.
2. **Undirected Graph:** Edges have no direction.
3. **Weighted Graph:** Edges have weights or costs.
4. **Cyclic Graph:** Contains at least one cycle.
5. **Acyclic Graph:** Does not contain any cycles.
6. **Bipartite Graph:** Vertices can be divided into two disjoint sets such that no two vertices within the same set are adjacent.

## Representation of Graphs
1. **Adjacency Matrix:** A 2D matrix where rows and columns represent vertices, and matrix[i][j] indicates whether there is an edge between vertex i and vertex j.
2. **Adjacency List:** A collection of lists or arrays where each list/array represents a vertex and contains its adjacent vertices.

## Graph Traversal
Graph traversal refers to visiting all vertices and edges of a graph in a systematic manner. Common graph traversal algorithms include:
- **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS):** Explores neighbors of a vertex before moving on to the next level of neighbors.