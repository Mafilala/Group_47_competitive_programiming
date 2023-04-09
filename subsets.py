    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(i, sub_ans):
            if i == n:
                ans.append(sub_ans.copy())
                return
            sub_ans.append(nums[i])
            dfs(i + 1, sub_ans)
            sub_ans.pop()
            dfs(i + 1, sub_ans)
        dfs(0, [])
        return ans
