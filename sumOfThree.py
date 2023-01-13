class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num / 3
        if middle != int(middle):
            return []
        middle = int(middle)
        first = middle - 1
        last = middle + 1
        return [first, middle, last]
