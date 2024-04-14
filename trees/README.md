# Trees

## Introduction
A tree is a hierarchical data structure that consists of nodes connected by edges. Each node in a tree has a value and zero or more child nodes. Trees are widely used in programming for representing hierarchical data such as file systems, organizational charts, and more.

## Terminology
- **Root Node:** The topmost node in a tree.
- **Parent Node:** A node that has child nodes.
- **Child Node:** A node directly connected to another node when moving away from the root.
- **Leaf Node:** A node with no children.
- **Height of a Tree:** The length of the longest path from the root to a leaf node.
- **Depth of a Node:** The length of the path from the root to that node.
- **Binary Tree:** A tree in which each node has at most two children, often referred to as the left child and the right child.

## Types of Trees
### 1. Binary Trees
A binary tree is a tree in which each node has at most two children.

### 2. Binary Search Tree (BST)
A binary search tree is a binary tree in which the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value. This property makes searching, insertion, and deletion operations efficient.

## Tree Traversal
Traversal refers to visiting all nodes of a tree in a specific order. There are three common ways to traverse a tree:
- **Inorder Traversal:** Left subtree, root, right subtree.
- **Preorder Traversal:** Root, left subtree, right subtree.
- **Postorder Traversal:** Left subtree, right subtree, root.
