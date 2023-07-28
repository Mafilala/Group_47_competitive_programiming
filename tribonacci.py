class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(idx):
            if idx == 0:
                return 0
            if idx <= 2:
                return 1
            if idx in memo:
                return memo[idx]
            result = dp(idx - 1) + dp(idx - 2) + dp(idx - 3)
            memo[idx] = result
            return result
        return dp(n)
