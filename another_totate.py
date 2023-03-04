class Solution:
    def rotate(self, nums: List[int], k):
        if k == 0:
            return
        n = len(nums)
        k = k % n
        temp = nums[n - k: n] + nums[:n - k]
        nums[:] = temp
