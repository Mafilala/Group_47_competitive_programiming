class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        mx = max(arr)
        m_idx = arr.index(mx)
        if m_idx == 0 or m_idx == len(arr) - 1:
            return False
        prev = -1
        for i in range(m_idx + 1):
            if prev >= arr[i]:
                return False
            prev = arr[i]
        prev = mx
        for j in range(m_idx + 1, len(arr)):
            if prev <= arr[j]:
                return False
            prev = arr[j]
        return True
