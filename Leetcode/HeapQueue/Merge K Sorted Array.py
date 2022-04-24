'''
arr_list = [[3,6,9],[1,2,3],[9,10,12]]
Answer: [1, 2, 3, 3, 6, 9, 9, 10, 12]
'''

import heapq
arr_list = [[3,6,9],[1,2,3],[9,10,12]]
# minHeap
minHeap = []
res = []
for arr in arr_list:
    if arr:
        heapq.heappush(minHeap, (arr[0],arr[1:]))
while minHeap:
    num, next_arr = heapq.heappop(minHeap)
    res.append(num)
    if next_arr:
        heapq.heappush(minHeap, (next_arr[0], next_arr[1:]))
print(res)


#### 合并两个sorted array in place
arr1 = [1,2,3]
arr2 = [2,5,6,8]

# guarantee arr1 always the longest
if len(arr1) < len(arr2):
    arr1, arr2 = arr2, arr1
# m always the long array length
# n always the short array length
m, n = len(arr1), len(arr2)
arr1.extend([0]*n)
while m > 0 and n > 0:
    if arr1[m-1] > arr2[n-1]:
        arr1[m+n-1] = arr1[m-1]
        m -= 1
    else:
        arr1[m+n-1] = arr2[n-1]
        n -= 1
if n > 0:
    arr1[:n] = arr2[:n]
print(arr1)
