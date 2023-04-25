class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return set(range(n))
        candidates = set(range(n))
        position = len(state)
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            ans = []
            for idx in state:
                ans.append(self.ans_to_string(idx, n))
            solutions.append(ans)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def ans_to_string(self, idx, n):
        return "." * idx + "Q" + "." * (n - idx - 1)
