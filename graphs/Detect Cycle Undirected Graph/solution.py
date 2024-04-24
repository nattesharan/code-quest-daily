from typing import List

class Solution:
    
    def cycle_bfs(self, node, adj, visited):
        queue = [(node, -1)]
        visited.add(node)
        while queue:
            u, parent = queue.pop(0)
            for v in adj[u]:
                if v == parent:
                    continue
                elif v in visited:
                    return True
                else:
                    queue.append((v, u))
                    visited.add(v)
        return False
    
    def cycle_dfs(self, u, adj, visited, parent):
        visited.add(u)
        for v in adj[u]:
            if v == parent:
                continue
            if v in visited:
                return True
            if self.cycle_dfs(v, adj, visited, u):
                return True
        return False
    
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        for i in range(V):
            if i not in visited and self.cycle_bfs(i, adj, visited):
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    V = 5
    E = 5
    adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    print(solution.isCycle(V, adj))

# Time complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity - O(V)