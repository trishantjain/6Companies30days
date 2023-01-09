'''

    --> LeetCode 207.: --Course Schedule--

    Ques. There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where    prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.

'''

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return True

        graph = [[] for _ in range(numCourses)]

        inDegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1

        queue = deque()

        for i in range(0, len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        count = 0

        while len(queue) > 0:
            current = queue.popleft()

            if inDegree[current] == 0:
                count += 1

            if not graph[current]:
                print(f"{current} does not exist in {graph}.")
                continue

            for neighbour in graph[current]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        if count == numCourses: 
            return True 
        else:
            return False


p = Solution()

print(p.canFinish(2, [[1,0],[0,1]]))
