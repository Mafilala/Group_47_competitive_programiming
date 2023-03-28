class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recurse(r):
            if r == None:
                return
        
            recurse(r.left)
            ans.append(r.val)
            recurse(r.right)

        recurse(root)
        return ans
