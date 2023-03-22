class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n  = len(intervals)
        first_d_index = []
        for i in range(n):
            first_d_index.append((intervals[i][0], i))
        
        first_d_index.sort(key=lambda x : x[0])
        def ans(interval):
            l = 0
            r = len(intervals) - 1
            while l < r:
                mid = (l + r) // 2 
                if first_d_index[mid][0]  >=  interval[1]:
                    r = mid
                else:
                    l = mid + 1
            if interval[1] <= first_d_index[l][0]:
                return first_d_index[l][1]
            else:
                return -1
        
        answer = []
        for i in intervals:
            answer.append(ans(i))
        return answer
