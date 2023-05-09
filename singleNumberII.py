class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            set_count = 0
            for num in nums:
                if num & 1 << i:
                    set_count += 1
            if set_count % 3 != 0:
                ans |= 1 << i
        if ans & 1 << 31:
            return ans - (2 ** 32)
        return ans
