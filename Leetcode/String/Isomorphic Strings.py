'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Input: s = "egg", t = "add" True
        Input: s = "foo", t = "bar" False
        s = "paper", t = "title"  True
        "badc"
        "baba"
        '''
        if len(s) != len(t):
            return False

        s_t_map = collections.defaultdict(str)
        t_s_map = collections.defaultdict(str)

        for c1, c2 in zip(s,t):
            # No mapping exists in either of the dictionaries
            if c1 not in s_t_map and c2 not in t_s_map:
                s_t_map[c1] = c2
                t_s_map[c2] = c1
            # If the character doesn't exist in one of the dictionaries
            # Or the mapping doesn't match
            elif s_t_map[c1] != c2 or t_s_map[c2] != c1:
                return False
        return True

'''
Time: O(N) process each character in both strings exactly once
Space: O(1) Because the size of the ASCII character set is fixed
'''
