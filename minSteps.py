class Solution:
    def minSteps(self, n: int) -> int:
        def prime_factorization(n):
            ans = 0
            div = 2
            while div <= n:
                while div <= n and n % div == 0:
                    ans += div
                    n = n // div
                div += 1
            if n > 1:
                ans += n
            return ans
        return prime_factorization(n)
