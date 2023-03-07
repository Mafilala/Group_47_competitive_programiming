class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[0: k])
        max_ = sum_
        for i in range(len(nums) - k):
            sum_ -= nums[i]
            sum_ += nums[i + k]
            max_ = max(max_, sum_)
        return max_ / k
