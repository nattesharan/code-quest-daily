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
    
    def isCyclic(self, V : int , adj):
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
    V = 3
    adj = [[1], [2], []]
    print(solution.isCyclic(V, adj))