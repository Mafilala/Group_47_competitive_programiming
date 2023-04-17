class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        reference = defaultdict(int)
        reference[0] = 1
        paths = 0
        def traverse(node, total=0):
            if not node:
                return
            nonlocal paths
            total += node.val
            paths += reference[total - targetSum]
            reference[total] += 1
            traverse(node.left, total)
            traverse(node.right, total)
            reference[total] -= 1
            total -= node.val
            
        traverse(root)
        return paths
