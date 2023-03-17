class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        store = ''
        num = ''
        for ch in s:
            if ch == ']':
                while stack and stack[-1] != '[':
                    store = stack.pop() + store
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                if num:
                    mul = int(num)
                    st = mul * store
                    num = ''
                    store = ''
                    stack.append(st)
            else:
                stack.append(ch)
        return ''.join(stack)
        
