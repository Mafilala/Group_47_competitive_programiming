from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def hasCycle(node, color, parent):
		    if color[node] == 1:
		        return True
	        
	        if color[node] == 2:
	            return False
	        color[node] = 1 
            for child in adj[node]:
                if child == parent:
                    continue
                cyclic = hasCycle(child, color, node)
                
                if cyclic:
                    return True
            color[node] = 2
            return False
            
        color = [0] * V
        for node in range(V):
            if color[node] == 0:
                cyclic = hasCycle(node, color, -1)
                if cyclic:
                    return  True
        return False
