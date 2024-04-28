from typing import List
from collections import defaultdict

# simple cycle detection in directed graph
class SolutionBFS:
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

class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_cycle_exists(u, adj_list, in_recursion, visited):
            visited.add(u)
            in_recursion.add(u)
            for v in adj_list[u]:
                if v not in visited and dfs_cycle_exists(v, adj_list, in_recursion, visited):
                    return True
                elif v in in_recursion:
                    return True
            in_recursion.remove(u)
            return False

        adj_list = defaultdict(list)
        for prerequisite in prerequisites:
            a, b = prerequisite
            adj_list[b].append(a)
        visited = set()
        in_recursion = set()
        for i in range(numCourses):
            if i not in visited and dfs_cycle_exists(i, adj_list, in_recursion, visited):
                return False
        return True

if __name__ == '__main__':
    solution = SolutionDFS()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(solution.canFinish(numCourses, prerequisites))