class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Queue = deque()
        Queue.append((0, root))
        ans = 0
        while Queue:
            n = len(Queue)
            store = []
            for _ in range(n):
                idx, next_root = Queue.popleft()
                store.append(idx)
                if next_root.left:
                    new_idx = idx * 2 + 1
                    Queue.append((new_idx,next_root.left))
                if next_root.right:
                    new_idx = idx * 2 + 2
                    Queue.append((new_idx,next_root.right))
            ans = max(ans, max(store) - min(store) + 1)
        return ans
