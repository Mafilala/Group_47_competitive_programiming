class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mx = max(arr)
        n = len(arr)
        idx = arr.index(mx)
        for i in range(idx):
            if arr[i] >= mx:
                return -1
        
        for i in range(idx + 1, n):
            if arr[i] >= mx:
                return - 1
        
        return idx
