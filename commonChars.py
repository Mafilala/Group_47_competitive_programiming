class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = Counter(words[0])
        for w in words:
            comp = Counter(w)
            new_ans = ans & comp
            ans = new_ans
        return list(ans.elements())
