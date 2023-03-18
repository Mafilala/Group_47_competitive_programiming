class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(wgt):
          d, w = 1, 0
          for weight in weights:
            if w + weight > wgt:
              d += 1
              w = 0
            w += weight
          return d <= days
         
        l, r = max(weights), sum(weights)
        while l < r:
          mid = (l + r) // 2
          if valid(mid):
            r = mid
          else:
            l = mid + 1
        return r
