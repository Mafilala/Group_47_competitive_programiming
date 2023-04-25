class Solution:
    def splitString(self, s: str) -> bool:
        ans = False
        def backtrack(idx, state):
            nonlocal ans
            for candidate in get_candidates(idx, state):
                state.append(int(candidate))
                
                next_idx = idx + len(candidate)
                if next_idx == len(s):
                    if len(state) >= 2:
                        ans = True
                        return
                backtrack(next_idx, state)
            if state:
                state.pop()
        def get_candidates(idx, state):
            ini = idx
            candidates = []
            if len(state) == 0:
                while idx < len(s):
                    val = s[ini: idx + 1]
                    candidates.append(val)
                    idx += 1
            else:
                while idx < len(s):
                    val = s[ini: idx + 1]
                    if state[-1] == int(val) + 1:
                        candidates.append(val)
                    elif state[-1] < int(val) + 1:
                        break
                    idx += 1
            return candidates
        backtrack(0, [])
        return ans
