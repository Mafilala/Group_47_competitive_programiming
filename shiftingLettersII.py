class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ref = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        s = list(s)
        let_str_ = []
        let_str = [0] * len(s)
        for letter in s:
            let_str_.append(ord(letter) - ord('a'))
        for l, r, d in shifts:
            dirx = -1 if d == 0 else 1
            let_str[l] += dirx
            if r + 1 < len(s):
                let_str[r + 1] -= dirx
        acc = 0
        for i in range(len(s)):
            idx = let_str[i]
            acc += idx
            let_str[i] = ref[(acc + let_str_[i]) % 26]

        return ''.join(let_str)
