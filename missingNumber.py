class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        li = [x for x in range(n + 1)]
        while i < n:
            if nums[i] != li[i]:
                return li[i]
            i += 1
        return li[i]
