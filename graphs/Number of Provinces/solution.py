from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(u, adj_list, visited):
            visited.add(u)
            for v in adj_list[u]:
                if v in visited:
                    continue
                dfs(v, adj_list, visited)

        n = len(isConnected)
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, adj_list, visited)
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    count = solution.findCircleNum(isConnected)
    print(count)