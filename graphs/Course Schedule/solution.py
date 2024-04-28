from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        for prerequisite in prerequisites:
            a, b = prerequisite
            adj_list[b].append(a)
            indegree[a] += 1
        queue = []
        count = 0
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
                count += 1
        while queue:
            u = queue.pop(0)
            for v in adj_list[u]:
                indegree[v] -= 1
                if not indegree[v]:
                    queue.append(v)
                    count += 1
        if count == numCourses:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(solution.canFinish(numCourses, prerequisites))