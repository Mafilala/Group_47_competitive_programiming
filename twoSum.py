class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            v1 = numbers[left]
            v2 = numbers[right]
            if v1 + v2 == target:
                return [left + 1, right + 1]
            elif v1 + v2 > target:
                right -= 1
            else:
                left += 1
