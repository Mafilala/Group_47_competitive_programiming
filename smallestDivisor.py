class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def valid(div):
            cum = 0
            for n in nums:
                cum += math.ceil(n / div)
            return cum <= threshold

        low, high = 1, max(nums)

        while low < high:
            mid = (low + high) // 2
            if  valid(mid):
                high = mid
            else:
                low = mid + 1
        return high
