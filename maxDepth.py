class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node):
            if node == None:
                return 0
            left = 1 + depth(node.left)
            right = 1 + depth(node.right)

            return max(left, right)
        return depth(root)
