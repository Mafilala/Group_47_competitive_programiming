class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = ""
        while i < n:
            mul = 0
            if s[i].isalpha():
                ans += s[i]
                i += 1
            else:
                while s[i].isdigit():
                    mul = (mul * 10) + int(s[i])
                    i += 1
                i += 1
                op = 1
                cl = 0
                ret = ""
                while cl < op:
                    if s[i] == "[":
                        op += 1
                    elif s[i] == "]":
                        cl += 1
                    ret += s[i]
                    i += 1
                if mul:
                    ans += mul * self.decodeString(ret[: -1])
                else:
                    ans += self.decodeString(ret[: -1])
        return ans    
