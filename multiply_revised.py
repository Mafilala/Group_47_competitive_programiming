class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        nums = {
            "0": 0, "1": 1,"2": 2,"3": 3,"4": 4, "5": 5,"6": 6,"7": 7,"8": 8,"9": 9,}

        m, n = len(num1), len(num2)
        maxSize = min(m, n)
        carry = 0
        res = deque()
        for size, (i, j) in enumerate(
            zip_longest(range(m - 1, -1, -1), range(n - 1, -1, -1), fillvalue=0)
        ):
            size = min(size + 1, maxSize)
            s = (
                sum(
                    nums[num1[a]] * nums[num2[b]]
                    for a, b in zip(range(i, i + size), range(j + size - 1, j - 1, -1))
                )
                + carry
            )
            carry, digit = divmod(s, 10)
            res.appendleft(str(digit))
        size = size - 1

        while size > 0:
            s = (
                sum(
                    nums[num1[a]] * nums[num2[b]]
                    for a, b in zip(range(i, i + size), range(j + size - 1, j - 1, -1))
                )
                + carry
            )
            carry, digit = divmod(s, 10)
            res.appendleft(str(digit))
            size -= 1
        if carry != 0:
            res.appendleft(str(carry))

        return "".join(res)
