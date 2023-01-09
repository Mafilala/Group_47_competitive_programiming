class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_sum = 0
        for n in nums:
            if n % 2 == 0:
                even_sum += n
        for i in range(len(queries)):
            idx = queries[i][1]
            val = queries[i][0]
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            ans.append(even_sum)
        return ans
