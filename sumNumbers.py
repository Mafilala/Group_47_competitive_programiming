class Solution:
   
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node, curVal):

            if node and not node.left and not node.right:
                ans.append(int(curVal + str(node.val)))
            if not node:
                return
            dfs(node.left, curVal + str(node.val))
            dfs(node.right, curVal + str(node.val))
        dfs(root, '')
        return sum(ans)
