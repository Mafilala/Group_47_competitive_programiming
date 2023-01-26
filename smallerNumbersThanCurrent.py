class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash_map = {}
        sorted_num = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            num = sorted_num[i]
            if num not in hash_map:
                hash_map[num] = i
        for i in range(n):
            num = hash_map[nums[i]]
            ans.append(num)
        return ans
