class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s):
            di = defaultdict(int)
            for c in s:
                di[c] += 1
            key = min(di.keys())
            return di[key]

        q, w, a = [], [], []
        for query in queries:
            val = f(query)
            q.append(val)
        
        for word in words:
            val = f(word)
            w.append(val)
        
        w.sort(reverse=True)

        for k in q:
            i = 0
            v = 0
            while i < len(w):
                if k < w[i]:
                    v += 1
                else:
                    break
                i += 1
            a.append(v)
        return a
