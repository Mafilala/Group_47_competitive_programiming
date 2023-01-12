class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        index1 = num1.index("+")
        index2 = num2.index("+")
        r1 = int(num1[0 : index1])
        r2 = int(num2[0:index2])
        i1 = int(num1[index1 + 1: -1])
        i2 = int(num2[index2 + 1: -1])
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        r = str(r)
        i = str(i) + "i" 
        ans = r + "+" + i
        return ans
