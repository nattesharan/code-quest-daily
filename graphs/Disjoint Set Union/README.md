# Disjoint Set Union (DSU) / Union-Find

## Overview

The Disjoint Set Union (DSU), also known as Union-Find, is a data structure that manages a collection of disjoint sets. It supports two main operations:
- **Find**: Identify the set an element belongs to.
- **Union**: Merge two sets into one.

## Features

- **Efficient Operations**: Nearly constant time complexity for both `Find` and `Union`.
- **Path Compression**: Optimizes the `Find` operation.
- **Union by Rank**: Keeps the tree flat and balanced.

## Usage

### Initialization

Create a DSU for `n` elements.

```python
dsu = DisjointSetUnion(n)
