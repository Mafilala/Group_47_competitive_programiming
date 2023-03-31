class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        f_half = (len(nums) + 1) // 2
        ans = [0] * len(nums)
        ans[::2] = nums[:f_half]
        ans[1::2] = nums[f_half:]
        return ans
