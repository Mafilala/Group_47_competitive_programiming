class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def isBound(r, c):
            return (0 <= r < m and 0 <= c < n)
        
        def dp(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if not isBound(r, c):
                return 0
            state = (r, c)
            if state in memo:
                return memo[state]

            result = dp(r + 1,c) + dp(r, c + 1)
            memo[state] = result
            return result
            
        return dp(0, 0)
