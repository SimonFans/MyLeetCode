'''
Given a triangle array, return the minimum path sum from top to bottom.
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
            2
          3   4
        6   5   7 <- row
      4   1   8   3 <- col
        from bottom to up
        '''
        # total number of rows
        n = len(triangle)-1

        # used for getting the minimum value after comparing with numbers in the below row
        below_row = triangle[-1]

        for row in range(n-1,-1,-1):
            # save the minimum sum each time and use it to update the below row
            current_row = []
            # loop the col in the below row
            for col in range(row + 1):
                mini_val = min(below_row[col], below_row[col+1]) + triangle[row][col]
                current_row.append(mini_val)
                print(current_row)
            # update the below row to the current row, and row pointer goes up one step
            below_row = current_row
        return below_row[0]

'''
Time: O(n^2) A triangle with n rows and n columns contains (1+n)*n//2 ~ O(n^2)
Space: O(n)
'''
