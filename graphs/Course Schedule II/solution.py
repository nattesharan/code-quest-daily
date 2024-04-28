from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        for prerequisite in prerequisites:
            a, b = prerequisite
            adj_list[b].append(a)
            indegree[a] += 1
        queue = []
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        result = []
        while queue:
            u = queue.pop(0)
            result.append(u)
            for v in adj_list[u]:
                indegree[v] -= 1
                if not indegree[v]:
                    queue.append(v)
        if len(result) != numCourses:
            return []
        return result

if __name__ == '__main__':
    solution = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(solution.findOrder(numCourses, prerequisites))
    