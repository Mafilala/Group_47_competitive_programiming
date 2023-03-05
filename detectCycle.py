class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rab, tor = head, head
        while rab and rab.next and rab.next.next:
            rab = rab.next.next
            tor = tor.next
            if rab == tor:
                tor = head
                while True:
                    if tor == rab:
                        return tor
                    tor = tor.next
                    rab = rab.next
