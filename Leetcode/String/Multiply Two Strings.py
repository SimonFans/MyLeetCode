class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        num1 = '12', num2 = '11'
        '''
        # Any of two input strings is '0' then return '0'
        if num1 == '0' or num2 == '0':
            return '0'
        # initialize result list with length(nums1) + length(nums2)
        res = [0] * (len(num1) + len(num2))
        # reverse the string
        first_number = num1[::-1]
        second_number = num2[::-1]

        for index1, num_1 in enumerate(first_number):
            for index2, num_2 in enumerate(second_number):
                pos = index1 + index2
                # load carry flag value
                carry = res[pos]
                # set the position value
                res[pos] = (int(num_1)*int(num_2) + carry) % 10
                # add to the next position in the result list
                res[pos+1] += (int(num_1)*int(num_2) + carry) // 10

        # if num1=12, num2 = 6 then actual return should length = 2, so remove the last pos
        if res[-1] == 0:
            res.pop()
        return ''.join([str(num) for num in res[::-1]])

# Time: O(M*N), Space: O(M+N)
