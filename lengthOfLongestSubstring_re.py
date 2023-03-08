class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_str = []
        left, right = 0, 0
        longest = 0
        for letter in s:
            while letter in unique_str:
                unique_str.pop(0)
                left += 1
            unique_str.append(letter)
            right += 1
            longest = max(longest, right - left)
        return longest
        
