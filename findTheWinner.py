class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recurse(arr):
            if len(arr) == 1:
                return arr.pop()
            else:
                idx = (k - 1) % len(arr)
                new_arr = arr[idx + 1:] + arr[:idx]
                return recurse(new_arr)
        first_arr = [x for x in range(1, n + 1)]
        return recurse(first_arr)
