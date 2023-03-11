class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        store = ["+", "-", "*", "/"]
        for sy in tokens:
            if sy not in store:
                stack.append(sy)
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                ans = int(eval(f"{n1} {sy} {n2}"))
                stack.append(ans)
        return int(stack.pop())
