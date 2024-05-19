class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])
    
    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)
        if parent_of_u == parent_of_v:
            # if both belong to same set then no need to union again
            return
        self.parent[parent_of_v] = parent_of_u
    
    def belong_same_set(self, u, v):
        return self.find(u) == self.find(v)

class DisjointSetUnionUsingRankAndPathCompression:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)
        if parent_of_u == parent_of_v:
            # if both belong to same set then no need to union again
            return
        if self.rank[parent_of_u] > self.rank[parent_of_v]:
            self.parent[parent_of_v] = parent_of_u
        elif self.rank[parent_of_v] > self.rank[parent_of_u]:
            self.parent[parent_of_u] = parent_of_v
        else:
            self.parent[parent_of_u] = parent_of_v
            self.rank[parent_of_v] += 1

    def belong_same_set(self, u, v):
        return self.find(u) == self.find(v)
    

if __name__ == '__main__':
    dsu = DisjointSetUnionUsingRankAndPathCompression(3)
    dsu.union(0, 1)
    print(dsu.belong_same_set(0, 1))
    print(dsu.belong_same_set(1, 2))
    dsu.union(1, 2)
    print(dsu.belong_same_set(1, 2))

