# Detect cycle in an undirected graph

## Problem Description
Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

**Example 1:**
Input:  V = 5, E = 5 adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1

**Example 2:**
Input: V = 4, E = 2 adj = {{}, {2}, {1, 3}, {2}}
Output: 0
