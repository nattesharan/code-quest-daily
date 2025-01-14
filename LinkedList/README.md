# Linked List

## Introduction
A linked list is a linear data structure in which elements are linked using pointers. Each element of a linked list is called a node, and each node has two parts: one that stores data and another that stores the address of the next node in the sequence.

Linked lists are dynamic and can easily grow and shrink in size by allocating or deallocating memory at runtime. They are commonly used in scenarios where frequent insertion and deletion operations are required.

## Terminology
- **Node:** The basic unit of a linked list, which contains data and a pointer to the next node.
- **Head:** The first node of a linked list.
- **Tail:** The last node of a linked list, which points to null or none.
- **Next:** A reference or pointer to the next node in the list.
- **Singly Linked List:** A linked list where each node points to the next node in the sequence.
- **Doubly Linked List:** A linked list where each node has two pointers: one pointing to the next node and one pointing to the previous node.
- **Circular Linked List:** A linked list where the last node points back to the first node, forming a circle.

## Types of Linked Lists
### 1. Singly Linked List
A singly linked list is a type of linked list where each node points to the next node and the last node points to null.

### 2. Doubly Linked List
A doubly linked list is a type of linked list where each node contains two pointers: one to the next node and another to the previous node. This allows for traversal in both directions.

### 3. Circular Linked List
A circular linked list is a variation where the last node points to the first node, forming a circular structure. It can be singly or doubly linked.

## Operations on Linked Lists
### 1. Traversal
Visiting each node in the linked list to perform some operation like printing data.

### 2. Insertion
Adding a new node to the linked list at a specific position (beginning, end, or any position).

### 3. Deletion
Removing a node from the linked list from a specific position (beginning, end, or any position).

### 4. Search
Finding a node in the linked list that contains a specific value.

### 5. Reversal
Reversing the order of nodes in the linked list.

## Advantages of Linked Lists
- Dynamic size.
- Efficient insertion and deletion operations.

## Disadvantages of Linked Lists
- Higher memory usage due to pointers.
- Sequential access only; no direct access to elements.
