# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode()
        dummy = merged
        heaps = []
        limit = 0
        for ll in lists:
            heap = []
            while ll:
                limit += 1
                heapq.heappush(heap, ll.val)
                ll = ll.next
            if heap:
                heaps.append(heap)
        l = len(heaps)
        if heaps and heaps[0]:
            min_heap = heaps[0]   
        while limit:
            for heap in heaps:
                if not min_heap:
                    min_heap = heap
                if heap and heap[0] < min_heap[0]:
                    min_heap = heap
            if min_heap:
                val = min_heap[0]
                heapq.heappop(min_heap)
                merged.next = ListNode(val)
                merged = merged.next
            limit -= 1
        return dummy.next
