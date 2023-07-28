class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(idx, sofar):
            if idx == n - 1:
                if sofar + nums[idx] == target:
                    if nums[idx] == 0:
                        return 2
                    return 1
                if sofar - nums[idx] == target:
                    return 1
                return 0
            state = (idx, sofar)
            if state in memo:
                return memo[state]
            result = dp(idx + 1, sofar + nums[idx]) + dp(idx + 1, sofar - nums[idx])
            memo[state] = result
            return result
        
        return dp(0, 0)
                 
