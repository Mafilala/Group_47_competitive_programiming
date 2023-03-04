class Solution(object):
    def maxOperations(self, nums, k):
        i = 0
        j = len(nums) - 1
        ops = 0
        nums.sort()
        while i < j:
            val = nums[i] + nums[j]
            if val == k:
                ops += 1
                i += 1
                j -= 1
            elif val > k:
                j -= 1
            else:
                i += 1
        return ops
