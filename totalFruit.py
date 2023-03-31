class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        mx = 0
        hash_map = defaultdict(int)
        for r in range(len(fruits)):
            val = fruits[r]
            hash_map[val] += 1
            if len(hash_map.keys()) <= 2:
                mx = max(mx, r - l + 1)
            else:
                hash_map[fruits[l]] -= 1
                if hash_map[fruits[l]] == 0:
                    del hash_map[fruits[l]]
                l += 1
        return mx
