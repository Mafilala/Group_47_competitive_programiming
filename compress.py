class Solution:
    def compress(self, chars: List[str]) -> int:
        char_set = set()
        compressed = []
        left = 0
        right = 0
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            n = right - left
            if n == 1:
                compressed.append(chars[left])
            else:
                compressed.append(chars[left])
                compressed.extend(list(str(n)))
            left = right
        n = len(compressed)
        chars[:n] = compressed
        chars[n:] = []
        return n
