class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = False
        def backtrack(state, idx):
            nonlocal ans
            for candidate in get_candidates(idx, state):
                state.append(int(candidate))
                next_idx = idx + len(candidate)
                if next_idx == len(num):
                    if len(state) > 2:
                        ans = True
                        return
                backtrack(state, next_idx)
            if state:
                state.pop()
        
        def get_candidates(idx, state):
            candidate = []
            if idx == len(num):
                return candidate
            ini = idx
            while idx < len(num):
                val = num[ini: idx + 1]
                if num[ini] == '0' and num[idx] != '0':
                    break
                if len(state) < 2:
                    candidate.append(val)
                else:
                    if int(val) == state[-1] + state[-2]:
                        candidate.append(val)
                        break
                    elif int(val) > state[-1] + state[-2]:
                        break
                idx += 1
            return candidate

        backtrack([], 0)
        return ans
