class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ref = arr[:]
        arr.sort(reverse=True)
        ans = []
        j = len(arr)
        for n in arr:
            i = ref.index(n)
            ref[:i + 1] = reversed(ref[:i + 1])
            ans.append(i + 1)
            ans.append(j)
            ref[:j] = reversed(ref[:j])
            j -= 1
        return ans
        
