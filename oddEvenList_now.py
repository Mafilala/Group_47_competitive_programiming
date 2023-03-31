class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        dummy = head
        even = head.next
        even_dummy = even
        odd = head

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            if even.next:
                even.next = odd.next
                even = even.next
                        
        odd.next = even_dummy

        return dummy
