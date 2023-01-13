class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_map = dict()
        for i, n in enumerate(nums):
            hash_map[n] = i
        for op in operations:
            index = hash_map[op[0]]
            nums[index] = op[1]
            hash_map[op[1]] = index
        return nums
