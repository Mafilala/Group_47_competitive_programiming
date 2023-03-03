class Solution(object):
    def middleNode(self, head):
        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        return slow
