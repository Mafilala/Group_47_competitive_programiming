class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = [[] for _ in range(3)]
        for n in nums:
            if n < pivot:
                arr[0].append(n)
            elif n == pivot:
                arr[1].append(n)
            else:
                arr[2].append(n)
        return arr[0] + arr[1] + arr[2]
