# Topological Sort Algorithm

## Introduction
Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. It is widely used in scheduling and task management applications.

## Algorithm Overview
Topological sorting can be performed using algorithms such as Depth-First Search (DFS) or Kahn's algorithm.

### Depth-First Search (DFS) Approach
1. Perform DFS on the given DAG.
2. Maintain a stack to store the order of visited vertices.
3. After visiting all neighbors of a vertex, push it onto the stack.
4. Pop elements from the stack to get the topological ordering.

### Kahn's Algorithm
1. Initialize an empty list for the topological ordering.
2. Compute in-degrees for all vertices (number of incoming edges).
3. Enqueue vertices with in-degree 0 into a queue.
4. While the queue is not empty:
   - Dequeue a vertex `v`.
   - Add `v` to the topological ordering.
   - Reduce the in-degree of its neighbors.
   - Enqueue neighbors with in-degree 0.
5. If all vertices are visited, return the topological ordering; otherwise, the graph has a cycle.

## Problem Description
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

### Example
Input:

Sure, here's a README.md file for a topological sort algorithm using the format you provided:

markdown
Copy code
# Topological Sort Algorithm

## Introduction
Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. It is widely used in scheduling and task management applications.

## Algorithm Overview
Topological sorting can be performed using algorithms such as Depth-First Search (DFS) or Kahn's algorithm.

### Depth-First Search (DFS) Approach
1. Perform DFS on the given DAG.
2. Maintain a stack to store the order of visited vertices.
3. After visiting all neighbors of a vertex, push it onto the stack.
4. Pop elements from the stack to get the topological ordering.

### Kahn's Algorithm
1. Initialize an empty list for the topological ordering.
2. Compute in-degrees for all vertices (number of incoming edges).
3. Enqueue vertices with in-degree 0 into a queue.
4. While the queue is not empty:
   - Dequeue a vertex `v`.
   - Add `v` to the topological ordering.
   - Reduce the in-degree of its neighbors.
   - Enqueue neighbors with in-degree 0.
5. If all vertices are visited, return the topological ordering; otherwise, the graph has a cycle.

## Problem Description
Given a DAG, perform a topological sort to find a valid linear ordering of its vertices.

**Example 1:**
Input:
Vertices: 6
Edges: [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
Output: 4 5 2 3 1 0

**Example 2:**
Input:
Vertices: 6
Edges: [(), (3), (3), (), (0, 1), (2, 0)]
Output: 5 4 2 1 3 0