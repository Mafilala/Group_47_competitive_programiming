class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        def dp(idx, end):
            state = (idx, end)
            if idx == end - 1:
                return nums[idx]
            if idx == end - 2:
                return max(nums[idx], nums[idx + 1])
            if state in memo:
                return memo[state]
            result = max(nums[idx] + dp(idx + 2, end), dp(idx + 1, end))
            memo[state] = result
            return result
        return max(dp(0, n - 1), dp(1, n))
