class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                val = nums[i] * 2
                nums[i] = val
                nums[i + 1] = 0
        ans = [x for x in nums if x != 0]
        ans += [0] * (len(nums) - len(ans))
        return ans
