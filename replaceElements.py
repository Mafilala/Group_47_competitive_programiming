class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp_arr = []
        for i, v in enumerate(arr):
            temp_arr.append((v, i))
        temp_arr.sort(reverse=True)
        ans = []
        j = 0
        for i, n in enumerate(arr):
            while i >= temp_arr[j][1] and j < len(arr) - 1:
                j += 1
            val = temp_arr[j][0]
            ans.append(val)
        if ans:
            ans.pop()
        ans.append(-1)
        return ans
