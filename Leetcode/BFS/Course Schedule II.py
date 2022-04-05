'''
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
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
            ans.append(course)
            for next_course in prev_next_relation[course]:
                inDegree[next_course] -= 1
                # All prerequisites for this course have been completed, can start this course, add to queue
                if inDegree[next_course] == 0:
                    queue.append(next_course)
        return ans if not sum(inDegree) else []
