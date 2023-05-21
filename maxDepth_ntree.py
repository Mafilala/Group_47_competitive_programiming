# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node):
            if not node.children:
                return 1
            depths = []
            for nd in node.children:
                depths.append(1 + dfs(nd))
            return max(depths)
        
        return dfs(root)
