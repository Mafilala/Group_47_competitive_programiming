class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        hash_set = set()
        for i in range(len(nums)):
            val = str(nums[i])[::-1]
            val = int(val)
            nums.append(int(val))
            hash_set.add(val)
            hash_set.add(nums[i])
        return len(hash_set)
            
