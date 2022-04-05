'''
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if the length of nums1 is greater than nums2, then switch them so that nums1 is smaller
        # than nums2 Time: O(log(len(nums1))) 时间复杂度为短的序列长度
        m = len(nums1)
        n = len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2, m, n = nums2, nums1, n, m

        # low, high means nums1 start and end
        low, high = 0, m
        while low <= high:
            # patition_nums1: # of numbers on left side in the nums1 想象成一个split bar
            # patition_nums2: # of numbers on left side in the nums2
            partition_nums1 = (low + high)//2
            partition_nums2 = (m + n + 1)//2 - partition_nums1
            maxLeft_nums1 = float('-Inf') if partition_nums1 == 0 else nums1[partition_nums1-1]
            minRight_nums1 = float('Inf') if partition_nums1 == m else nums1[partition_nums1]
            maxLeft_nums2 = float('-Inf') if partition_nums2 == 0 else nums2[partition_nums2-1]
            minRight_nums2 = float('Inf') if partition_nums2 == n else nums2[partition_nums2]
            if maxLeft_nums1 <= minRight_nums2 and maxLeft_nums2 <= minRight_nums1:
                if (m+n)%2 == 0:
                    return (max(maxLeft_nums1, maxLeft_nums2) + min(minRight_nums1,minRight_nums2))/2.0
                else:
                    return max(maxLeft_nums1,maxLeft_nums2)
            # we are too far on right side for partition_nums1, go on left side
            elif maxLeft_nums1 > minRight_nums2:
                high = partition_nums1 - 1
            # we are too far on left side for partition_nums1, go on right side
            else:
                low = partition_nums1 + 1
