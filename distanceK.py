\# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque()
        queue.append(root)
        adj_list = defaultdict(list)
        while queue:
            a = queue.popleft()
            val = a.val
            if a.left:
                queue.append(a.left)
                adj_list[val].append(a.left.val)
                adj_list[a.left.val].append(val)
            if a.right:
                adj_list[val].append(a.right.val)
                adj_list[a.right.val].append(val)
                queue.append(a.right)
        bfs_queue = deque()
        bfs_queue.append(target.val)
        visited = set()
        visited.add(target.val)
        while bfs_queue:
            if k == 0:
                ans = []
                while bfs_queue:
                    ans.append(bfs_queue.popleft())
                return ans
            for i in range(len(bfs_queue)):
                node = bfs_queue.popleft()
                for child in adj_list[node]:
                    if child not in visited:
                        bfs_queue.append(child)
                        visited.add(child)
            k -= 1
            
        return []
            
