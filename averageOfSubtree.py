# confession
# I made use of Keni's approach

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def postorder(r):
            nonlocal ans
            if not r: 
                return [0, 0] # n and total
            else:
                total, n = 0, 0
                lf = postorder(r.left)
                rt = postorder(r.right)
                n = lf[0] + rt[0] + 1
                total += r.val + rt[1] + lf[1]
                if total // n == r.val:
                    ans += 1
                return [n, total]
        postorder(root)
        return ans
            
