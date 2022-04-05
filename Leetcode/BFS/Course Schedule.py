'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [1,0] => 0 is the prerequisite of 1, so {0: [1]}
        prev_next_relation = defaultdict(list)
        # each course has a inDegree, the number means how many prerequites it needs before the current course can be taken
        inDegree = [0] * numCourses
        # fill in relations between prerequites and next course
        for _next, _prev in prerequisites:
            prev_next_relation[_prev].append(_next)
            inDegree[_next] += 1
        # queue: start from which course doesn't have prerequisites
        queue = deque([i for i in range(len(inDegree)) if inDegree[i] == 0])
        while queue:
            course = queue.popleft()
            for next_course in prev_next_relation[course]:
                inDegree[next_course] -= 1
                # All prerequisites for this course have been completed, can start this course, add to queue
                if inDegree[next_course] == 0:
                    queue.append(next_course)
        return not sum(inDegree)

Time: O(V+E)
Space: O(V)

### dfs

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # edge cases
        if numCourses == 0:
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        state = [0] * numCourses

        # state == 0 inital state, state == -1 processing, state = 1 visited
        def isCycle(u):

            if state[u] == -1:
                return True

            if state[u] == 1:
                return False

            # Set state to -1
            state[u] = -1

            for v in graph[u]:
                if isCycle(v):
                    return True

            state[u] = 1

            return False

        for u in range(numCourses):
            if isCycle(u):
                return False

        return True
