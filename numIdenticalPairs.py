class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp = 0
        l, r = 0, 1
        for l in range(len(nums) - 1):
            for r in range(l + 1, len(nums)):
                if nums[l] == nums[r]:
                    gp += 1
        return gp
