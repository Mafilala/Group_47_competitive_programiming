class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime: list[bool] = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False

        start = 2

        while start * start <= n:
            if is_prime[start]:
                mul = start * 2
                while mul < n:
                    is_prime[mul] = False
                    mul += start
            start += 1

        return is_prime.count(True)
