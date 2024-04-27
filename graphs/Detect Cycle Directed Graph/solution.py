from typing import List
from collections import defaultdict

class Solution:
    def cycle_dfs(self, u, adj_list, inrecursion, visited):
        visited.add(u)
        inrecursion.add(u)
        for v in adj_list[u]:
            if v not in visited and self.cycle_dfs(v, adj_list, inrecursion, visited):
                return True
            elif v in inrecursion:
                return True
        inrecursion.remove(u)
        return False
    
    # using kahns algorithm
    def cycle_bfs(self, V, adj):
        indegree = defaultdict(int)
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        queue = []
        count = 0
        for v in range(V):
            if not indegree[v]:
                queue.append(v)
                count += 1
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                indegree[v] -= 1
                if not indegree[v]:
                    queue.append(v)
                    count += 1
        # if all nodes are visited then no cycle
        if count == V:
            return False
        return True
    
    def isCyclic(self, V : int , adj, use_bfs=True):
        if use_bfs:
            return self.cycle_bfs(V, adj)
        visited = set()
        inrecursion = set()
        adj_list = defaultdict(list)
        for u in range(V):
            for v in adj[u]:
                adj_list[u].append(v)
        for i in range(V):
            if i not in visited and self.cycle_dfs(i, adj_list, inrecursion, visited):
                return True
        return False
    

if __name__ == '__main__':
    solution = Solution()
    V = 4
    adj = [[1], [2], [3], [3]]
    print(solution.isCyclic(V, adj))
    
# Time complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity - O(V)