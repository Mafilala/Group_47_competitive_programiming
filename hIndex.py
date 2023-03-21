class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(h):
            h_ = 0
            for c in citations:
                if c >= h:
                    h_ += 1
            return h_ >=  h
            
        low, high = 0, len(citations)
        while low < high:
            mid = (low + high) // 2 + 1
            if valid(mid):
                low = mid
            else:
                high = mid - 1
        return low if valid(low) else 0
