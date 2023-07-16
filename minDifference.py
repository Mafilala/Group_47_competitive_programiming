class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        num = nums[-1] - nums[0]
        num = min(num, nums[-4] - nums[0])
        num = min(num, nums[-3] - nums[1])
        num = min(num, nums[-2] - nums[2])
        num = min(num, nums[-1] - nums[3])
        return num
