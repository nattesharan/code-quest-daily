from collections import defaultdict, OrderedDict

class Solution:
    def BFS(self, node, adj_list, visited):
        queue = [node]
        while queue:
            u = queue.pop(0)
            visited[u] = True
            for v in adj_list[u]:
                if v in visited:
                    continue
                queue.append(v)
    
    def bfsOfGraph(self, V, adj):
        adj_list = defaultdict(list)
        for u in range(V):
            adj_list[u] = adj[u]
        visited = OrderedDict()
        self.BFS(0, adj_list, visited)
        return list(visited.keys())

if __name__ == '__main__':
    solution = Solution()
    V = 5
    E = 4 
    adj = [[1,2,3],[],[4],[],[]]
    print(solution.bfsOfGraph(V, adj)) # 0 1 2 3 4