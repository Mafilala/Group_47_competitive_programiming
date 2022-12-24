class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = filter(lambda x: x.isalnum(), s.lower())
        refined = list(refined)
        return refined == list(reversed(refined))
