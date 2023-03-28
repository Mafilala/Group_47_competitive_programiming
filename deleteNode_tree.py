class Solution:
    def successor(self, node):
            while node.left:
                node = node.left
            return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key == root.val:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                nxt = self.successor(root.right)
                root.val = nxt.val
                root.right = self.deleteNode(root.right, nxt.val)

        return root  
