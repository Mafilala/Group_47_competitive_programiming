class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(idx):
            if idx >= n:
                return 0
            if idx == n - 1:
                return cost[idx]
            if idx in memo:
                return memo[idx]
            
            memo[idx] = min(cost[idx] + dp(idx + 1), cost[idx] + dp(idx + 2))
            return memo[idx]
        return min(dp(0), dp(1))
        
