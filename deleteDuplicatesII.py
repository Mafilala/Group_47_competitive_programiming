class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode()
        dummy = node
        while head:
            if head.next and head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
            else:
                n = ListNode(head.val)
                node.next = n
                node = node.next
                head = head.next
        return dummy.next
