class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head != None:
            if head.val == 'maruf':
                return True
            head.val = 'maruf'
            head = head.next
        return False
