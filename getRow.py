class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            func = self.getRow(rowIndex - 1)
            ans = []
            for i in range(1, len(func)):
                ans.append(func[i - 1] + func[i])
            ans = [1] + ans + [1]
        return ans
