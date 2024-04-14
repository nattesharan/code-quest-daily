# Depth-First Search (DFS) for Graphs

## Introduction
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It traverses the depth of any particular branch before moving on to explore other branches.

## Algorithm Overview
DFS can be implemented using either recursion or an iterative approach using a stack (explicit or implicit call stack).

### Recursive DFS Algorithm
1. Start from a given vertex (start vertex).
2. Mark the start vertex as visited.
3. For each unvisited neighbor of the start vertex:
   - Recursively perform DFS from that neighbor.
4. Backtrack when all neighbors have been visited.

### Iterative DFS Algorithm (using an explicit stack)
1. Push the start vertex onto the stack.
2. While the stack is not empty:
   - Pop a vertex from the stack.
   - If the vertex is not visited:
     - Mark it as visited.
     - Push its unvisited neighbors onto the stack.
3. Continue until the stack is empty.

## Problem Description
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.

**Example 1:**
Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
Output: 0 2 4 3 1
Explanation: 0 is connected to 2, 3, 1.
1 is connected to 0.
2 is connected to 0 and 4.
3 is connected to 0.
4 is connected to 2.
so starting from 0, it will go to 2 then 4,
and then 3 and 1.
Thus dfs will be 0 2 4 3 1.

**Example 2:**
Input: V = 4, adj = [[1,3], [2,0], [1], [0]]
Output: 0 1 2 3
Explanation:
0 is connected to 1 , 3.
1 is connected to 0, 2. 
2 is connected to 1.
3 is connected to 0. 
so starting from 0, it will go to 1 then 2
then back to 0 then 0 to 3
thus dfs will be 0 1 2 3.