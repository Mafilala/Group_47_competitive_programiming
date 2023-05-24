class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        while queue:
            subAns = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    subAns.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if subAns:
                ans.append(subAns)
        return ans
