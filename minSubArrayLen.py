class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        sum_ = sum(nums)
        smallest = length
        if sum_ < target:
            return 0
        else:
            l = 0
            sum_ = 0
            for r in range(length):
                val = nums[r]
                sum_ += val
                while l <= r and sum_ >= target:
                    smallest = min(smallest, r - l + 1)
                    sum_ -= nums[l]
                    l += 1
        return smallest
