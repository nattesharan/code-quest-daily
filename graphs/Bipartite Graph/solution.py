class Solution:
    def isBipartite(self, V, adj):
        def is_bipartite(adj, u, colors, current_color):
            colors[u] = current_color
            for v in adj[u]:
                if colors[v] == current_color:
                    return False
                elif colors[v] == -1 and not is_bipartite(adj, v, colors, 1-current_color):
                    return False
            return True
            
        
        colors = [-1] * V
        for i in range(V):
            if colors[i] == -1 and not is_bipartite(adj, i, colors, 0):
                return False
        return True
    
    def isBipartiteBFS(self, V, adj):
        def is_bipartite(adj, i, colors, current_color):
            colors[i] = current_color
            queue = [i]
            while queue:
                u = queue.pop(0)
                for v in adj[u]:
                    if colors[v] == colors[u]:
                        return False
                    elif colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
            return True
        
        colors = [-1] * V
        for i in range(V):
            if colors[i] == -1 and not is_bipartite(adj, i, colors, 0):
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    adj = [[1], [0, 2], [1]]
    print(solution.isBipartite(3, adj))
    print(solution.isBipartiteBFS(3, adj))

# Time complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity - O(V)
        