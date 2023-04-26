class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minUnfairness = sum(cookies)
        children = [0] * k
        def dfs(cookieIndex, children):
            if cookieIndex == len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(children))
                return
            for i in range(min(cookieIndex + 1, k)):
                children[i] += cookies[cookieIndex]
                dfs(cookieIndex + 1, children)
                children[i] -= cookies[cookieIndex]
        dfs(0, children)
        return self.minUnfairness
