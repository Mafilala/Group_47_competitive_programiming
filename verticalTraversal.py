class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        by_columns = defaultdict(list) # stores node values grouped by their column number
        def traverse(node, row, col):
            if not node:
                return
            by_columns[col].append([row, node.val])
            traverse(node.left,row + 1 , col - 1)
            traverse(node.right,row + 1, col + 1)

        traverse(root, 0, 0)
        
        res = []
        
        for key in sorted(by_columns.keys()): # traversing through subLists in ascending order(leftmost col to rightmost col)
            subList = by_columns[key]
            subList.sort() # sorting subList based on their row num, if thier row nums is equall, the node value will be considered
            li = []
            for row, val in subList:
                li.append(val)
            res.append(li)

       
        return res
