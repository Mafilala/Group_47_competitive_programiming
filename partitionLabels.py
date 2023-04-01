class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        label_set = set()
        cnt = Counter(s)
        cum = 0
        ans = []
        for right, letter in enumerate(s):
            if letter not in label_set:
                cum += cnt[letter]
                label_set.add(letter)
            cum -= 1
            if cum == 0:
                ans.append(right - left + 1)
                left = right + 1
        return ans
