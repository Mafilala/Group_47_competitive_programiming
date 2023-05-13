class Solution:
    def findComplement(self, num: int) -> int:
        idx = 0
        limit = num.bit_length()
        while idx < limit:
            num ^= 1 << idx
            idx += 1
        return num
