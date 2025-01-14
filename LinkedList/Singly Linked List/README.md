# Singly Linked List

## Introduction
A Singly Linked List is a linear data structure where each element (called a node) points to the next node in the sequence. It consists of a sequence of nodes, where each node contains a data field and a pointer to the next node in the list. The last node points to null, indicating the end of the list.

## Algorithm Overview
A Singly Linked List supports various operations such as insertion, deletion, traversal, and search. These operations are performed as follows:

### Insertion
1. **At the beginning**: Create a new node, set its next pointer to the current head, and update the head to this new node.
2. **At the end**: Traverse to the end of the list, set the next pointer of the last node to the new node.
3. **At a specific position**: Traverse to the position, set the next pointer of the previous node to the new node, and set the next pointer of the new node to the next node.

### Deletion
1. **From the beginning**: Update the head to point to the next node.
2. **From the end**: Traverse to the second last node, set its next pointer to null.
3. **From a specific position**: Traverse to the node before the target, set its next pointer to skip the target node.

### Traversal
Start from the head node and visit each node by following the next pointers until reaching null.

### Search
Start from the head node and traverse through the list, comparing each node's data with the target value.

## Problem Description
Implement a Singly Linked List with operations for insertion, deletion, traversal, and search. Use the following examples to test your implementation:

**Example 1:**
Input: Insert 1, 2, 3 at the beginning
Output: 3 -> 2 -> 1 -> null
Explanation: Nodes 1, 2, and 3 are inserted at the beginning, resulting in a reversed order.

**Example 2:**
Input: Insert 4, 5 at the end of the list 1 -> 2 -> 3 -> null
Output: 1 -> 2 -> 3 -> 4 -> 5 -> null
Explanation: Nodes 4 and 5 are inserted at the end, extending the list.

**Example 3:**
Input: Delete node at position 2 in list 1 -> 2 -> 3 -> null
Output: 1 -> 3 -> null
Explanation: Node at position 2 (value 2) is deleted, resulting in the list 1 -> 3.
