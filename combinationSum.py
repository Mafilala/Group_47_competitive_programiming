    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(subAns, idx, total):
            if total == target:
                ans.append(subAns.copy())
                return
            elif total > target or len(candidates) <= idx:
                return
            
            subAns.append(candidates[idx])
            helper(subAns, idx, total + candidates[idx])
            subAns.pop()
            helper(subAns, idx + 1,  total)
        helper([], 0, 0)

        return ans
