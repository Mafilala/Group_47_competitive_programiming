class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        prev = 0
        for n in nums:
            prev += n
            output.append(prev)
        return output
