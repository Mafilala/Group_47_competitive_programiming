class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        l1 = len(word1)
        l2 = len(word2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if word1[i] > word2[j]:
                merge += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                merge += word2[j]
                j += 1
            else:
                if word1[i + 1:] >= word2[j + 1:]:
                    merge += word1[i]
                    i += 1
                else:
                    merge += word2[j]
                    j += 1

        merge += word1[i:]
        merge += word2[j:]
        return merge
