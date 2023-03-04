class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        max_ = 0
        store = []
        while j < len(s):
            while i < j and s[j] in store:
                store.pop(0)
                i += 1
            store.append(s[j])
            print(store)
            j += 1
            max_ = max(max_, j - i)
        return max_
