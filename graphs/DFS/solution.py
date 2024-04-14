from collections import defaultdict, OrderedDict

class Solution:
    
    def dfs(self, u, adj_list, visited):
        visited[u] = True
        for v in adj_list[u]:
            if v in visited:
                continue
            self.dfs(v, adj_list, visited)
    
    def dfsOfGraph(self, V, adj):
        adj_list = defaultdict(list)
        visited = OrderedDict()
        for u in range(0, V):
            for v in adj[u]:
               adj_list[u].append(v)
        self.dfs(0, adj_list, visited)
        return list(visited.keys())

if __name__ == '__main__':
    solution = Solution()
    V = 5
    adj = [[2,3,1] , [0], [0,4], [0], [2]]
    print(solution.dfsOfGraph(V, adj)) # 0 2 4 3 1

# Time complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity - O(V)

    