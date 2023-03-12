class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for par in s:
            if par == '(':
                stack.append(0)
            else:
                prev = stack.pop()
                now = max(2 * prev, 1)
                stack[-1] += now
        return stack.pop()
