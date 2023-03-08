class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hash_map = {}
        longest = 1
        for right in range(len(s)):
            val = s[right]
            win_size = right - left + 1
            hash_map[val] = hash_map.get(val, 0) + 1
            if win_size - max(hash_map.values()) <= k:
                longest = max(longest, right - left + 1)
            else:
                val = s[left]
                hash_map[val] -= 1
                left += 1
        return longest
