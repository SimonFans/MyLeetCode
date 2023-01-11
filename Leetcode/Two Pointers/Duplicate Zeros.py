'''
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count_zero = 0
        for num in arr:
            if num == 0:
                count_zero += 1
        n = len(arr)
        i = n - 1
        j = n + count_zero - 1
        '''
        arr = [1,0,2,3,0,4,5,0]
                             i
        new = [1,0,2,3,0,4,5,0, 0,0,0]
                                    j
        '''
        while i >=0 and j >= 0:
            # no zero found, just write
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
            # if zero found, write twice if we can
            else:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
                if j < n:
                    arr[j] = arr[i]
            i -= 1
            j -= 1


Time: O(n)
Space: O(1) because in place
