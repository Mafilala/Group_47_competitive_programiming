class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smaller = ListNode()
        greater = ListNode()
        dummy = smaller
        greater_dummy = greater
        while head:
            if head.val >= x:
                greater.next = head
                head = head.next
                greater = greater.next
            else:
                smaller.next = head
                head = head.next
                smaller = smaller.next
        smaller.next = greater_dummy.next
        greater.next = None
        
        return dummy.next
