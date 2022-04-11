'''
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

Input: digits = ""
Output: []
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(index, path):
            # when # of letters in path == length of digits, found answer
            if len(path) == len(digits):
                combination.append(''.join(path))
                return
            possible_letters = mapping[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        if not digits:
            return []

        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        combination = []
        backtrack(0, [])
        return combination

    # Time: O(N * M^N), where N is the length of digits. If digits = '23', then N is 2.
    # 2 and 3 has 3 letters respectively, so here M = 3. So time complexity is O(2*3^2)

    # space: O(N) the space occupied by the reursion call stack
