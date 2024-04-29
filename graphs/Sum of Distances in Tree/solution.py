from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        total_depth = 0
        adj_list = defaultdict(list)
        children_count = [0]*n
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs_base(adj_list, u, parent, curr_depth):
            nonlocal total_depth
            total_nodes = 1
            total_depth += curr_depth
            for v in adj_list[u]:
                if v == parent:
                    continue
                total_nodes += dfs_base(adj_list, v, u, curr_depth+1)
            children_count[u] = total_nodes
            return total_nodes
        
        def dfs_result(adj_list, u, parent, result):
            
            for v in adj_list[u]:
                if v == parent:
                    continue
                result[v] = result[u] - children_count[v] + (n - children_count[v])
                dfs_result(adj_list, v, u, result)

        # get the sum of distances from initial root which is 0 and populate number child nodes at every node
        dfs_base(adj_list, 0, -1, 0)
        result = [0]*n
        result[0] = total_depth
        dfs_result(adj_list, 0, -1, result)
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(solution.sumOfDistancesInTree(n, edges))