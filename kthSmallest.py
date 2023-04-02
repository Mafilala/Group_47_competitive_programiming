class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def recurse(r):
            if r == None:
                return
        
            recurse(r.left)
            ans.append(r.val)
            recurse(r.right)

        recurse(root)
        return ans[k - 1]
        
