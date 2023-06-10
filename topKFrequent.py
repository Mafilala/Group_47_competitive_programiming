class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        ctr = Counter(words)
        ans = []
        for val, ct in ctr.most_common(k):
            ans.append(val)
        return ans
