# Breadth-First Search (BFS) for Graphs

## Introduction
Breadth-First Search (BFS) is a graph traversal algorithm that explores all the vertices in a graph at the current depth before moving on to the vertices at the next depth level. It starts at a specified vertex (or node) and visits its neighbors first before moving to the next level of neighbors.

## Algorithm Overview
BFS can be implemented using a queue data structure to keep track of vertices to visit. It follows these steps:
1. Enqueue the start vertex into the queue and mark it as visited.
2. While the queue is not empty:
   - Dequeue a vertex from the front of the queue.
   - Process the dequeued vertex (e.g., print or store its value).
   - Enqueue all unvisited neighbors of the dequeued vertex and mark them as visited.
3. Repeat step 2 until the queue is empty.

## Problem Description
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.

**Example 1:**
Input: V = 5, E = 4 adj = {{1,2,3},{},{4},{},{}}
Output: 0 1 2 3 4
Explanation: 0 is connected to 1 , 2 , 3. 2 is connected to 4. so starting from 0, it will go to 1 then 2 then 3. After this 2 to 4, thus bfs will be 0 1 2 3 4.

**Example 2:**
Input: V = 3, E = 2 adj = {{1,2},{},{}}
Output: 0 1 2
Explanation: 0 is connected to 1 , 2. so starting from 0, it will go to 1 then 2, thus bfs will be 0 1 2. 
