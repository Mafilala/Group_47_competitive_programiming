class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = list(str(x))
        return new_x == list(reversed(new_x))
