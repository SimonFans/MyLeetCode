'''
Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
'''

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        output = []
        for start, end in intervals:
            if remove_end < start or remove_start > end:
                output.append([start,end])
            else:
                if start < remove_start:
                    output.append([start, remove_start])
                if end > remove_end:
                    output.append([remove_end, end])
        return output
