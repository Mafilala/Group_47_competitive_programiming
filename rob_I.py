class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(idx):
            if idx == n - 1:
                return nums[idx]
            if idx == n - 2:
                return max(nums[idx], nums[idx + 1])
            if idx in memo:
                return memo[idx]
            
            result =  max(nums[idx] + dp(idx + 2), dp(idx + 1))
            memo[idx] = result
            return result
        return dp(0)
