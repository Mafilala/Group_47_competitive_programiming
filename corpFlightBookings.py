class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        def prefixSum(arr):
            sum_ = 0
            for idx, val in enumerate(arr):
                sum_ += val
                arr[idx] = sum_
            return arr
        answer = [0] * n
        for booking in bookings:
            l = booking[0] - 1
            r = booking[1]
            val = booking[2]
            answer[l] += val
            if r < n:
                answer[r] -= val
        return prefixSum(answer)
