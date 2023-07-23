class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        ans = mx

        def search(val):
            residue = 0
            for i in range(len(nums) - 1, -1, -1):
                num = nums[i]
                if num < val:
                    residue -= val - num
                    residue = max(0, residue)
                else:
                    residue += num - val
            return residue == 0


        while mn <= mx:
            mid = (mn + mx) // 2
            if search(mid):
                ans = mid
                mx = mid - 1
            else:
                mn = mid + 1
        
        return ans

