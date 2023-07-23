class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        left = n
        while left > 0 and arr[left] >= arr[left - 1]:
            left -= 1
        print(left)
        if left == 0:
            return arr
        pt = left - 1

        right = n

        while right > pt and arr[right] >= arr[pt]:
            right -= 1
        
        while arr[right] == arr[right - 1]:
            right -= 1
        
        arr[right], arr[pt] = arr[pt], arr[right]
        return arr
