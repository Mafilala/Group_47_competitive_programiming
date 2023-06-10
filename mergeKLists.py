# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode()
        dummy = merged
        heap = []
        for list_node in lists:
            while list_node:
                heappush(heap, list_node.val)
                list_node = list_node.next
        while heap:
            val = heappop(heap)
            merged.next = ListNode(val)
            merged = merged.next
        return dummy.next
        

        
