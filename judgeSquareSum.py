class Solution(object):
    def judgeSquareSum(self, c):
        
        sqrs = [0]
        strt = 1
        
        while True:
             if (strt ** 2) > c:
                    break
             sqrs.append(strt ** 2)
             strt += 1
        i = 0
        j = len(sqrs) - 1
        while i <= j:
            v1 = sqrs[i]
            v2 = sqrs[j]
            if v1 + v2 == c or v1 == c or v2 == c:
                return True
            elif v1 + v2 > c:
                j -= 1
            else:
                i += 1
        return False
