class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = 0
        start = head
        stack = []
        while l < left - 1:
            start = start.next
            l += 1
        temp = start
        l_ = l

        while l < right:
            stack.append(start.val)
            start = start.next
            l += 1

        while l_ < right:
            temp.val = stack.pop()
            temp = temp.next
            l_ += 1

        return head
