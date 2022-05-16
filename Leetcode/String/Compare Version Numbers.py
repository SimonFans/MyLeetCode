'''
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split('.')
        lst2 = version2.split('.')
        n1 = len(lst1)
        n2 = len(lst2)
        # version1 = "1.01" => ['1', '01']
        for i in range(max(n1, n2)):
            v1 = int(lst1[i]) if i < n1 else 0
            v2 = int(lst2[i]) if i < n2 else 0
            if v1 != v2:
                return -1 if v1 < v2 else 1
        return 0

# Time: O(n1+n2+max(n1,n2))
# Space: O(n1+n2)
