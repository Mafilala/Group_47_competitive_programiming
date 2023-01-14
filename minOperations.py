class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_indexes = []
        ans = []
        for idx, item in enumerate(boxes):
            if item == '1':
                one_indexes.append(idx)
        for idx, item in enumerate(boxes):
            add = 0
            for i in one_indexes:
                add += abs(idx - i)
            ans.append(add)
        return ans
