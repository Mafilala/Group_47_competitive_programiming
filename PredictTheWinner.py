class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(l, r, turn):
            if l == r:
                return nums[l] * turn
            front = nums[l] * turn + winner(l + 1, r, -turn)
            back = nums[r] * turn + winner(l, r - 1, -turn)
            return turn * max(front * turn, back * turn)
        return winner(0, len(nums) - 1, 1) >= 0
