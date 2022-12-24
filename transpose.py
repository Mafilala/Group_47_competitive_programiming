class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        width = len(matrix[0])
        height = len(matrix)
        ans = []
        for i in range(width):
            sub_ans = []
            for j in range(height):
                sub_ans.append(matrix[j][i])
            ans.append(sub_ans)
        return ans
