class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_count = 0
        arr = []
        for i in range(len(strs[0])):
            val = ""
            for j in range(len(strs)):
                val += strs[j][i]
            arr.append(val)
        print(arr)
        for i in range(len(arr)):
            if arr[i] != "".join(sorted(arr[i])):
                del_count += 1

        return del_count
