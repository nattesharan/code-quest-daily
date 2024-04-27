from collections import defaultdict

class Solution:
    
    def topogical_sort_kahns_algorithm(self, V, adj):
        # contruct indegree dict
        indegree = defaultdict(int)
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        # populate default queue
        queue = []
        for u in range(V):
            if not indegree[u]:
                queue.append(u)
        
        result = []
        while queue:
            u = queue.pop(0)
            result.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                # when indegree is 0 push to queue
                if not indegree[v]:
                    queue.append(v)
        return result
    
    def topolgical_sort_dfs(self, u, visited, adj_list, stack):
        visited.add(u)
        for v in adj_list[u]:
            if v in visited:
                continue
            self.topolgical_sort_dfs(v, visited, adj_list, stack)
        stack.append(u)
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj, use_kahns_algorithm=True):
        if use_kahns_algorithm:
            return self.topogical_sort_kahns_algorithm(V, adj)
        visited = set()
        adj_list = defaultdict(list)
        stack = []
        for u in range(V):
            for v in adj[u]:
                adj_list[u].append(v)
        for i in range(V):
            if i not in visited:
                self.topolgical_sort_dfs(i, visited, adj_list, stack)
        return stack[::-1]

if __name__ == '__main__':
    solution = Solution()
    vertices = 6
    edges = [[], [3], [3], [], [0, 1], [2, 0]]
    print(solution.topoSort(vertices, edges))

# Time complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity - O(V)