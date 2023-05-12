class Solution:
    def getSum(self, a: int, b: int) -> int:
        idx = 0
        carry = 0
        ans = 0
        while idx < 32:
            bit_a = a & 1 << idx
            bit_b = b & 1 << idx
            if bit_a and bit_b and carry:
                ans |= 1 << idx
            elif not carry and (bit_a and bit_b):
                carry = 1
            elif not carry and (bit_a or bit_b):
                ans |= 1 << idx
            elif carry and (bit_a or bit_b):
                carry = 1
            elif carry:
                ans |= 1 << idx
                carry = 0
            idx += 1
        if ans & 1 << 31:
            ans = ans - (2 ** 32) 
        return ans
