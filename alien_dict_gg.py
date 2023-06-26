#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        if len(alien_dict) == 1:
            return alien_dict[0]
        incoming = defaultdict(int)
        adj = defaultdict(list)
        first = alien_dict[0]
        for i in range(1, len(alien_dict)):
            second = alien_dict[i]
            idx = 0
            limit = min(len(first), len(second))
            while idx < limit and first[idx] == second[idx]:
                idx += 1
            if idx < limit:
                adj[first[idx]].append(second[idx])
                incoming[second[idx]] += 1
            first = second
        queue = deque()
        for i in range(ord('a'), ord('a') + k):
            letter = chr(i)
            if incoming[letter] == 0:
                queue.append(letter)
        order = ''  
        while queue:
            popped = queue.popleft()
            order += popped
            for child in adj[popped]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        return order
        
