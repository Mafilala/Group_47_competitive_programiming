class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs.count("") >= 1:
            return ""
        least = len(strs[0])
        for item in strs:
            if len(item) < least:
                least = len(item)
        ans = ""       
        for index in range(least):
            first = strs[0][index]
            failled = False
            for item in strs:
                if first != item[index]:
                    failled = True
                    break
            if failled:
                break
            ans += first
        return ans
