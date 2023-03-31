class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_ = 0
        k_ = k
        while right < len(nums):
            if nums[right] == 0 and k_ > 0:
                k_ -= 1
                max_ = max(max_, right - left + 1)
                right += 1
            elif nums[right] == 1:
                max_ = max(max_, right - left + 1)
                right += 1
            elif k_ == 0:
                if nums[left] == 0:
                    k_ += 1
                left += 1
        return max_
