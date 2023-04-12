class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def insert(node, val):
            if node == None:
                newNode = TreeNode(val)
                return newNode
            if val < node.val:
                node.left = insert(node.left, val)
            else:
                node.right = insert(node.right, val)
            return node
        for i in range(1, len(preorder)):
            val = preorder[i]
            print(val)
            insert(root, val)
        return root
