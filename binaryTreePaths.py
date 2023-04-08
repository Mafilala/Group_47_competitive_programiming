class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def traverse(node, val = ''):
            if val != "":
                val += '->'
            val += str(node.val)
            if not (node.left or node.right):
                ans.append(val)
            if node.left:
                traverse(node.left, val)
            if node.right:
                traverse(node.right, val)

        traverse(root)
        return ans
