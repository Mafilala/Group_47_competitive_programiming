class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = 0
        for j in range(3):
            for i in range(tracker, len(nums)):
                if nums[i] == j:
                    nums[tracker], nums[i] = nums[i], nums[tracker]
                    tracker += 1
