class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Assume target = 11
amount                  0 1 2 3 4 5 6 7 8 9 10 11
comb no coins           1 0 0 0 0 0 0 0 0 0 0  0
comb 2 coins            1 0 1 0 1 0 1 0 1 0 1  0
combine 2 & 5 coins     1 0 1 0 1 1 1 1 1 1 2  1
combine 2 & 5& 10 coins 1 0 1 0 1 1 1 1 1 1 3  1
        '''
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[amount]

'''
Time: O(N*amount)
Space: O(amount)
'''
